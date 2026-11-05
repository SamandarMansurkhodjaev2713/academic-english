# Honest limitations and environment requirements

## Speech and audio

- **Text-to-speech (TTS):** All 30 dialogues have authored scripts and can be synthesised on demand via the browser Speech Synthesis API. **No prerecorded native-speaker audio files are bundled.** Voice quality, English voices, support for changing speed, initial playback restrictions and reliability depend on the installed browser and operating system. TTS does not represent a diversity of real speakers or accents.
- **Speech recognition:** Optional recognition uses browser-provided Web Speech APIs (if present). It is not available in all browsers and may use vendor cloud infrastructure. The course does not control the browser vendor's speech backend. It should not be used for confidential student records.
- **Recording:** Where the browser supports MediaRecorder and `getUserMedia`, the user can make a temporary voice recording and listen back to it. Microphone permission is required, and HTTPS or localhost is usually necessary. The recording is kept within the current page session (object URL), never uploaded by this application, and is not part of saved progress.
- **Pronunciation scoring:** No objective phonetic scores, accent analysis, or AI voice-coaching claims. Transcript recognition compares *words*, not the acoustic qualities of a learner's speech. Speaking is self-reviewed against a model and rubric.
- **Fallback:** Without voice APIs, all lessons, scripts, exercises, professional cases and written responses remain accessible. Written text can be entered instead of speaking to a microphone.

## Dictionaries and feedback

- Offline reading lookups cover the course's 300 lexical entries (289 distinct terms) and a small set of common words. **Not every inflected form or every possible English word has a verified translation.** The interface explicitly reports missing terms; it does not invent a translation. Multiword lexical entries are handled where they match the passage exactly.
- Multiple-choice, matching and sentence-order tasks are deterministically graded against authored answer keys. Fill-in blanks normalise case, punctuation and spaces, but do **not** perform a general semantic evaluation. Alternative grammatically valid open responses are reviewed against a model by the learner.
- Course content is institution-neutral. Academic terms and formal procedures vary among universities. Always verify actual policy, deadlines, contacts, consent requirements and approval authority.

## Assessment validity

- Placement is 17 sampled selected-response items, final assessment is 18 different sampled items; their percentage is **not** a CEFR certification result.
- Speaking and writing do not receive fabricated numerical grades. The final learner may link to independent Day 30 speech and writing tasks and use their rubrics. Comparisons of initial/final percentages are indicative only; question sets differ and can be practised.
- The user's B1 starting level is provided by the course brief and not independently validated.
- A 30-day course can improve job-specific communication but cannot guarantee B2 certification.

## Storage, sync, privacy

- **Local-only:** progress, attempts, daily streak, vocabulary intervals and notes live in the browser's localStorage. There is no server account, cross-device sync, external database or cloud backup.
- Export progress in JSON before clearing browser/site data. Import validates the expected save structure, yet any browser with local access to the exported JSON can read the progress.
- Browsers may apply private-mode limits, quota restrictions or other storage policies. A corrupted existing saved file is not overwritten automatically on load; a deliberate reset or import can replace it.
- External TTS or speech recognition may be processed by the browser/OS vendor. Do not read confidential personal or academic records aloud in unapproved cloud-enabled voice services.

## Offline use and installation

- The site contains no remote font, analytics, media CDN or API requirement.
- `dist/` contains an actual ready-built HTML/CSS/JS application; it must be served over a local static web server or hosted on HTTPS for consistent voice/storage/service-worker behaviour.
- The service worker caches the static application shell after a successful visit on supported same-origin HTTP(S) contexts; it does not work through `file://`.
- TTS availability while offline depends on local voice installation. Browser-dependent recognition may need network access.

## Testing coverage and residual risk

- Chrome/Chromium DOM/UI flows were exercised with inline test assets because direct localhost navigation was blocked by the sandbox's browser policy. Static HTTP responses and production build were independently verified, but an actual connected HTTP browser flow / service-worker offline install was **not** completed in this environment.
- Tests were **not** run in real iOS Safari, mobile Android Chrome, macOS Safari, Firefox or Edge. The CSS is responsive and uses modern platform APIs, but these browsers should be checked on deployment before institutional roll-out.
- The tests do not objectively validate all 300 translations, linguistic nuance of 30 articles or naturalness of every audio voice. A professional ESL/higher-education subject expert should review course content before high-stakes institutional use.
