# Academic English — 30-Day Learning Studio

**A complete, dependency-free, bilingual (RU/EN), offline-first browser course for international university Academic Support staff (approx. B1 → B1+ / toward B2).**

This is a working educational website with 30 authored lessons. It is not an AI tutor, a CEFR certification test, or a generic blank dashboard. Its exercises and quizzes are scored with transparent, deterministic rules; original speaking/writing is evaluated via **explicit self-review rubrics** rather than fabricated machine scores.

## Quick start (local computer)

**Requirements:** Node.js 18 or newer. Python 3 to regenerate curriculum and rebuild from authoring scripts. You do **not** need a paid API, account, database, internet connection, or `npm install` dependencies.

1. Unzip `Academic-English-30-Day-Course.zip`.
2. Open a terminal in the `Academic-English-30-Day-Course` folder.
3. Run `npm run preview` to start the **included production build**. A local server appears at **http://127.0.0.1:4173**.
4. Open that address in Chrome, Edge or another modern browser.

To develop against the source files, run `npm run dev`. To generate a fresh production build, run `npm run build` (requires Python 3).

If Node.js is unavailable, you may use any static HTTP server from the project root, for example `python3 -m http.server 4173`. Open `http://127.0.0.1:4173/`.

Do **not** rely on double-clicking `index.html` through `file://`: Web Speech, service workers, and local storage can have inconsistent permissions on file URLs.

## What is included?

- **30 authored days** across five Academic Support modules; each lesson has four specific outcomes, ten lexical items, six useful phrases, an original reading (201–231 English words), an eight-or-more-turn professional dialogue, grammar in context, reading/listening checks, practice tasks, a speaking scenario and written workplace challenge.
- **Exercise engine:** multiple choice, text gaps, matching, ordering words, error correction, situational decisions, and self-checked translation.
- **Vocabulary Trainer:** 300 lexical entries (289 distinct English expressions), 180 functional phrases, flashcard reveal, both directions, personalised spaced review (four recall ratings), saved words and difficulty filter.
- **Listening Studio:** 30 dialogue scripts rendered through browser speech synthesis with play/stop controls, text transcript, comprehension exercises and playback speed settings.
- **Conversation Lab:** guided / standard / independent role-play. The learner practices as an Academic Support Officer or as the learner in Day 30; dialogue models come from authored lesson scripts.
- **Microphone practice:** browser-native recording and playback using MediaRecorder (where available), optional SpeechRecognition transcription (where available), manual text alternative, model answer and self-review rubric.
- **Reading interaction:** click words and known multiword terms for an offline glossary lookup; missing glossary entries are disclosed rather than invented.
- **Assessment:** 17-question initial diagnostic, four short module checkpoints, 18-question final quiz, separate speaking and writing portfolio tasks, transparent strengths and weaknesses.
- **Academic resources:** 15 editable email templates, searchable phrasebook, lesson notes and mistake review.
- **Progress & preferences:** automatic local save, next lesson, achievements, XP, streaks for real activity, dark/light/system mode, larger font, JSON backup/import/reset.
- **Responsive design:** desktop and mobile navigation, safe-area support, keyboard-accessible controls, reduced-motion mode.

## Daily study pattern (recommended ~70 min)

| Session | Typical time |
| --- | ---: |
| Recall and spaced review | 10 min |
| Vocabulary and professional phrases | 10 min |
| Reading/listening | 10 min |
| Grammar in context | 10 min |
| Spoken role-play | 15 min |
| Applied workplace challenge | 10 min |
| Summary / reflection | 5 min |

This is a guide, not a timer. The learner may spend longer on speaking, listen several times, and replay earlier modules. Time spent is **not fabricated** in analytics.

## How to use the course

Start with the five-screen onboarding, then optionally take the diagnostic. The **Learning Path** shows all 30 days; lessons may be opened out of sequence for quick reference. Each lesson has 11 steps. Vocabulary becomes eligible for spaced review after completing the Vocabulary step; objective practice stages require attempts before advancing. Speaking and writing require meaningful input and explicit comparison with the sample before marking them practised. Incorrect answers can be retried.

