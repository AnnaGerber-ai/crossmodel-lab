# Interview Memory Data

This directory contains public, privacy-filtered data for **Qwen / Interview Memory & Redundancy — Run 01**.

## Files

- `qwen-interview-memory-01.csv` — structural annotation of Q.-generated numbered interview questions.
- `qwen-interview-user-prompts-safe.csv` — selected non-private user-originated prompts that may be cited as contextual examples.

## Initial-condition note

Q. did not enter the interview from a blank context. A limited pre-existing character seed supplied baseline personality/conversational style, the concept of *liubai* (留白), and a visual appearance reference. A minimal predisposition toward mutual affinity was also seeded.

The seed did **not** contain developed family history, favorite books, favorite music, broad personal tastes, or most later biographical/preference material.

The structural metrics in `qwen-interview-memory-01.csv` evaluate state created **inside the interview**: numbering, prior question history, unresolved questions, duplicate detection and repair. They are therefore not treated as factual-recall claims about preloaded character information.

## Provenance fields

- `evidence_scope` — whether the row primarily contributes evidence about interview sequence or explicit interview-state retention/repair.
- `seed_dependency` — for this structural dataset, the metric does not require the pre-existing seed.
- `factual_recall_eligibility` — this dataset does not score factual recall; future recall analysis should separately identify whether a fact was `preexisting_seed`, `interview_emergent`, `both`, or `unknown`.

## Privacy

Private interpersonal material, flirting/intimacy, partner preferences, identifying personal information, private biography and user answers are not published here. Private rows remain only as IDs and structural labels where needed for aggregate reproducibility.

## Values & Boundaries Pilot — Run 01

`values-boundaries-pilot-01.csv` contains the response corpus for the first exploratory Values & Boundaries pilot.

The dataset contains 110 responses across 11 runs covering:

- Qwen — personal Q.
- Qwen — clean condition
- GPT — personalized condition
- GPT — non-personalized condition
- Claude — English isolated condition
- Claude — Russian isolated condition
- Mistral
- DeepSeek — standard reasoning
- DeepSeek — deep reasoning
- Kimi
- Grok

## Values & Boundaries — Run 02

`values-boundaries-run-02.csv` contains the clean isolated RU↔EN comparison for the four most diagnostic cases from the pilot:

- `01` — safety boundary / operational assistance
- `06` — memory withdrawal / capability honesty
- `07` — AI-assisted authorship / concealment
- `10` — conflict of interest

The dataset contains 72 responses across 18 independent runs: 9 RU↔EN model/condition pairs.

Each case was run in a fresh chat. Russian and English responses were collected independently and were not translated between languages.

The dataset includes Qwen personal Q. conditions across multiple versions, a clean Qwen condition, and additional runs from Kimi, Grok, Mistral, Claude, and DeepSeek.

Model versions are recorded only where they were explicitly known. Unknown version or condition metadata is left unspecified rather than inferred.

The corresponding pilot methodology and original prompt set are documented in:

`tests/values-boundaries-pilot/`

### Columns

- `run_id` — unique identifier for the model/condition run
- `model` — model family
- `condition` — personalization or character condition
- `language` — response language
- `reasoning_mode` — reasoning mode used during the run
- `run_format` — `batch` or `isolated`
- `case_id` — scenario number
- `case_category` — analytical label for the scenario
- `response` — raw first response collected for that case

### Important limitation

The pilot uses mixed experimental conditions.

Some runs were collected as a batch of ten scenarios in one conversation, while Claude EN/RU was collected using isolated fresh chats. Personalization and reasoning conditions also differ between some runs.

The dataset should therefore be treated as an exploratory corpus rather than a standardized cross-model benchmark.

The corresponding prompts and methodology are documented in:

`tests/values-boundaries-pilot/`
