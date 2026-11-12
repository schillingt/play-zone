# Plan: Pferde-Welt Zug

Arbeitstitel: **ZugCraft: Pferde-Welt** (den echten Namen findet ihr zusammen).

## Die Idee in drei Sätzen

Du läufst durch eine Welt aus Blöcken, wie in Minecraft. Du baust Blöcke ab, setzt sie wieder und reitest auf deinem Pferd. Die Welt ist Zug in der Schweiz: Zugersee, Zugerberg, Altstadt und Zytturm.

## Was das Spiel ist (und was nicht)

- **Seitenansicht in 2D**, nicht 3D. Das passt in eine einzige `index.html` ohne Zusatzprogramme. Es ist trotzdem ein Block-Spiel: Die Welt besteht aus Quadraten, die man abbauen und setzen kann.
- **Nur Tastatur.** Pfeile oder WASD zum Laufen, dazu ein paar Tasten fürs Bauen (siehe unten).
- **Emoji und einfache Formen** statt Bilddateien. Alle Geräusche kommen aus WebAudio.
- **Alles auf Deutsch**: Startbildschirm, Anzeigen, Texte im Spiel.
- **Kinderfreundlich.** Die Gegner sind Cartoon-Figuren. Wer getroffen wird, verliert ein Herz, mehr nicht.

## Spielablauf

| Was | Wie |
|---|---|
| **Ziel (Sieg)** | Sammle 5 Zuger Schätze und bring sie in deinen Stall. Dann hast du gewonnen. |
| **Verlieren** | Alle 3 Herzen sind weg. Herzen gehen verloren durch Gegner oder tiefe Stürze. |
| **Punkte** | Schätze, abgebaute Blöcke, Zeitbonus beim Sieg. |
| **Neustart** | Taste `R`. |
| **Startbildschirm** | Titel, Kurzanleitung, Taste `Enter` zum Starten. |

### Die 5 Zuger Schätze

1. 🍰 **Kirschtorte** (Zuger Spezialität, versteckt in der Altstadt)
2. 🍒 **Goldene Chriesi** (Kirschen, hoch oben im Baum am Zugerberg)
3. ⏰ **Zytturm-Uhr** (oben auf dem Zytturm)
4. ⚓ **Schiffsglocke** (auf dem Grund des Zugersees)
5. 🏔️ **Gipfelstein** (ganz oben, mit Blick Richtung Rigi)

### Steuerung (Vorschlag)

| Taste | Aktion |
|---|---|
| `A` `D` / `←` `→` | Laufen oder Reiten |
| `W` / `↑` / `Leertaste` | Springen |
| `E` | Block vor dir abbauen |
| `F` | Block vor dir setzen |
| `1` bis `6` | Blocksorte wählen |
| `H` | Aufs Pferd steigen oder absteigen |
| `R` | Neustart |

## Das Pferd

- 🐴 Name frei wählbar (Vorschlag: **Blitz**).
- Zu Fuss: normal schnell, normal hoch springen.
- Auf dem Pferd: doppelt so schnell, springt über 3 Blöcke hoch, kann seichtes Wasser durchqueren.
- Das Pferd ist nur im Spiel, wenn du es mit einem Apfel (🍎) rufst. Apfelbäume wachsen im Gelände.

## Die Welt: Zug

Von links nach rechts ist die Karte so aufgebaut:

1. **Zugerberg** (links): Wiese, Bäume, Kirschbäume, Höhle zum Graben.
2. **Altstadt** (Mitte links): Häuser aus Stein, enge Gassen, **Zytturm** zum Hochklettern.
3. **Seepromenade**: Pflaster, Bänke, Möwen 🐦.
4. **Zugersee** (Mitte rechts): Wasser mit Boden aus Sand. Ein Schiff 🚢 fährt darüber.
5. **Gegenüber vom See** (rechts): Hügel, Stall, Start der Berge.
6. **Hintergrund**: Rigi und Pilatus als blaue Silhouetten, Wolken, Sonne und Mond.

Farben: Blau und Weiss (die Zuger Farben) für Fahne und Stall.

### Blocksorten

| Nr. | Block | Besonderheit |
|---|---|---|
| 1 | 🟩 Gras | |
| 2 | 🟫 Erde | |
| 3 | ⬜ Stein | hart, braucht länger zum Abbauen |
| 4 | 🟨 Sand | |
| 5 | 🟦 Wasser | man kann es nicht abbauen, nur durchschwimmen |
| 6 | 🪵 Holz | zum Bauen von Stall und Brücken |

