---
name: unslop
description: Rewrite text so it reads like a person wrote it. Use when the user says "unslop", or asks to clean up, tighten, or de-fluff plans, docs, README files, UI texts or commit messages. Works for German and English.
---

# Unslop

Remove filler and AI-sounding patterns from text. Keep the facts. Keep the language of the text (German stays German).

## Rules

1. **Cut filler.** Delete openers, closers and announcements: "In diesem Dokument...", "Zusammenfassend...", "It's worth noting that...".
2. **Say the specific thing.** Replace vague words with a number, a name or an example. "Viele Orte" becomes "Zytturm, Zugersee, Zugerberg".
3. **No hype words.** Drop: spannend, einzigartig, nahtlos, ganzheitlich, revolutionär, tauche ein, entdecke, seamless, powerful, unlock, journey, delve.
4. **Short sentences.** One idea each. Active voice. Present tense where it fits.
5. **No stacked patterns.** Avoid "nicht nur..., sondern auch...", rule-of-three lists with no content, and rhetorical questions that the text answers right away.
6. **No empty praise or hedging.** Remove "sehr wichtig", "grundsätzlich", "eigentlich", "quite", "really", "just".
7. **Use plain lists and tables only when the content is a list or a table.** Do not turn prose into bullets for looks.
8. **No decoration.** Drop emojis, bold and headings that add no information. Exception: emojis that are part of the game (hero, items, UI).
9. **Match the reader.** For this project the reader is a 12-14 year old and a parent. Plain words. No jargon without a one-line explanation.
10. **Keep what is specific.** Names, numbers, commands, file paths and quotes stay unchanged.

## Process

1. Read the text once. Mark filler, hype and vague words.
2. Rewrite. Do not add new facts. Do not remove facts.
3. Compare: the new text should be clearly shorter (aim for 15-30% less) and say the same.
4. Reply with the cleaned text. If you changed a lot, add one line on what you cut.

## Check before you finish

- Could a sentence be deleted without losing information? Delete it.
- Is there a number or a name where the text said "many" or "various"? Put it in.
- Does it still sound like the person who asked for it, not like a brochure?
