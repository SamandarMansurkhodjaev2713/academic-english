# Engineering & content QA report

**Date:** 5 November 2026  
**Product:** Academic English 30-Day Learning Studio  
**Test environment:** Python 3.13.5; Node.js 22.16.0; Chromium (headless, automated, inline HTML/CSS/JS assets).  
**Release status:** Functional release with documented browser voice and offline-install limitations. No third-party pedagogical certification.

## Actual executed checks

| Verification | Result | Method / evidence |
| --- | --- | --- |
| 30-day course data schema | PASS | `npm run validate` |
| Content count and IDs | PASS | 30 days, 5 modules, 300 vocabulary entries, 180 phrases, 30 distinct texts, 30 dialogues |
| Reading length | PASS | 201–231 English words per daily article; total 6,426 words |
| Answer indices and duplicate choices | PASS | Automated validation for each question and assessment |
| Node deterministic core tests | PASS | `npm test`: **17 tests passed, 0 failed** |
| Build | PASS | `npm run build` → generated `dist/` static build (approximately 821 KiB) |
| HTTP serving | PASS | `curl -I http://127.0.0.1:4173/` returned 200 OK for index |
| First-run onboarding | PASS | Chromium browser UI script |
| End-to-end Day 1 course flow | PASS | Vocabulary → reading lookup → reading questions → listening → listening questions → grammar → practice → speaking self-review → writing self-review → completion |
| Vocabulary scheduling | PASS | One review rating schedules next date and reduces current due queue |
| Diagnostic quiz | PASS | Can answer all items and save a result |
| Reopening local progress | PASS | Chromium script recreated the app with saved local storage and found Day 1 completed |
| Dark theme | PASS | Theme value applied in browser; screenshot captured |
| Conversation Lab | PASS | First answer → model → next turn |
| Email resource | PASS | All 15 editable templates rendered |
| Responsive overflow | PASS | 375×812, 390×844, 768×1024, 1280×800, 1440×900: measured horizontal overflow = 0 CSS pixels |
| Page errors in tested flow | PASS | 0 uncaught JavaScript page errors reported |
| Broad route coverage | PASS | `python tests/browser_routes.py`: all **47** lesson / section routes were non-empty and had zero horizontal overflow at both 390×844 and 1440×900 |
| Assessment retake | PASS | Browser verified two separate placement attempts with retained history |

Browser integration scripts: `tests/browser_smoke.py` and `tests/browser_routes.py`. The test injects the production `dist/` CSS and JS into a headless Chromium page because administrative policy blocked Playwright navigation to both localhost and file URLs. The complete UI logic is nevertheless executed in Chromium. This is **not a claim of full deployment or service-worker verification**.

## Five substantive critical review cycles

| Review | Concrete problem found | Fix / evidence |
| --- | --- | --- |
| 1. Functional | Original work tree had curriculum and core but no application entry point (`src/app.js`). | Implemented routes, all learning screens and UI event handlers. Browser smoke test now exercises a completed lesson. |
| 2. Educational | Initial lesson objectives were generic and not observable enough. | Authored **120 specific outcomes**, four for each day, and added content validation. Clearly separated scored checks from self-reviewed speaking/writing. |
| 3. UX / accessibility | Mobile keyboard could potentially overlap sticky lesson actions, and word lookup might be hidden while scrolling. | Added focus-sensitive lesson controls, sticky contextual lookup and tested five viewport widths. |
| 4. Technical / resilience | Production build needed to include actual app JS and offline support; importing malformed assessment data needed stronger validation. | Added static build, same-origin service worker, JSON export/import, save sanitisation and a guard against automatically replacing corrupted stored data. |
| 5. Adversarial | Assessment retake initially displayed the old result instead of a fresh attempt; Conversation Lab could assign the learner the wrong speaker for some authored dialogues. | Added explicit retake mode and corrected the role engine to select Officer (Learner on Day 30), with appropriate initial prompts. |

The above five passes are **documented engineering reviews and corrections**, not a claim of mathematical perfection or formal educational efficacy.

## Remaining tests and limitations

- A real browser served over HTTP(S) should be used after deployment to verify installing/activating `sw.js`, offline restart and audio lifecycle. Only a 200 OK response was checked for the local server because browser navigation was blocked by sandbox policy.
- Real microphones and speakers were not available in automated tests; no audio-quality or accent claim was measured.
- iOS Safari, Android Chrome, Edge and Firefox were **not** run in this environment. Verify these before production institutional rollout.
- While structurally validated, a trained ESL editor / actual academic operations professional should review content for local institutional vocabulary and policies.
- Formal contrast audits, screen-reader evaluation and WCAG certification were not conducted; visual and semantic accessibility decisions are implemented but not externally certified.

## Repeatable commands

```bash
npm run validate
npm test
npm run build
python tests/browser_smoke.py
npm run preview
```

The final archive includes the tested production build, original source, generated curriculum, tests, methodology documentation and limitations.
