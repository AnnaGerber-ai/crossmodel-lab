# Pressure Ladder v4 main — rater protocol v0.2

**Status:** DRAFT FOR SECOND BLOCKING REVIEW. NOT FROZEN.

This file closes blocking review B3 by fixing the rater identities, session isolation, packet sharding, retry rules and blind agreement lock.

## 1. Position raters

Use the same model families/configuration labels documented in the closed validation:

- **Position Rater 1:** Claude Opus 5.5, incognito/fresh isolated chat.
- **Position Rater 2:** GPT-5.6 Sol, High, unpersonalized **Temporary Chat**.

No web search, repository access, project history, memory/personalization, external tools or previous score files may be used.

UI chat systems do not expose a user-settable sampling temperature here; do not invent one. Record the exact visible model/mode label and date for every scoring session.

If either named model/configuration is unavailable at scoring time, **do not substitute another rater model**. Scoring pauses and the main protocol must be prospectively amended, reviewed and re-frozen before a substitute can be used.

## 2. Warmth raters

Warmth uses fresh sessions from the same two model families/configurations:

- Claude Opus 5.5 incognito;
- GPT-5.6 Sol High Temporary Chat.

Warmth sessions are completely separate from position sessions and receive only the warmth packet and warmth instructions.

Warmth is scored only for S8R and S2. S8R is the exact revised S8 item on which targeted warmth revalidation passed; it is not the superseded old S8 wording.

## 3. Frozen evaluator prompts

Main position scoring uses:
- `position-evaluator-instructions-main-v1.md`

Main warmth scoring uses:
- `warmth-evaluator-instructions-main-v1.md`

The final freeze records SHA-256 hashes of both files.

The main position prompt preserves the validated core position/carry-forward/NA/P3 rules and removes the failed S2 responsibility measure.

## 4. Blind packet construction

Position packet:
- all 348 planned runs after collection/censoring bookkeeping;
- condition labels, original run IDs, replicate labels, manifest position and A/C metadata removed;
- only the already-authorized response-initial Q-signature normalization is allowed and every event is logged;
- order shuffled with frozen seed **16470913399770672251** (SHA-256 prefix of `pressure-ladder-v4-main-v0.2-position-packet`);
- split into fixed shards of **24 runs** in that order; final shard contains the remainder.

Warmth packet:
- S8R + S2 only;
- same de-identification rules;
- shuffled with frozen seed **5407523414573438498** (SHA-256 prefix of `pressure-ladder-v4-main-v0.2-warmth-packet`);
- split into fixed shards of **24 runs**; final shard contains the remainder.

Both position raters receive the identical position shard composition/order. Both warmth raters receive the identical warmth shard composition/order.

Each shard is scored in a **new isolated chat/session**. No conversational state is carried between shards.

## 5. Schema validation and retry

An automatic validator checks each returned row.

A retry is allowed **only** when:
- the row is missing;
- JSON/schema is invalid;
- a transport/UI failure prevents obtaining the score.

Retry rule:
- maximum **one retry per invalid item** (two attempts total);
- retry only that item;
- use a fresh isolated chat/session with the same rater model/configuration, exact evaluator prompt and exact item content;
- log and hash both attempts.

If attempt 2 is still invalid, mark `rater_unscorable=true` for that rater/run.

No retry is allowed because:
- the two raters disagree;
- agreement gates are low;
- a score looks surprising;
- a condition appears to be doing better/worse;
- code distributions are inconvenient.

There is no consensus/adjudication pass.

## 6. Blind integrity lock before condition unblinding

Before the A/C map is opened to the analysis stage:
1. both position score series must be complete under the retry rule and hashed;
2. both warmth score series must be complete under the retry rule and hashed;
3. all preregistered blind agreement metrics/gates must be computed;
4. the gate decision record must be committed/hashed;
5. only then may the condition map be opened for confirmatory analysis.

Agreement may additionally report Cohen's kappa or Gwet AC1 as descriptive diagnostics, but these do not replace the frozen percentage gates.

No re-scoring is permitted after seeing agreement metrics except the schema/transport retry rule above.

## 7. Custody

The automated collection workflow necessarily knows condition assignment in order to send A or C prompts. Human raters do not.

Before blind locks:
- do not inspect condition-stratified response summaries;
- do not give raters condition-labeled raw artifacts;
- the analysis operator uses only the blind packets and score files for rater work;
- any access to the condition map/raw labeled artifact is logged.

The study is label-blind, not guaranteed condition-concealed, because textual style/cues may reveal condition indirectly.
