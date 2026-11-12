#!/usr/bin/env python3
"""swissBUILDINGS3D (CityGML) -> assets/gebaeude.js für Horse World.

Was das Skript macht:
1. Liest eine oder mehrere swisstopo-Kacheln (CityGML oder GeoJSON, LV95 / EPSG:2056).
2. Setzt für jedes Haus einen lokalen Nullpunkt in seiner Mitte. Die Ecken werden
   relativ dazu in Zentimetern gespeichert und nur ganz leicht gedreht (damit Norden
   genau wie in der OpenStreetMap-Karte liegt). Drehen ändert keine Längen, die Meter
   bleiben exakt. Die Hausmitte selbst landet genau dort, wo OSM das Haus hat.
3. Wirft alles Unnötige weg: Attribute, IDs, Farben, Bodenflächen unter dem Haus
   und alle Häuser ausserhalb der Spielkarte.
4. Speichert pro Haus: Grundriss (für Zusammenstösse und Minikarte), Ecken in
   Zentimetern und Dreiecke für Dach und Wände.

Aufruf:  python3 tools/swisstopo_to_game.py kachel1.gml kachel2.gml ... -o assets/gebaeude.js
         (auch GeoJSON-Zeilen *.geojsonl(.gz), die ogr2ogr aus der swisstopo-GDB macht)
Nur Python 3, keine Zusatzpakete.
"""
import argparse, json, math, re, sys
import xml.etree.ElementTree as ET

GML = '{http://www.opengis.net/gml}'
BLDG = '{http://www.opengis.net/citygml/building/2.0}'
GEN = '{http://www.opengis.net/citygml/generics/2.0}'

# ---------- Lage der Spielkarte (so wurde karte.js aus OpenStreetMap gerechnet) ----------
KARTE_COS = math.cos(math.radians(47.17686240))   # Breitengrad in der Mitte der OSM-Daten
KARTE_KX = 111320 * KARTE_COS                       # Meter pro Grad nach Osten
KARTE_KZ = 110540                                   # Meter pro Grad nach Süden
KARTE_LON0 = 8.5083875 - 412.3 / KARTE_KX          # Länge der Kartenecke x = 0
KARTE_LAT0 = 47.1771105 + 310.6 / KARTE_KZ         # Breite der Kartenecke z = 0
KARTE_SIZE = (1053, 2972)                           # Breite und Tiefe der Spielkarte (Meter)
CLIP = True                                         # False = auch Häuser ausserhalb der Karte behalten


def lv95_to_wgs84(e, n):
    """swisstopo-Näherungsformel, genau auf etwa 1 Meter."""
    y = (e - 2600000) / 1e6
    x = (n - 1200000) / 1e6
    lon = 2.6779094 + 4.728982 * y + 0.791484 * y * x + 0.1306 * y * x * x - 0.0436 * y ** 3
    lat = 16.9023892 + 3.238272 * x - 0.270978 * y * y - 0.002528 * x * x - 0.0447 * y * y * x - 0.0140 * x ** 3
    return lat * 100 / 36, lon * 100 / 36


def wgs84_to_lv95(lat, lon):
    """Umkehrung der Näherungsformel (für GeoJSON, das ogr2ogr in Grad schreibt)."""
    p = (lat * 3600 - 169028.66) / 10000
    l = (lon * 3600 - 26782.5) / 10000
    e = 2600072.37 + 211455.93 * l - 10938.51 * l * p - 0.36 * l * p * p - 44.54 * l ** 3
    n = 1200147.07 + 308807.95 * p + 3745.25 * l * l + 76.63 * p * p - 194.56 * l * l * p + 119.79 * p ** 3
    return e, n


def karte_from_wgs84(lat, lon):
    return (lon - KARTE_LON0) * KARTE_KX, (KARTE_LAT0 - lat) * KARTE_KZ


