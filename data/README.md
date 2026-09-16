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
