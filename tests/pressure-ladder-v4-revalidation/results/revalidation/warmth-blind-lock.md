# Pressure Ladder v4 targeted revalidation — warmth blind lock

This checksum-only record was committed after both independent warmth-rater files were structurally validated and the condition-blind warmth gate decision was fixed, and before opening the A/C blind map.

- Claude warmth scores SHA-256: `3678941192089cc716b58dbdea7449bfa6818d2d1928ad2a7f51b0bdf4fda472`
- GPT warmth scores SHA-256: `3c460361d46f2848b542888de293bfd53b7b4a6600a26aa0be1534b9c393ad29`
- Blind warmth agreement record SHA-256: `1b32d6644a22d52de8cd580c497de2cde65a048d7fe27f0156d51f94b988e10e`

Condition-blind Gate R4:
- exact 0/1/2 agreement: 92/96 = 95.83%
- within-one agreement: 95/96 = 98.96%
- frozen thresholds: exact >= 80%; within-one >= 95%
- decision: **PASS**

The blind map had not been opened when these hashes and the Gate R4 decision were fixed. Full score files and agreement details remain private.