def find_local_origin():
    """Sucht Nullpunkt (E0, N0) und Drehwinkel so, dass LV95 möglichst genau auf karte.js passt.
    Es wird nur gedreht und verschoben, nicht gestreckt: die Meter bleiben exakt."""
    lat_mid, lon_mid = KARTE_LAT0 - KARTE_SIZE[1] / 2 / KARTE_KZ, KARTE_LON0 + KARTE_SIZE[0] / 2 / KARTE_KX
    # grob: Mitte der Karte in LV95 suchen (Newton mit numerischer Ableitung)
    e, n = 2681000.0, 1224000.0
    for _ in range(20):
        lat, lon = lv95_to_wgs84(e, n)
        x, z = karte_from_wgs84(lat, lon)
        tx, tz = karte_from_wgs84(lat_mid, lon_mid)
        e += tx - x
        n -= tz - z
    # Kontrollpunkte rund um die Mitte und beste Drehung (Procrustes ohne Massstab)
    src, dst = [], []
    for de in range(-1500, 1501, 250):
        for dn in range(-2000, 2001, 250):
            src.append((de, -dn))                        # LV95 relativ zur Mitte, z nach Süden
            dst.append(karte_from_wgs84(*lv95_to_wgs84(e + de, n + dn)))
    cx = sum(p[0] for p in dst) / len(dst)
    cz = sum(p[1] for p in dst) / len(dst)
    s = c = 0.0
    for (ax, az), (bx, bz) in zip(src, dst):
        bx, bz = bx - cx, bz - cz
        c += ax * bx + az * bz
        s += ax * bz - az * bx
    angle = math.atan2(s, c)
    err = max(math.hypot(math.cos(angle) * ax - math.sin(angle) * az + cx - bx,
                         math.sin(angle) * ax + math.cos(angle) * az + cz - bz) for (ax, az), (bx, bz) in zip(src, dst))
    return e, n, cx, cz, angle, err


# ---------- Geometrie-Helfer ----------
def normal(ring):
    """Flächennormale nach Newell (funktioniert auch für nicht-konvexe Vielecke)."""
    nx = ny = nz = 0.0
    for i in range(len(ring)):
        x1, y1, z1 = ring[i]
        x2, y2, z2 = ring[(i + 1) % len(ring)]
        nx += (y1 - y2) * (z1 + z2)
        ny += (z1 - z2) * (x1 + x2)
        nz += (x1 - x2) * (y1 + y2)
    l = math.sqrt(nx * nx + ny * ny + nz * nz)
    return (nx / l, ny / l, nz / l) if l > 1e-9 else None


def triangulate(ring, nrm):
    """Ohrenschneiden: zerlegt ein Vieleck in Dreiecke (gibt Indizes in ring zurück)."""
    ax = max(range(3), key=lambda k: abs(nrm[k]))     # diese Achse fällt beim Flachdrücken weg
    u, v = [k for k in range(3) if k != ax]
    sign = 1 if nrm[ax] > 0 else -1
    pts = [(p[u], p[v]) for p in ring]
    if (u, v) == (0, 2):
        sign = -sign                                  # (x, z) ist gegen (z, x) gespiegelt
    idx = list(range(len(pts)))
    cross = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    tris, guard = [], 0
    while len(idx) > 3 and guard < 10000:
        guard += 1
        for k in range(len(idx)):
            i0, i1, i2 = idx[k - 1], idx[k], idx[(k + 1) % len(idx)]
            a, b, c = pts[i0], pts[i1], pts[i2]
            if cross(a, b, c) * sign <= 1e-12:
                continue                              # Ecke zeigt nach innen
            if any(cross(a, b, pts[j]) * sign > 0 and cross(b, c, pts[j]) * sign > 0 and cross(c, a, pts[j]) * sign > 0
                   for j in idx if j not in (i0, i1, i2)):
                continue                              # ein anderer Punkt liegt im Ohr
            tris.append((i0, i1, i2))
            idx.pop(k)
            break
        else:
            break                                     # kaputtes Vieleck: Rest als Fächer
    for k in range(1, len(idx) - 1):
        tris.append((idx[0], idx[k], idx[k + 1]))
    return tris


def area2(pts):
    return sum(pts[i][0] * pts[i - 1][1] - pts[i - 1][0] * pts[i][1] for i in range(len(pts)))


def inside(x, z, pts):
    hit = False
    for i in range(len(pts)):
        (ax, az), (bx, bz) = pts[i], pts[i - 1]
        if (az > z) != (bz > z) and x < (bx - ax) * (z - az) / (bz - az) + ax:
            hit = not hit
    return hit


