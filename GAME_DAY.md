# Game Day Guide

Goal: make a real, playable game together and have fun. Claude handles the technical stuff. Your job is the **ideas**.

---

## Part 1: The plan (focus on the fun)

### Step 1: Dream it up (10-15 min)
Open `GAME_IDEA.md` and answer the questions together. Short and silly answers are best.
Tips:
- Pick **one simple goal** (collect stuff, survive, escape). Extra features come later.
- Pick **one weird thing** that makes the game yours (the enemies are broccoli, the hero is a dinosaur, gravity flips every 10 seconds).
- Don't worry if it sounds too big. Claude builds a small version first.

### Step 2: Build the first version (about 5 min of waiting)
Tell Claude: **"Build the game from GAME_IDEA.md"**.
Claude writes the game, tests it, and publishes it. Meanwhile, sketch the hero and enemies on paper.

### Step 3: Play it (10 min)
Everyone plays. Keep a list of what you notice:
- What's fun? (Keep it!)
- What's annoying or too hard / too easy?
- What's missing?

### Step 4: Improve it, one change at a time (the main loop)
Repeat as long as it's fun:
1. The kid picks **one** change.
2. Claude makes it (usually 1-3 minutes).
3. Reload the page and play.
4. Keep it or say "undo that".

One change at a time means you can see exactly what each idea did, and a bad idea is easy to undo.

### Good change requests (copy these)
| Type | Examples |
|---|---|
| Difficulty | "Make enemies faster after every 10 points." "Give me 3 lives." |
| Looks | "Change the hero to a ninja." "Make the background a sunset." |
| Power-ups | "Add a star that makes me invincible for 5 seconds." |
| Juice (feels great) | "Add screen shake when I get hit." "Add confetti when I score." |
| Sound | "Add a funny sound when I collect something." |
| Big ideas | "Add a boss every 50 points." "Add a second player." "Add levels." |

### Stuck for ideas?
- "What would make this game *hilarious*?"
- "What's the hardest thing about the game? Make it even harder, or make it a power-up."
- "What would a boss look like?"

### Try it yourself!
Open `index.html` and find the `SETTINGS` block at the top. Change a number (like `speed: 320` to `speed: 800`), save, reload. That's real programming, and it's safe: the worst case is you set it back.

### Finishing the day
- Give the game a name and a high-score challenge for friends and family.
- Send the link: `https://schillingt.github.io/play-zone/`

---

## Part 2: What's happening technically (the 2-minute version)

You don't need to understand this to have fun, but here's the big picture.

```
 Your idea  ->  Claude writes code  ->  Saved on GitHub  ->  Published online  ->  You play it
 (words)        (index.html)            (the "repo")         (GitHub Pages)         (any browser)
```

1. **The idea.** You describe the game in plain words. Claude turns those words into code.
2. **The code.** The whole game is one file, `index.html`. It uses JavaScript (the programming language of web pages) and a *canvas* (a blank rectangle the code draws on). Characters are emojis, so no drawing is needed.
3. **The game loop.** Every game does the same thing about 60 times per second: *read the keys, move things, check for hits, redraw the screen*. That's how it feels like things are moving.
4. **The settings.** Numbers like speed and lives live in one block at the top, so you can tweak the game without understanding all the code.
5. **The repo.** A repository ("repo") is a project folder on GitHub that remembers every version. Each change we make is saved as a *commit*, like a save point you can go back to.
6. **Publishing.** When a change lands on the `main` branch, GitHub automatically copies `index.html` to a public web address (GitHub Pages). It takes about a minute. That's why you reload to see changes.
7. **Testing.** Before saving a change, Claude opens the game in an invisible browser, presses keys, and checks for errors, like a robot player.

### Words you might hear
| Word | Meaning |
|---|---|
| **Code** | Instructions the computer follows |
| **Bug** | A mistake in the code (the game does something unintended) |
| **Commit** | A save point |
| **Repo** | The project folder on GitHub |
| **Branch** | A separate copy for trying things; `main` is the official one |
| **Deploy** | Publishing the new version online |
| **Sprite** | A character or object in the game |
| **Game loop** | The "read, move, check, draw" cycle running over and over |

---

## Part 3: Checklist before the day

- [ ] Open `https://schillingt.github.io/play-zone/` and check the placeholder dinosaur moves
- [ ] Laptop charged, with a browser and internet
- [ ] Paper and pens for sketching
- [ ] `GAME_IDEA.md` printed or open on screen
- [ ] Optional: a big screen or TV so everyone can watch
- [ ] Decide who gets the first turn at the keyboard, then take turns