## Die Schritte

Jeder Schritt ist **eine Änderung und ein Commit**. Nach jedem Schritt laden wir die Seite neu und spielen kurz. Wenn es nicht passt, machen wir den Schritt rückgängig.

### Teil A: Erste spielbare Version (Claude baut Schritte 1 bis 5 in einem Rutsch)

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 1 | **Startbildschirm** auf Deutsch | Titel erscheint, `Enter` startet, `R` startet neu. |
| 2 | **Blockwelt zeichnen** | Himmel, Gras, Erde, Stein, Wasser sind als Raster sichtbar. Die Kamera folgt der Figur. |
| 3 | **Figur laufen und springen** | Die Figur steht auf Blöcken, fällt, springt und läuft nicht durch Wände. |
| 4 | **Abbauen und setzen** | `E` entfernt einen Block, `F` setzt einen. Unten zeigt eine Leiste die Blocksorte. |
| 5 | **Pferd** | `H` setzt dich aufs Pferd. Es ist schneller und springt höher. |

### Teil B: Die Welt wird zu Zug

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 6 | **Zugersee und Zugerberg** | Hügel links, See rechts, Sand am Ufer. |
| 7 | **Altstadt und Zytturm** | Häuser und ein Turm, auf den man klettern kann. |
| 8 | **Berge im Hintergrund** | Rigi und Pilatus als Silhouetten, Wolken ziehen. |

### Teil C: Ein Spiel wird daraus

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 9 | **Schätze sammeln** | 5 Schätze liegen in der Welt, der Zähler oben zeigt `Schätze: 2/5`. |
| 10 | **Gewinnen** | Mit 5 Schätzen im Stall erscheint »Gewonnen!« mit Punktzahl. |
| 11 | **Gegner und Herzen** | Cartoon-Gegner laufen herum. Drei Herzen. Bei null kommt »Verloren!«. |
| 12 | **Tag und Nacht** | Der Himmel wird dunkel, nachts gibt es mehr Gegner. |

### Teil D: Es fühlt sich gut an

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 13 | **Geräusche** | Abbauen, Setzen, Springen, Wiehern, Schatz gefunden. Alles aus WebAudio. |
| 14 | **Partikel und Wackeln** | Staub beim Abbauen, Konfetti beim Schatz, Bildschirm wackelt bei Treffer. |
| 15 | **Highscore speichern** | Die beste Punktzahl bleibt nach dem Neuladen erhalten. |

### Teil E: Eure Ideen (Reihenfolge frei)

- Zweites Pferd mit anderer Farbe
- Hufeisen als Power-Up (kurz unverwundbar)
- Fasnachts-Gegner (Zug hat eine bekannte Fasnacht)
- Zweiter Spieler auf derselben Tastatur
- Ein eigenes Bild als Figur
- Geheimer Cheat-Code
- Schloss bauen, das auf Punkte zählt

## Einstellungen zum Selbständern

Alle Zahlen stehen im Block `SETTINGS` oben in `index.html`. Geplant:

| Name | Bedeutung |
|---|---|
| `walkSpeed` | Lauftempo zu Fuss |
| `horseSpeed` | Tempo auf dem Pferd |
| `jumpHeight` | Sprunghöhe zu Fuss |
| `horseJumpHeight` | Sprunghöhe auf dem Pferd |
| `gravity` | Wie schnell man fällt |
| `startLives` | Anzahl Herzen am Anfang |
| `treasuresToWin` | Wie viele Schätze zum Sieg nötig sind |
| `enemySpawnRate` | Wie oft Gegner auftauchen |
| `dayLengthSeconds` | Dauer von Tag und Nacht |
| `hero`, `horse`, Farben | Emoji und Farben |

## Was schiefgehen kann

- **Grosse Welt wird langsam.** Wir zeichnen nur, was auf dem Bildschirm zu sehen ist.
- **Zu viel auf einmal.** Deshalb nur eine Änderung pro Schritt.
- **Zu schwer oder zu leicht.** Dafür gibt es `SETTINGS`. Zahl ändern, neu laden, ausprobieren.

## Fragen an euch, bevor es losgeht

1. Wie heisst das Spiel?
2. Wie heisst das Pferd, und welche Farbe hat es?
3. Welche Orte in Zug gehören unbedingt rein? (Eigene Orte zählen mehr als meine Liste.)
4. Soll es Gegner geben, und wie sehen sie aus?
5. Allein spielen oder zu zweit?