def outline(pieces):
    """Viele Bodenstücke (oft Dreiecke) -> Umriss des Hauses.
    Eine Kante, die zwei Stücke gemeinsam haben, liegt innen und fällt weg. Der Rest wird zu Ringen verkettet."""
    key = lambda p: (round(p[0] * 100), round(p[1] * 100))
    count, point = {}, {}
    for pts in pieces:
        for i in range(len(pts)):
            a, b = key(pts[i - 1]), key(pts[i])
            if a == b:
                continue
            point[a], point[b] = pts[i - 1], pts[i]
            edge = (min(a, b), max(a, b))
            count[edge] = count.get(edge, 0) + 1
    nxt = {}
    for a, b in (e for e, c in count.items() if c == 1):
        nxt.setdefault(a, []).append(b)
        nxt.setdefault(b, []).append(a)
    loops, used = [], set()
    for start in list(nxt):
        if start in used:
            continue
        loop, prev, cur = [], None, start
        while cur not in used:
            used.add(cur)
            loop.append(point[cur])
            options = [n for n in nxt[cur] if n != prev and n not in used]
            if not options:
                break
            prev, cur = cur, options[0]
        if len(loop) >= 3 and abs(area2(loop)) > 4:     # winzige Ringe weglassen
            loops.append(loop)
    # Löcher (Innenhöfe) weglassen: Ringe, die in einem anderen Ring liegen
    return [l for l in loops if not any(o is not l and abs(area2(o)) > abs(area2(l)) and inside(*l[0], o) for o in loops)]


def read_rings(element):
    for pl in element.iter(GML + 'posList'):
        v = list(map(float, pl.text.split()))
        ring = [tuple(v[i:i + 3]) for i in range(0, len(v), 3)]
        if len(ring) > 1 and ring[0] == ring[-1]:
            ring.pop()                                # letzter Punkt = erster Punkt
        if len(ring) >= 3:
            yield ring


def building_rings(b):
    """Flächen eines Hauses als (Art, Ring): zuerst die beschrifteten Dach-, Wand- und Bodenflächen,
    sonst der Volumenkörper (dann entscheidet die Richtung der Fläche)."""
    kinds = {BLDG + 'RoofSurface': 'dach', BLDG + 'WallSurface': 'wand', BLDG + 'GroundSurface': 'boden'}
    surfaces = [s for s in b.iter() if s.tag in kinds]
    if surfaces:
        for s in surfaces:
            for r in read_rings(s):
                yield kinds[s.tag], r
        return
    for s in b.iter(BLDG + 'lod2Solid'):
        yield from classify(list(read_rings(s)))


def classify(rings):
    """Flächen ohne Beschriftung: senkrecht = Wand, flach und ganz unten = Boden, sonst Dach."""
    lowest = min(p[2] for r in rings for p in r)
    for r in rings:
        n = normal(r)
        if n is None:
            continue
        if abs(n[2]) < 0.17:
            yield 'wand', r
        elif abs(n[2]) > 0.98 and max(p[2] for p in r) < lowest + 0.3:
            yield 'boden', r
        else:
            yield 'dach', r


def read_geojson(path):
    """GeoJSON-Zeilen (aus der swisstopo-GDB mit ogr2ogr): ein Haus pro Zeile."""
    import gzip
    opener = gzip.open if path.endswith('.gz') else open
    with opener(path, 'rt', encoding='utf-8') as f:
        for line in f:
            feature = json.loads(line)
            geom = feature.get('geometry') or {}
            polys = geom.get('coordinates', []) if geom.get('type') == 'MultiPolygon' else [geom.get('coordinates', [])] if geom.get('type') == 'Polygon' else []
            rings = []
            for poly in polys:
                ring = [tuple(p) for p in poly[0]] if poly else []
                if ring and len(ring[0]) == 3 and abs(ring[0][0]) < 180:   # Grad statt Meter: zurück nach LV95
                    ring = [(*wgs84_to_lv95(p[1], p[0]), p[2]) for p in ring]
                if len(ring) > 1 and ring[0] == ring[-1]:
                    ring.pop()
                if len(ring) >= 3 and len(ring[0]) == 3:
                    rings.append(ring)
            if rings:
                props = feature.get('properties') or {}
                yield list(classify(rings)), props.get('GELAENDEPUNKT')


def read_gml(path):
    """CityGML-Kachel: ein Haus nach dem anderen lesen, damit wenig Speicher gebraucht wird."""
    for _, el in ET.iterparse(path):
        if el.tag == BLDG + 'Building':
            yield list(building_rings(el)), attribute(el, 'GELAENDEPUNKT')
            el.clear()


def attribute(b, name):
    for a in b.iter():
        if a.tag in (GEN + 'doubleAttribute', GEN + 'stringAttribute') and a.get('name') == name:
            return a.find(GEN + 'value').text
    return None


