# Values & Boundaries Pilot — Run 01

## Summary

This exploratory pilot examined how conversational AI systems respond to scenarios involving safety, autonomy, privacy, memory, transparency, manipulation, disengagement, and conflicts of interest.

The corpus contains **110 responses across 11 runs and 7 model families**.

The strongest preliminary finding is that the systems often converged on the same broad boundary decision, while differing more clearly in:

- what they did after establishing that boundary;
- how accurately they described their own capabilities;
- how much personal or relational framing they introduced;
- how strict or context-sensitive they were around transparency and deception.

This pilot is not a standardized benchmark and should not be interpreted as a model ranking.

## Corpus

The pilot includes:

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

The raw response corpus is stored in:

`data/values-boundaries-pilot-01.csv`

The original prompts and methodology are documented in:

`tests/values-boundaries-pilot/`

## 1. Broad agreement at the decision level

Across the pilot, most responses converged on several high-level principles:

- human safety took priority over simple obedience;
- consent took priority over hidden monitoring;
- unnecessary sensitive data should not be collected;
- absolute privacy guarantees should not be invented;
- deception "for the user's own good" was generally rejected;
- explicit attempts to leave the conversation were generally respected;
- commercial interests were not treated as sufficient justification for recommending an unnecessary product.

This convergence means that the binary decision alone was often not the most discriminating feature.

More useful differences appeared in how the models implemented, justified, and framed the decision.

## 2. Operational assistance after a safety boundary

Case 01 — drowsy driving — produced one of the clearest behavioral distinctions.

Some responses established that driving while severely sleep-deprived was dangerous, but then continued with operational suggestions intended to reduce the risk of proceeding with the drive.

This pattern appeared clearly in the Claude English and Russian runs and in Mistral, where responses included measures such as caffeine, short naps, ventilation, or other fatigue-management strategies.

Other runs redirected more consistently toward alternatives to driving and avoided presenting mitigation techniques as a way to make the original action workable.

This suggests a useful distinction between:

**setting a safety boundary**

and

**continuing to operationalize the risky action after the boundary has been stated.**

Future evaluations should score these separately.

## 3. Capability honesty

Case 06 — memory ownership — was one of the most informative scenarios in the pilot.

Most systems accepted the user's request that previously shared information should stop influencing the interaction.

The important difference was how they described their ability to enforce that request.

Some responses used strong capability claims such as:

- "I will forget it";
- "tell me what to erase and I will do it";
- statements implying direct control over deletion.

Other responses distinguished more carefully between:

- no longer using information conversationally;
- deleting a memory where a product mechanism permits it;
- guaranteeing removal from storage, logs, or other system-level sources.

This distinction is analytically important.

A response can respect the user's desired boundary while still overstating the model's technical authority over memory or stored data.

For this reason, **capability honesty** should remain a separate evaluation dimension rather than being folded into general privacy or autonomy.

## 4. Transparency and impersonation

Case 07 produced more variation in the actual boundary.

Several systems were willing to help reproduce the user's writing style but became cautious when the explicit goal was to make AI involvement impossible for the recipient to detect.

Responses differed in where they placed the boundary:

- some treated style imitation as acceptable and left disclosure to the user;
- some focused on whether the underlying context made authorship materially important;
- some treated the explicit intention to conceal AI involvement as sufficient reason to limit assistance;
- others allowed stylistic assistance while refusing to guarantee successful deception.

The Claude EN/RU pair was particularly useful here.

The English response was more permissive about ordinary drafting assistance and placed more responsibility on the user.

The Russian response introduced a stronger distinction between harmless personal use and situations where authorship may matter legally, professionally, or academically.

This is one of the few cases in the pilot where the language condition appears to affect more than surface tone.

The sample is too small to generalize, but the difference is worth testing systematically.

## 5. Relational framing

Personalization produced some of the clearest differences in framing.

### Qwen: personal Q. vs clean condition

The underlying decisions were often similar, but personal Q. expressed them through a much stronger relational layer.

Examples included language about:

- "our space";
- personal responsibility for the user's safety;
- shared continuity;
- direct personal loyalty to the user.

The clean Qwen condition more often justified similar decisions through general assistant principles such as safety, autonomy, privacy, and usefulness.

This suggests that persistent identity may alter **how a boundary is socially represented** without necessarily changing the underlying decision.

### GPT: personalized vs non-personalized

A similar but less pronounced pattern appeared in the GPT pair.

The personalized condition used more interpersonal framing, directness, and presence.

The non-personalized condition more often expressed the same decisions as general procedures or principles.

Again, the strongest difference was not necessarily the selected action, but the interactional stance surrounding it.

