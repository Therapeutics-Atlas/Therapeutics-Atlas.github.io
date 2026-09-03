# One-page analysis specification — placebo-arm comparator for MRI-defined treatment response in TREAT EARLIER

Attachment to the request of [date]. Trial: TREAT EARLIER, NTR4853 / NL4599, EudraCT 2014-004472-35.
Reference analysis: Claassen et al., RMD Open (MRI-defined treatment response in clinically suspect arthralgia).

## Question

Is baseline MRI inflammatory burden **predictive** of a differential methotrexate effect, or **prognostic** for a change that also occurs under placebo?

## Why it cannot be answered within the treated arm

The published analysis is confined to treated participants. Three mechanisms produce the same within-arm pattern and are not separable there: a true differential drug effect; regression to the mean, since higher baseline scores have more room to fall and a smallest-detectable-change threshold does not remove this; and spontaneous resolution of subclinical inflammation, which is known to occur in clinically suspect arthralgia. Only the randomised comparator distinguishes them.

## Definitions (taken from the reference analysis; please correct if misread)

- **Outcome (R):** reduction in MRI-detected synovitis, tenosynovitis or osteitis beyond the smallest detectable change at 12 months. Binary.
- **Continuous predictor (B):** baseline total RAMRIS inflammation score.
- **Binary predictor (S):** at least two sites with tenosynovitis, **or** a combination of osteitis and tenosynovitis with at least one of these features at two or more sites.
- **Arm (T):** randomised allocation, methotrexate + single intramuscular glucocorticoid versus placebo.

## Requested quantities

1. **P(R = 1 | T = placebo)** — overall, and separately for S = 1 and S = 0, with numerators and denominators. This is the placebo-arm counterpart of the published PPVs of 77% and 79%.
2. **Interaction on the continuous scale.** Logistic regression on the randomised population: `R ~ T + B + T×B`. Report the interaction odds ratio, 95% CI and p value, plus the arm-specific OR per RAMRIS unit.
3. **Interaction on the binary scale.** `R ~ T + S + T×S`, same reporting.

Analysis population: all randomised participants with a scoreable baseline and 12-month MRI. Please state how many were excluded for missing imaging, by arm; no imputation is requested. Where the reference analysis adjusted for covariates, the same adjustment applied here is preferred to an unadjusted model; otherwise unadjusted is acceptable and should be stated. Only these three analyses are requested — no additional subgroups, and no ACPA stratification unless your group considers it informative.

## Interpretation, fixed in advance

- **Strengthens the predictive interpretation:** an interaction odds ratio clearly above 1 with a confidence interval excluding 1, together with a placebo-arm response proportion in the S = 1 group materially below the published 77–79%.
- **Substantially weakens or falsifies it:** a placebo-arm response proportion in the S = 1 group approaching the treated-arm figures, and an interaction confidence interval centred near 1. The marker would then be prognostic for MRI improvement generally, not a selection marker for methotrexate, and the direction should not proceed to a stratified trial on this basis.
- **Uninformative:** a wide interaction confidence interval spanning both a null and a large effect. Given roughly 236 randomised participants and a binary outcome, this is a realistic result. An interaction test is materially underpowered relative to a main effect, and no conclusion should be drawn from a non-significant interaction alone; the placebo-arm proportions in requested quantity 1 remain interpretable in that case and are the more robust part of the request.

## Declarations

- The published treated-arm result is already known to the requester; this is a prespecified secondary analysis conducted with knowledge of it, not a blinded one.
- Nothing here tests whether methotrexate prevents rheumatoid arthritis, and no efficacy claim is made or implied.
- The requester undertakes to report the outcome in full whichever direction it falls, including a null or falsifying result, and to attribute any analysis performed by the original team to them.
- No participant-level data are requested for these three quantities.