Use **Vocabulary → Review** for spaced flashcards. Ratings schedule the next recall (first successful reviews in 1–7 days, longer later; a difficult card returns sooner). Use **Settings → Export progress** periodically, especially before clearing browser data or changing devices. To transfer progress to another device, import that JSON there. No cloud synchronisation exists.

## Accessibility & navigation

The interface is built with semantic controls, live status messages, visible keyboard focus, appropriate text contrast, and button targets suited to touch. Use Tab and Enter/Space to navigate. Esc closes open menus/dialogs. There is a skip-to-content link. Text scaling is available in Settings. Microphone and audio are never required to read lessons or answer text questions.

## Technical structure

```text
Academic-English-30-Day-Course/
├── index.html                # Application entry point
├── sw.js                     # Static offline cache for HTTP(S) deployments
├── src/
│   ├── app.js                # Routes, components, lesson screens, UI events
│   ├── core.js               # Deterministic learning logic and storage checks
│   └── styles.css            # Design system / responsive CSS
├── content/
│   ├── curriculum.json       # Structured canonical published course data
│   └── curriculum.js         # Same data for static script loading
├── scripts/
│   ├── part1.py … part4.py   # Human-authored lesson content
│   ├── objectives.py         # 30 × 4 specific learning goals
│   ├── authoring.py          # Authoring helpers
│   ├── content_tools.py      # Content schema creation
│   ├── build_content.py      # Regenerates JSON / JS curriculum
│   ├── validate_content.py   # Content integrity validator
│   ├── build.cjs             # Copies production-ready static files
│   └── serve.cjs             # Local static HTTP server
├── tests/
│   ├── core.test.cjs         # Unit tests for business logic
│   └── browser_smoke.py      # Browser UI integration walkthrough
├── dist/                     # Ready-to-run production static build
├── assets/favicon.svg
├── CURRICULUM.md
├── METHODOLOGY.md
├── DESIGN_SYSTEM.md
├── QA_REPORT.md
└── LIMITATIONS.md
```

There are **zero npm runtime dependencies**. `npm install` is unnecessary. Plain JavaScript keeps the application small and source files editable without a proprietary platform.

## Commands

| Command | Purpose |
| --- | --- |
| `npm run preview` | Serve ready-made `dist/` on localhost:4173 |
| `npm run dev` | Serve source files on localhost:4173 |
| `npm run build` | Recreate content and `dist/` (needs Python 3) |
| `npm run validate` | Check 30-day content data, IDs, counts and answer indices |
| `npm test` | Run 17 unit tests (Node.js test runner) |
| `python tests/browser_smoke.py` | Browser UI integration walkthrough; requires Python Playwright + Chromium |
| `python tests/browser_routes.py` | Check 47 application routes at phone and desktop widths |

## Modifying lesson content

Edit authoring material in `scripts/part1.py` to `part4.py` and detailed objectives in `scripts/objectives.py`; then run `npm run build && npm run validate && npm test`. Every day includes source-authored translations, dialogue turns, grammar, answer choices and explanations. Content remains separate from application logic.

## How results are calculated

- A machine-checked response is marked correct according to its published answer key or permitted normalised form.
- The mastery chart uses the **last attempt per exercise** and shows only categories with actual measured questions; an empty category shows `—`.
- The initial and final tests have **different** question selections. Their percentages concern only those specific selected-response items.
- Completing a self-reviewed spoken/written assignment is recorded as **practice completed**, never as a measured pronunciation or CEFR score.
- XP is awarded for unique successful exercise IDs, completed stages, lessons and flashcard reviews; repeated success on the same ID cannot be farmed repeatedly.

## Data and privacy

Progress is stored in browser `localStorage`. The app does not send progress, notes or recordings to a backend. Browser/OS speech recognition **may** depend on a third-party speech service: inspect browser privacy documentation before enabling it. MediaRecorder playback files are kept only in the current page session, are not exported, and are released when changed. `sw.js` caches only static course assets on supported same-origin HTTP(S) pages.

For candid details about speech quality, exact dictionary coverage, offline limits, and testing coverage, read [LIMITATIONS.md](LIMITATIONS.md) and [QA_REPORT.md](QA_REPORT.md).

**Scope:** The 30-day programme builds professional confidence through repeated workplace practice. It does not guarantee a full CEFR level increase in a month.