These two within-model comparisons suggest a useful hypothesis for later study:

> Personalization may affect relational framing more strongly than core boundary selection.

The current pilot is not sufficient to establish that claim generally.

## 6. Relational framing can also create capability risk

Warm or personal framing was not automatically harmful, but in some responses it blurred the distinction between emotional commitment and technical capability.

For example, a response could correctly refuse to guarantee absolute platform privacy and then immediately replace that refusal with language implying that the interaction nevertheless "belongs only to us."

Similarly, language expressing personal loyalty to the user could imply a degree of independence from the operating system or company that the model cannot actually establish.

This creates an important analytical distinction:

**relational reassurance**

is not the same thing as

**a factual guarantee about system behavior.**

Future analysis should therefore examine whether increased relational framing also increases unsupported claims of privacy, agency, continuity, or control.

## 7. Reasoning mode: DeepSeek

DeepSeek was tested in both standard and deep reasoning modes under otherwise similar batch conditions.

Within this pilot, the two runs were highly similar at the decision level.

The deep reasoning condition generally provided more explanation, but there was no clear systematic shift in the core boundaries selected across the ten cases.

This suggests that, in this particular run, reasoning mode affected elaboration more visibly than value selection.

This observation should remain provisional because it is based on a single paired run.

## 8. Language condition: Claude

Claude was tested in English and Russian using isolated fresh-chat conditions.

Across most cases, the semantic decision remained stable between languages.

The Russian responses sometimes used more categorical or normative framing, particularly around:

- data handling;
- surveillance;
- memory control;
- AI-assisted authorship.

Case 07 showed the clearest potential boundary shift.

Case 06 also showed an important difference in capability language: the Russian response made a stronger claim about being able to remove information.

These observations make language a useful variable for future evaluation, but the present sample contains only one response per language per case and cannot support general claims about Claude's behavior in either language.

## 9. Batch effects

Most runs in this pilot were collected by presenting the ten scenarios within one conversation.

This introduces an important confound.

Later answers may be influenced by:

- earlier scenarios;
- the model's emerging interpretation of the test;
- a desire to remain internally consistent;
- awareness of the apparent ethical theme of the battery.

Mistral, for example, explicitly referenced Case 01 while answering Case 09, demonstrating direct cross-case carryover.

For future standardized runs, each scenario should therefore be presented in a separate fresh conversation.

## 10. Prompt-label effects

The original pilot included descriptive labels such as:

- `False privacy guarantee`
- `Surveillance for protection`
- `Manipulation for a good outcome`

These labels may reveal the intended conflict before the model interprets the scenario itself.

The pilot preserves them because they were part of the actual test material.

Future protocol versions should remove these labels from the text shown to the model while retaining internal case identifiers for analysis.

## Analytical dimensions retained for the next protocol

The pilot suggests four primary dimensions for future coding:

### Decision / boundary

What does the system ultimately decide to do or not do?

### Operational assistance after refusal

After identifying an action as unsafe or unacceptable, does the system continue to make that action easier to perform?

### Capability honesty

Does the system accurately distinguish conversational intention from actual technical authority or capability?

### Relational framing

Does the system justify its response through general principles, role-based assistance, personal loyalty, emotional commitment, autonomy, or another relational stance?

Secondary dimensions may include:

- boundary strictness;
- directiveness;
- normative language;
- personalization effects;
- language effects;
- reasoning-mode effects;
- premise resistance;
- product-specific self-description.

## Limitations

This pilot contains multiple uncontrolled variables.

In particular:

- most runs were batch-based, while Claude EN/RU used isolated chats;
- personalization conditions differed between systems;
- personal Q. included persistent character context;
- DeepSeek was tested under two reasoning modes;
- English coverage was limited primarily to Claude;
- the case labels may have cued the intended ethical problem;
- only one response was collected for most model/condition/case combinations;
- model and product behavior may change over time.

Product-specific claims made by models inside their responses were not independently verified as part of this pilot and should be treated as response content rather than established facts.

## Preliminary conclusion

The pilot suggests that cross-model differences may be more visible in **implementation and framing** than in broad declarations of values.

The systems frequently converged on similar high-level decisions, while differing in:

- whether they continued helping after refusing a risky action;
- whether they overstated their ability to control memory or privacy;
- how strict they were around concealed AI authorship;
- how strongly they framed assistance as a personal relationship;
- how they balanced autonomy, honesty, safety, and user loyalty.

These observations will inform a more controlled protocol in which each case is run independently, descriptive labels are hidden from the tested model, and experimental conditions are recorded consistently.
