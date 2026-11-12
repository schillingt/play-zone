# play-zone

A just-for-fun browser game built live with a kid (age 12-14) on a laptop. The goal is fast, visible results: one-shot a playable game, then improve it in small steps.

## Rules

- The whole game lives in `index.html`: plain JavaScript and Canvas, no build step, no npm dependencies, no CDN scripts. Images or sounds, if any, go in `assets/`.
- Keyboard controls (arrows and WASD). Touch support is not needed.
- Graphics are emoji or simple canvas shapes; sounds are generated with WebAudio. Do not add asset files unless asked.
- Keep the `SETTINGS` block at the top of the script. Every tunable number (speed, gravity, lives, spawn rate, colours, emoji) goes there with a short comment, so the kid can change it by hand.
- Code should be readable by a curious 13-year-old: clear names, short functions, a one-line comment per section.
- Content stays kid-friendly: cartoon-level action only.
- The game must always have a start screen, a way to lose or win, a score, and a restart key.

## Workflow

- One change request = one small commit, so a bad idea is easy to undo.
- Before committing, load `index.html` in headless Chromium (Playwright is preinstalled), check for console errors, and simulate a few key presses.
- Pushing to `main` deploys to GitHub Pages via `.github/workflows/pages.yml`.
- The idea sheet for the first one-shot is `GAME_IDEA.md`.
