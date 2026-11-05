# Design system — Academic English

## Design intent

Premium minimalist EdTech, optimised for calm daily focus rather than gamified visual clutter. It uses a neutral surface, quiet green accent, generous line-height and a type hierarchy that prioritises the learning content. Desktop navigation is a persistent left sidebar; mobile navigation is an accessible bottom tab bar with a separate drawer for additional tools.

## Design tokens and typography

The canonical tokens are defined in `src/styles.css` and include backgrounds, elevated surfaces, ink/muted text, state colours, borders, shadows, focus indicator, radii and spacing. Colour modes are controlled by `html[data-theme="system|light|dark"]`, with `prefers-color-scheme` used for the system setting. The interface uses the self-hosted Manrope variable font with a system fallback. The font is included in the offline cache, so it does not require an external font service. Russian Cyrillic and English Latin script are both supported.

Major headings use fluid type; academic reading text is larger with generous leading. Controls have a minimum recommended interactive height of about 44–48 CSS pixels; small toolbar-only controls retain accessible labels.

## Components

- `Sidebar`, `Topbar`, `MobileNav`: consistent navigation hierarchy.
- `Hero`, `StatCard`, `ContinueCard`, `ModuleTile`: course dashboard.
- `LessonStepper`, `LessonSection`, `LessonNav`: single-focus step-by-step study.
- `VocabularyCard`, `ReadingWord`, `LookupCard`: lexical discovery and saving.
- `ExerciseChoice`, `FillInput`, `MatchingRows`, `SentenceBuilder`, `SelfReview`: practice engine.
- `AudioBox`, `DialogueBubble`, `RecorderStatus`: listening and role-play.
- `Feedback`, `Notice`, `Toast`, `Modal`: explicit status and safe confirmations.
- `ThemeToggle`, `TextScale`: personal preferences.

## Accessibility considerations

Real HTML buttons, radio inputs, select fields and textareas are used, so keyboard interactions are not artificially simulated. Focus styles remain visible. Feedback has text as well as colour. Skip-to-content and status roles are present. Layout supports reduced-motion settings. The mobile lesson action bar becomes non-sticky while answer fields have focus to reduce keyboard obstruction, and mobile bottom navigation includes safe-area padding.

Accessibility has been designed for WCAG 2.2 AA principles; **the project has not undergone a formal independent WCAG certification audit**. See `QA_REPORT.md` for actual tests.

## Responsive screens reviewed

- 375×812: compact phone
- 390×844: contemporary phone
- 768×1024: tablet
- 1280×800: laptop
- 1440×900: large desktop

All five sizes passed the measured horizontal overflow test in Chromium in the browser UI smoke test. This does not guarantee identical text rendering or voice API support in every browser.

## Navigation and progress principles

A learner can jump to any course day, and within a day can revisit unlocked steps. Progress is always recorded locally, rather than hidden behind a sign-up wall. The lesson action bar keeps the next learning action visible; it does not prevent reading content. XP and streaks are displayed as supportive feedback, but do not replace actual learning checks.
