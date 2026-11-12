# Plan: Horse World (Switzerland)

Titel: **Horse World (Switzerland)**. Die beiden Spielmodi heissen »Pferde-Kurier« und »Entlaufene Fohlen«.

## Die Idee in drei Sätzen

Du reitest als Pferde-Kurier durch Zug und lieferst Pakete aus, bevor die Zeit abläuft. Dein Pferd hat Hunger und Laune: Du fütterst und streichelst es. Später kommt ein zweiter Modus dazu: Zehn Fohlen sind ausgebüxt, und du bringst sie zurück in den Stall. Die Welt ist eine offene Karte von Zug mit Altstadt, Zytturm, Bahnhof, Zugersee und Zugerberg.

## Was das Spiel ist

- **Ansicht von oben**, wie ein Stadtplan. Du reitest frei in alle Richtungen.
- **Eine Datei**: alles steht in `index.html`, ohne Zusatzprogramme.
- **Nur Tastatur.** Pfeile oder WASD.
- **Emoji und einfache Formen** statt Bilddateien. Alle Geräusche kommen aus WebAudio.
- **Alles auf Deutsch**: Startbildschirm, Anzeigen, Texte im Spiel.
- **Kinderfreundlich.** Hindernisse sind Enten, Pfützen und Marktstände. Es gibt keine Kämpfe.

## Steuerung (Vorschlag)

| Taste | Aktion |
|---|---|
| `W` `A` `S` `D` / Pfeile | Reiten |
| `Leertaste` | Galopp (schneller, die Ausdauer sinkt) |
| `E` | Paket aufnehmen oder abgeben, Fohlen einfangen |
| `F` | Pferd füttern (Karotte oder Apfel) |
| `G` | Pferd streicheln (gedrückt halten, das Pferd steht still) |
| `Enter` | Spiel starten |
| `R` | Neustart |

## Dein Pferd: füttern und streicheln

Das Pferd hat zwei Anzeigen oben links. Sie gelten in beiden Modi.

| Anzeige | Was sie macht |
|---|---|
| 🥕 **Hunger** | Sinkt langsam. Bei leerem Balken kannst du nicht galoppieren und reitest langsamer. `F` füttert: eine Karotte oder ein Apfel füllt den Balken. |
| ❤️ **Laune** | Sinkt, wenn du gegen Enten, Pfützen und Marktstände rennst. `G` streicheln füllt sie wieder auf, mit Herzchen und Wiehern. Gute Laune gibt mehr Ausdauer im Galopp. |

**Futter:** Du hast einen Vorrat (am Anfang 3). Nachschub gibt es am Futtertrog im Stall, an Apfelbäumen am Zugerberg und an Marktständen in der Altstadt.

## Modus 1: Pferde-Kurier (wird zuerst gebaut)

**Ablauf:** Ein Auftrag erscheint, zum Beispiel »Pizza vom Stall zum Bahnhof«. Du holst das Paket ab, reitest zum Ziel und gibst es ab. Ein Pfeil am Bildschirmrand zeigt dir die Richtung. Dann kommt der nächste Auftrag.

| Was | Regel |
|---|---|
| **Punkte** | 100 pro Lieferung, dazu 1 Punkt für jede Sekunde, die übrig bleibt. |
| **Zeit** | Jeder Auftrag hat ein Zeitlimit. Eine Lieferung gibt Zusatzzeit auf die Gesamtuhr. |
| **Sieg** | 10 Lieferungen geschafft. |
| **Verlieren** | Die Gesamtuhr läuft ab. |
| **Hindernisse** | Enten bremsen dich, Pfützen machen dich langsam, Marktstände blockieren den Weg. |
| **Schwieriger werden** | Die Aufträge werden weiter entfernt, die Zeitlimits kürzer. |

### Die Pakete

| Paket | Von | Nach |
|---|---|---|
| 🍕 Pizza | Altstadt | Seepromenade |
| 📦 Paket | Bahnhof | Zytturm |
| ✉️ Post | Zytturm | Zugerberg |
| 🍰 Kirschtorte | Zugerberg | Bahnhof |

Die Liste ist ein Startvorschlag. Ihr denkt euch weitere Aufträge aus.

## Modus 2: Entlaufene Fohlen (kommt danach)

**Ablauf:** Zehn Fohlen 🐴 sind aus dem Stall ausgebüxt. Du findest sie in Zug, fängst sie ein und bringst sie zurück.