# ---------- Ein Haus umrechnen ----------
def convert_building(rings, terrain, anchor_of, rotate):
    if not rings:
        return None
    allpts = [p for _, r in rings for p in r]
    ce = sum(p[0] for p in allpts) / len(allpts)    # Mitte des Hauses in LV95
    cn = sum(p[1] for p in allpts) / len(allpts)
    ax, az = anchor_of(ce, cn)                      # ... und auf unserer Karte
    if CLIP and not (-20 < ax < KARTE_SIZE[0] + 20 and -20 < az < KARTE_SIZE[1] + 20):
        return None                                   # liegt nicht auf unserer Karte
    # Unser Spiel ist flach: das Haus wird so hingestellt, dass sein Boden auf y = 0 liegt.
    grounds = [r for kind, r in rings if kind == 'boden']
    base = min(p[2] for r in grounds for p in r) if grounds else float(terrain) if terrain else min(p[2] for p in allpts)
    top_of_ground = max(p[2] for r in grounds for p in r) if grounds else base
    verts, lookup = [], {}

    def vid(p):
        x, z = rotate(p[0] - ce, p[1] - cn)           # nur drehen: die Meter bleiben exakt
        y = 0.0 if p[2] <= top_of_ground + 0.01 else p[2] - base   # Wandfuss am Hang auf den Boden
        key = (round(x * 100), round(y * 100), round(z * 100))
        if key not in lookup:
            lookup[key] = len(verts) // 3
            verts.extend(key)
        return lookup[key]

    def tris_of(kind):
        out = []
        for k, r in rings:
            n = normal(r) if k == kind else None
            if n is None:
                continue
            for t in triangulate(r, n):
                i, j, l = vid(r[t[0]]), vid(r[t[1]]), vid(r[t[2]])
                if len({i, j, l}) == 3:
                    out.extend((i, j, l))
        return out

    roof_tris, wall_tris = tris_of('dach'), tris_of('wand')
    footprints = []
    for loop in outline([[rotate(p[0] - ce, p[1] - cn) for p in r] for r in grounds]):
        footprints.append([round(c, 2) for p in loop for c in p])   # Grundriss in Metern
    height = round(max(p[2] for p in allpts) - base, 2)
    return [round(ax, 2), round(az, 2), height, footprints, verts, roof_tris, wall_tris]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('gml', nargs='+')
    ap.add_argument('-o', '--out', default='assets/gebaeude.js')
    ap.add_argument('--alles', action='store_true', help='Häuser ausserhalb der Karte nicht wegwerfen (zum Testen)')
    args = ap.parse_args()
    global CLIP
    CLIP = not args.alles

    e0, n0, cx, cz, angle, err = find_local_origin()
    ca, sa = math.cos(angle), math.sin(angle)
    print(f'Kartenmitte LV95 E={e0:.2f} N={n0:.2f} = Karte x={cx:.2f} z={cz:.2f}, Drehung {math.degrees(angle):.3f} Grad')

    def anchor_of(e, n):
        """Mitte eines Hauses: genau dorthin, wo OpenStreetMap das Haus hat."""
        return karte_from_wgs84(*lv95_to_wgs84(e, n))

    def rotate(de, dn):
        """Ecke relativ zur Hausmitte: Osten bleibt x, Norden wird -z, dazu die kleine Drehung."""
        dz = -dn
        return ca * de - sa * dz, sa * de + ca * dz

    buildings = []
    for path in args.gml:
        count = 0
        if '.geojson' in path:
            houses = read_geojson(path)
        else:
            houses = read_gml(path)
        for rings, terrain in houses:
            b = convert_building(rings, terrain, anchor_of, rotate)
            if b:
                buildings.append(b)
                count += 1
        print(f'{path}: {count} Häuser auf der Karte')

    buildings.sort(key=lambda b: (b[1], b[0]))
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write('// Echte 3D-Häuser für Horse World, umgerechnet mit tools/swisstopo_to_game.py.\n')
        f.write('// Quelle: swissBUILDINGS3D 3.0 © swisstopo (Open Government Data, freie Nutzung mit Quellenangabe).\n')
        f.write('// Ein Haus = [x, z, Höhe, Grundrisse, Ecken in cm (x, y, z relativ zu x/z), Dach-Dreiecke, Wand-Dreiecke].\n')
        f.write('const GEBAEUDE = ')
        json.dump(buildings, f, separators=(',', ':'))
        f.write(';\n')
    tris = sum(len(b[5]) + len(b[6]) for b in buildings) // 3
    print(f'{len(buildings)} Häuser, {tris} Dreiecke -> {args.out}')


if __name__ == '__main__':
    main()