| Was | Regel |
|---|---|
| **Verstecken** | Die Fohlen stehen an bekannten Orten, zum Beispiel am See, in der Altstadt oder am Bahnhof. |
| **Einfangen** | Reite langsam heran und drücke `E`. Wenn du im Galopp kommst, rennt das Fohlen weg. Mit einer Karotte (`F`) und Streicheln (`G`) beruhigst du ein scheues Fohlen. |
| **Zurückbringen** | Das gefangene Fohlen folgt dir bis zum Stall. |
| **Sieg** | Alle 10 Fohlen sind im Stall. |
| **Verlieren** | Die Sonne geht unter, bevor alle zurück sind. |
| **Punkte** | 50 pro Fohlen, dazu ein Bonus für die übrige Zeit. |

Auf dem Startbildschirm wählst du den Modus mit `1` (Kurier) oder `2` (Fohlen).

## Die Karte von Zug

Eine Karte, die in beiden Modi gebraucht wird:

| Ort | Aussehen auf der Karte |
|---|---|
| **Stall** | Start und Ziel, mit Futtertrog. Blaues Dach mit weisser Fahne (die Zuger Farben). |
| **Altstadt** | Gassen zwischen Häusern, Marktstände. |
| **Zytturm** | Turm am Rand der Altstadt, immer gut zu sehen. |
| **Seepromenade** | Weg am Wasser, Bänke, Möwen 🐦. |
| **Zugersee** | Wasser. Das Pferd kann nicht schwimmen. Ein Schiff 🚢 fährt darüber. |
| **Bahnhof** | Gleise und ein kleiner Zug 🚆. |
| **Zugerberg** | Hügel mit Wiese und Bäumen. Bergauf bist du langsamer. |

Unten rechts zeigt eine kleine Übersichtskarte, wo du bist.

## Arbeitsprozess: die Phasen

Jede App entsteht in denselben sieben Phasen. Phase 1 bis 3 machen wir am Anfang. Phase 4 bis 7 wiederholen sich für jeden Schritt unten.

| # | Phase | Was passiert | Wer | Das kommt heraus | Fertig, wenn... |
|---|---|---|---|---|---|
| 1 | **Idee** | Fragen in `GAME_IDEA.md` beantworten, Spielart und eine verrückte Zutat wählen | Ihr | Ein paar Sätze | Ihr erklärt die Idee in drei Sätzen |
| 2 | **Plan** | Idee in kleine Schritte teilen, pro Schritt ein »Fertig, wenn...« | Ihr und Claude | Dieser Plan | Jeder Schritt ist klein und prüfbar |
| 3 | **Design** | Skizzen auf Papier (Karte, Pferd, Bildschirm), Farben, deutsche Texte, Tasten | Ihr zeichnet, Claude fragt nach | Skizzen, Farbliste, Textliste | Claude kann danach bauen, ohne zu raten |
| 4 | **Bauen** | Ein Schritt nach dem anderen in `index.html` umsetzen | Claude | Neue Version von `index.html` | Das »Fertig, wenn...« des Schritts stimmt |
| 5 | **Testen** | Roboter-Spieler prüft auf Fehler, dann spielt ihr | Roboter, dann ihr | Liste: gut, kaputt, Wünsche | Keine Fehler, ihr sagt »behalten« |
| 6 | **Veröffentlichen** | Commit, Push, nach `main`, GitHub stellt die Seite online | Claude, ihr gebt das Okay | Neue Version unter dem Link | Die Seite online zeigt die Änderung |
| 7 | **Verbessern** | Freunde spielen lassen, beobachten, neue Ideen sammeln | Alle | Neue Ideenliste, erweiterter Plan | Nie ganz. Pause ist auch fertig genug |

**Zurückgehen ist erlaubt.** Fällt beim Testen auf, dass etwas nicht zusammenpasst, gehen wir zum Design oder zum Plan zurück.

**Wo wir stehen:** Idee und Plan sind fertig. Wir sind in Phase 3, dem Design. Danach beginnt Phase 4 mit Schritt 1.

## Die Schritte

Jeder Schritt ist **eine Änderung und ein Commit**. Nach jedem Schritt laden wir die Seite neu und spielen kurz. Wenn es nicht passt, machen wir den Schritt rückgängig.

### Teil A: Welt und Pferd (Claude baut Schritte 1 bis 3 in einem Rutsch)

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 1 | **Startbildschirm** auf Deutsch | Titel erscheint, `Enter` startet, `R` startet neu. |
| 2 | **Karte von Zug zeichnen** | See, Altstadt, Bahnhof, Zugerberg und Stall sind zu sehen. Die Kamera folgt dem Pferd. |
| 3 | **Pferd reiten** | Das Pferd reitet in alle Richtungen, bleibt vor dem See und vor Häusern stehen. `Leertaste` macht es schneller. |

### Teil B: Modus Kurier (erste spielbare Version)

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 4 | **Aufträge und Pfeil** | Ein Auftrag erscheint, der Pfeil zeigt zum Ziel. `E` nimmt das Paket auf und gibt es ab. |
| 5 | **Uhr und Punkte** | Oben stehen Zeit und Punkte. Lieferungen geben Punkte und Zusatzzeit. |
| 6 | **Sieg und Verlieren** | Nach 10 Lieferungen erscheint »Geschafft!«. Läuft die Uhr ab, erscheint »Zeit um!«. Beide zeigen die Punktzahl. |
| 7 | **Hindernisse** | Enten, Pfützen und Marktstände stehen im Weg. |
| 8 | **Übersichtskarte** | Unten rechts zeigt die Karte Pferd und Ziel. |

### Teil C: Pferd füttern und streicheln

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 9 | **Hunger und Futter** | Der Hunger-Balken sinkt. `F` füttert, der Vorrat sinkt. Bei leerem Balken geht kein Galopp. Futtertrog und Apfelbäume geben Nachschub. |
| 10 | **Laune und Streicheln** | Der Laune-Balken sinkt bei Zusammenstössen. `G` streicheln lässt Herzchen aufsteigen und füllt den Balken. |

### Teil D: Es fühlt sich gut an

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 11 | **Geräusche** | Hufe, Wiehern, Kauen, Abgeben, Zeit wird knapp. Alles aus WebAudio. |
| 12 | **Staub und Konfetti** | Staubwolke beim Galopp, Konfetti bei der Lieferung. |
| 13 | **Highscore speichern** | Die beste Punktzahl bleibt nach dem Neuladen erhalten. |

### Teil E: Modus Fohlen

| # | Schritt | Fertig, wenn... |
|---|---|---|
| 14 | **Modus-Auswahl** | Auf dem Startbildschirm wählt `1` oder `2` den Modus. |
| 15 | **Fohlen verstecken** | 10 Fohlen stehen an festen Orten in Zug. Der Zähler zeigt `Fohlen: 3/10`. |
| 16 | **Einfangen und Heimbringen** | Langsam heranreiten und `E` fängt ein Fohlen. Es folgt dir zum Stall. |
| 17 | **Wegrennen und Beruhigen** | Im Galopp rennen Fohlen weg. Karotte und Streicheln beruhigen sie. |
| 18 | **Sonnenuntergang** | Der Himmel wird dunkler. Ist die Sonne weg, erscheint »Zu spät!«. Alle Fohlen im Stall geben »Geschafft!«. |

### Teil F: Eure Ideen (Reihenfolge frei)

- Seemonster im Zugersee als letzte Mission
- Detektiv-Mission: Wer hat die Kirschtorte gestohlen?
- Pferd striegeln und Hufe putzen
- Schnelleres Pferd als Belohnung
- Rennen vom See auf den Zugerberg
- Zweiter Spieler auf derselben Tastatur
- Geheimer Cheat-Code
- Ein eigenes Bild als Figur

## Einstellungen zum Selbständern

Alle Zahlen stehen im Block `SETTINGS` oben in `index.html`. Geplant:

| Name | Bedeutung |
|---|---|
| `walkSpeed` | Reittempo |
| `gallopSpeed` | Tempo im Galopp |
| `staminaSeconds` | Wie lange der Galopp hält |
| `startTimeSeconds` | Gesamtzeit am Anfang (Kurier) |
| `bonusTimeSeconds` | Zusatzzeit pro Lieferung |
| `deliveriesToWin` | Lieferungen bis zum Sieg |
| `foalCount` | Anzahl Fohlen |
| `hungerSeconds` | Zeit, bis der Hunger-Balken leer ist |
| `startFood` | Futter-Vorrat am Anfang |
| `petBoost` | Wie viel Laune ein Streicheln bringt |
| `dayLengthSeconds` | Zeit bis zum Sonnenuntergang (Fohlen) |
| `pointsPerDelivery` | Punkte pro Lieferung |
| `horse`, `foal`, Farben | Emoji und Farben |

## Was schiefgehen kann

- **Zu viel auf einmal.** Deshalb nur eine Änderung pro Schritt.
- **Zu schwer oder zu leicht.** Dafür gibt es `SETTINGS`. Zahl ändern, neu laden, ausprobieren.
- **Pferd bleibt an Ecken hängen.** Wir testen jeden Ort auf der Karte mit einem Roboter-Spieler.

## Fragen an euch, bevor es losgeht

1. Wie heisst das Pferd, und welche Farbe hat es?
2. Welche weiteren Orte in Zug gehören unbedingt auf die Karte?
3. Welche Pakete soll der Kurier ausliefern?
4. Allein spielen oder zu zweit?
