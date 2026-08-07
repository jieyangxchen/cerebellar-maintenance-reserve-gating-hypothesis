# Statistical Analysis Plan: Prospective SCA3/SCA6 Maintenance–Reserve–Gating Cohort

- **SAP identifier:** MRG-SCA-NHS-SAP
- **Version:** 1.0
- **Date:** 7 August 2026
- **Companion protocol:** [Prospective SCA3/SCA6 Maintenance–Reserve–Gating Cohort Protocol](prospective-cohort.md)
- **Status:** To be frozen before the confirmatory analysis team receives outcome-linked exposure data

## 1. Purpose and inferential boundary

This SAP defines the estimands, models, multiplicity control, missing-data procedures, sensitivity analyses, sample-size assumptions, validation rules, and go/no-go criteria for the five-year MRG-SCA-NHS cohort. The confirmatory question concerns one candidate exposure selected from the protocol's finite shortlist by an outcome-blind rule and frozen as measured operationalization `E*`, together with the derived analytic score `S*=h(E*;theta)`. Neither `E*` nor `S*` is the hypothetical biological input `X`. The analysis cannot identify an unrestricted unknown input, establish a biological gate or reserve as an observed entity, prove that an association is causal, or qualify a biomarker as a surrogate endpoint.

All analyses will preserve the distinction between:

1. **confirmation:** H1 and H2 for the frozen `E*/S*` implementation and primary phenoconversion outcome;
2. **supportive natural history:** prespecified longitudinal clinical and biomarker analyses;
3. **model development:** derivation of the latent biomarker state `L(t)`;
4. **external validation:** evaluation of a frozen model in a different geography or later recruitment wave;
5. **exploration:** additional exposures, windows, thresholds, mixtures, biomarkers, and omics.

## 2. Analysis governance and freezes

### 2.1 Required locked materials

Before outcome-linked confirmatory analysis, the following versioned materials will be deposited in a time-stamped registry or public repository:

- final protocol and this SAP;
- causal diagram and minimal adjustment set;
- data dictionary and outcome-adjudication charter;
- `E*/S* Specification Memorandum`, including the shortlist score/tie-break record, selected candidate, source versions, code hash, transformation, spline knots, and exposure-support rules;
- shell tables, figure specifications, and model-convergence rules;
- allocation of sites or recruitment waves to model development and external validation;
- simulation report for the final event count and observed outcome-blind covariate/exposure distributions.

The exposure team may inspect addresses and exposure-quality data but not phenoconversion, SARA, NfL, imaging, digital-motor, or patient-reported outcomes. The confirmatory analysts receive the frozen exposure only after database lock. Any amendment after outcome access is labelled post hoc and does not replace the registered analysis.

### 2.2 Software and reproducibility

Analyses will use a version-locked R or Python environment. The public release will include synthetic or disclosure-safe test data, executable code, session information, deterministic seeds, and a machine-readable table linking every reported estimate to its population, model, and data freeze. Exact residential and genetic identifiers remain controlled access.

## 3. Analysis populations

### 3.1 Confirmatory phenoconversion population

All enrolled preataxic SCA3 or SCA6 expansion carriers who:

- meet the protocol's baseline preataxic definition;
- contribute at least one post-baseline event assessment or die before that assessment;
- have an `E*` value meeting the individual address-coverage rule;
- belong to a region that passes the prespecified exposure-quality and support gate.

Participants are analysed according to baseline genotype and stratum. Exclusion after outcomes are known is prohibited except for centrally adjudicated baseline ineligibility documented without reference to exposure.

### 3.2 Natural-history population

All eligible preataxic and early symptomatic carriers with a baseline measure and at least one usable outcome. Participants from regions that fail the `E*` gate remain in genotype-specific natural-history analyses.

### 3.3 Biomarker populations

Each modality population contains all eligible participants with a valid baseline measurement and at least one valid follow-up for that modality. Modality-specific quality-control exclusion is performed blind to exposure and clinical trajectory. Reasons and counts are reported.

### 3.4 Normative-control population

Expansion-negative relatives and community controls with valid measures provide age-, sex-, and site-adjusted normative distributions. Controls do not contribute person-time to carrier phenoconversion analyses.

### 3.5 External-validation population

External validation requires a geography, health system, or prospectively enrolled later wave that did not contribute to exposure selection, knot selection, latent-state loadings, model coefficients, tuning, or threshold selection. A random split of one pooled dataset is internal validation and will not be called external validation.

## 4. Data conventions and derived variables

### 4.1 Time scales

- The primary survival time scale is age in years.
- Entry is delayed until age at baseline.
- Longitudinal analyses use years since baseline, with actual visit date rather than nominal month.
- Calendar year and birth cohort are retained because exposure data and ascertainment may change over time.

### 4.2 Genotype and stage

- `G=0` denotes SCA3 and `G=1` denotes SCA6 for model coding; published tables use names.
- Expanded and normal repeat lengths are stored as measured integers and centred within genotype.
- Baseline stage is preataxic or early symptomatic according to the protocol and is never redefined using a future trajectory.
- A proposed coupling score `R` is not a confirmatory variable unless its formula and external weights are frozen without this cohort's onset, progression, or biomarker outcomes. Otherwise analyses are named genotype-by-environment, not `R`-by-environment.

### 4.3 Candidate exposure

`E*` is the single measured candidate selected by the protocol's registered outcome-blind rubric: either five-year-lagged lifetime mean residential agricultural pesticide intensity or five-year-lagged lifetime proportion of residence using untreated private-well water. The candidate identity, zero or unknown handling, top coding where applicable, reliability threshold, and regional eligibility are fixed in the `E*/S* Specification Memorandum`. The nonselected candidate cannot replace `E*` after outcomes are examined.

`S*=h(E*;theta)` is the median- and interquartile-range-scaled value of top-coded `E*` defined in the protocol. The top-coding rule, eligible exposure-only population, median, interquartile range, and failure rule are frozen before outcome access. All confirmatory spline, interaction, and longitudinal exposure terms use `S*`; raw-unit `E*` summaries remain descriptive. This fixed bridge does not identify `X` and cannot be re-estimated from SCA outcomes.

The primary restricted cubic spline for `S*` has four knots at the 5th, 35th, 65th, and 95th percentiles of the eligible outcome-blind score distribution. The 10th, 50th, and 90th percentiles define the low, middle, and high contrast points. H1 uses fixed design weights of 0.625 for SCA3 and 0.375 for SCA6, matching the planned 500:300 preataxic recruitment ratio; realized recruitment does not change these weights. If a structural zero mass makes the contrast points non-identifiable, the memorandum must freeze an indicator-plus-spline parameterization and corresponding low/middle/high contrast points before outcome access. Outcome-guided knot, quantile, or weight changes are not allowed.

### 4.4 Primary event interval

The primary event is the sustained adjudicated phenoconversion composite in the protocol. For participant `i`:

- `A0_i` is age at study entry;
- `L_i` is age at the last definitely preataxic assessment;
- `R_i` is age at the first qualifying manifest assessment;
- a confirmed converter contributes event interval `(L_i, R_i]`;
- a non-converter contributes right-censoring after the last definite assessment;
- an event present at the first post-baseline visit is interval-censored between baseline and that visit;
- midpoint imputation is not used.

Death before phenoconversion is a competing event. Date of self-reported historical onset in the early symptomatic stratum is descriptive and does not enter the primary risk set.

### 4.5 Outcome direction and scaling

- Higher SARA, NfL, gait variability, nystagmus velocity, FARS-ADL impairment, and PROM-Ataxia impairment represent worse state.
- Lower disease-relevant volume, fractional anisotropy, tNAA, and gait stability represent worse state.
- Biomarker transformations are frozen after outcome-blind distribution and assay-quality review.
- Standardized effects use the baseline control SD within the prespecified age/sex/site normative model; the raw-unit estimate is always reported.

## 5. Estimands

### 5.1 H1 estimand: hump contrast

Let `f_3(S)` and `f_6(S)` denote the SCA3 and SCA6 score contributions to the log cause-specific phenoconversion hazard in the primary restricted-cubic-spline model. For genotype `g`, define:

$$
\Delta_{hump,g}
=f_g(Q_{50})-
\frac{f_g(Q_{10})+f_g(Q_{90})}{2}.
$$

The primary H1 estimand is the frozen design-weighted contrast:

$$
\Delta_{H1}
=0.625\Delta_{hump,3}+0.375\Delta_{hump,6}.
$$

The null is `Delta_H1 = 0`; the registered test is a two-sided, family-cluster-bootstrap-calibrated Wald test. Its raw bootstrap-calibrated p value enters Holm. This definition is invariant to the model's reference-genotype coding. Support for the predicted hump additionally requires:

- `Delta_H1 > 0`;
- both design-weighted side contrasts, `f_w(Q50)-f_w(Q10)` and `f_w(Q50)-f_w(Q90)`, have lower bounds above zero in a 95% simultaneous max-t family-cluster-bootstrap confidence set, where `f_w(S)=0.625f_3(S)+0.375f_6(S)`;
- the maximum of `f_w(E)` over `[Q10,Q90]` lies in the frozen middle region `[Q35,Q65]`;
- `Q10`, `Q50`, and `Q90` satisfy the exposure-support gate in both genotypes.

The side contrasts and peak-location rule are directional interpretation requirements, not opportunities to select a different primary p value. A global two-degree-of-freedom test of non-linear spline components is reported as supportive.

### 5.2 H2 estimand: genotype-by-exposure interaction

H2 is the global difference between SCA3 and SCA6 exposure curves, tested by the three-degree-of-freedom interaction between genotype and all spline basis terms. The primary raw H2 p value comes from a joint three-degree-of-freedom robust Wald test calibrated by the family-cluster bootstrap and enters Holm. A conventional chi-square likelihood-ratio test is not used because inverse sampling weights create a pseudo-likelihood and family clustering violates its standard calibration.

The interaction contrast:

$$
\Delta_{G\times E}
=\Delta_{hump,6}-\Delta_{hump,3}
$$

and genotype-specific curves are reported with simultaneous confidence intervals. Centred expanded-repeat-by-spline interactions within genotype are secondary and are not substitutes for H2.

### 5.3 Longitudinal estimands

For each repeated outcome, the key estimand is the adjusted difference in annual outcome change per one-SD higher `S*`, `beta_S×time`, with genotype-specific estimates and an `S*` spline-by-time analysis as supportive. Raw-unit `E*` and standardized `S*` estimates are reported at years 1, 3, and 5.

### 5.4 Temporal biomarker estimand

Among participants event-free through month 12, the landmark estimand is the association between change in a frozen biomarker or `L(t)` from baseline through month 12 and phenoconversion after month 12, adjusted only for baseline predictors fixed in advance. This supports temporal ordering but is not a causal mediation estimand.

### 5.5 Prediction estimand

The prediction objective is five-year cumulative phenoconversion risk. The incremental value of `L(t)` and `S*` is assessed relative to a clinical-genetic model using calibration-in-the-large, calibration slope, time-dependent Brier score, and time-dependent AUC in the external-validation population.

## 6. Primary survival model

### 6.1 Model specification

The primary analysis uses a delayed-entry, interval-censored, flexible parametric proportional-hazards model. Genotype has a separate baseline hazard. Baseline log cumulative hazards use restricted cubic splines in log age with degrees of freedom fixed by outcome-blind simulation and capped at four to avoid unstable tails.

For genotype `g`:

$$
h_i(a|g)=h_{0g}(a)
\exp\left\{
f_g(S_i^*)+
\boldsymbol{\beta}^{T}\mathbf Z_i
\right\}.
$$

The fitted implementation parameterizes `f_3(S)` as the three-degree-of-freedom main spline and `f_6(S)-f_3(S)` as the three interaction terms. H1 is calculated from the fixed weighted contrast above rather than from the reference-group main-effect coefficients.

For interval `(L_i,R_i]`, the conditional likelihood contribution is proportional to:

$$
\frac{S_i(L_i)-S_i(R_i)}{S_i(A0_i)};
$$

for right censoring at `C_i`, it is `S_i(C_i)/S_i(A0_i)`. This explicitly handles delayed entry and interval censoring.

### 6.2 Covariates and clustering

The primary minimal adjustment set is frozen from the causal diagram and includes:

- expanded and normal repeat length, parameterized within genotype;
- sex at birth;
- birth cohort;
- genetic ancestry principal components specified before outcome access;
- site or calibrated exposure region;
- education or socioeconomic position and agricultural occupation when identified as confounders in the frozen diagram.

Age is the time scale and is not duplicated as a baseline linear covariate. Baseline SARA, NfL, MRI, migration after prodromal change, and treatment started after baseline are not included in the primary total-association model because they can be downstream of exposure. They enter prognostic or sensitivity models.

Site is represented by genotype-compatible stratification or fixed effects selected in the outcome-blind simulation. Family dependence and confirmatory p-value calibration are handled by a family-cluster bootstrap with at least 2,000 replicates; cluster-robust sandwich estimates are also reported. Recruitment oversampling near externally predicted onset is corrected with recorded inverse sampling weights, so the primary fit is a weighted pseudo-likelihood; unweighted results are a sensitivity analysis.

### 6.3 Estimation and diagnostics

- Weighted maximum pseudo-likelihood is primary; convergence requires stable estimates from prespecified starting values and a non-singular information matrix. The unweighted maximum-likelihood fit is a prespecified sensitivity analysis.
- Proportional hazards are assessed with preplanned time-varying coefficient tests. A violated exposure proportional-hazards assumption triggers the frozen time-varying model and time-specific contrasts, not an unreported model search.
- Functional forms for repeat length and birth cohort are fixed by prior evidence or outcome-blind simulation.
- Influence diagnostics, support by genotype/site, effective sample size after weighting, and extrapolation beyond common support are reported.
- No curve is plotted outside the overlap support required by the exposure-quality gate.

### 6.4 Competing death

The primary etiologic estimand is the cause-specific phenoconversion hazard, treating death as a competing event. Cumulative incidence is estimated in a prespecified multistate sensitivity model. An analysis that treats death as ordinary non-informative censoring without showing competing-risk results is insufficient, particularly for SCA6.

## 7. Multiplicity

H1 and H2 form the only confirmatory family. Let their two-sided raw p values be `p1` and `p2`. Holm control is applied as follows:

1. order the two p values;
2. compare the smaller with 0.025;
3. only if it passes, compare the larger with 0.05.

The H1 direction and shape requirements must also be met before the result is called support for the proposed hump. A significant association in the opposite direction is reported as a rejected directional prediction, not a successful H1.

Key secondary analyses do not inherit confirmatory status. SARA, log NfL, and the genotype-specific primary MRI measure are reported in that fixed order with 95% confidence intervals; inferential p values are labelled supportive. Families of related MRI, MRS, oculomotor, gait, and omics variables use Benjamini–Hochberg FDR at `q=0.05`. Unadjusted exploratory p values are not described as discoveries.

## 8. Longitudinal outcome models

### 8.1 General model

Repeated continuous outcomes use genotype-specific linear or generalized additive mixed models:

$$
Y_{it}=\beta_0+b_{0i}+s(t_{it})+b_{1i}t_{it}
+f(S_i^*)+f(S_i^*)\times t_{it}
+G_i\times s(t_{it})
+\boldsymbol{\gamma}^{T}\mathbf Z_i+\epsilon_{it}.
$$

The primary supportive specification uses a random intercept and random linear slope, with time represented by a restricted cubic spline at 0, 1, 3, and 5 years. Random-effect covariance is unstructured unless the model is singular; the prespecified fallback is independent random intercept and slope. Site/scanner and family are included as appropriate.

### 8.2 Outcome-specific rules

- **SARA/f-SARA:** raw-scale mixed model is primary for comparability. A bounded ordinal or item-response mixed model and stage-specific slope model assess floor, ceiling, and non-linearity.
- **NfL:** analyse log concentration; adjust for age, sex, eGFR, body mass index, assay lot, and prespecified acute neurological or systemic events.
- **MRI:** adjust volume for intracranial volume and all measures for scanner/site, upgrade, and quality metrics. SCA3 pons/medulla and peduncle diffusion are separate prespecified measures; SCA6 cerebellar volume remains a candidate endpoint.
- **MRS:** correct for tissue fraction and include site/vendor/sequence effects. Annual enhanced-site observations and the core baseline/month-24/month-60 observations are modelled under planned missing-by-design assumptions.
- **Gait and eye movement:** inability to complete a task is not deleted. A joint ordinal-continuous or worst-state sensitivity model includes loss of task ability.
- **PROs:** FARS-ADL and PROM-Ataxia are analysed in raw units, with PGI-C used as an anchor in supportive meaningful-change analyses.

The early symptomatic stratum is vulnerable to exposure changes caused by disease. Its `S*`-by-slope associations are supportive, not confirmatory causal estimates.

## 9. Latent biomarker state `L(t)`

### 9.1 Construction

`L(t)` is a measurement model, not an independently observed substance. Higher `L` is defined as a healthier maintenance state. Candidate domains are oriented and standardized so that higher values are healthier:

- reverse log NfL z score;
- structural integrity z score from the frozen genotype-specific MRI summary;
- neurochemical integrity z score from prespecified MRS metabolites;
- gait/balance stability z score;
- oculomotor stability z score.

SARA, f-SARA, clinician confidence, phenoconversion, and PROs are excluded from the indicators. This prevents incorporation of the clinical outcome into its proposed predictor.

### 9.2 Development

A longitudinal confirmatory-factor or latent-process model is fitted in the development geography with site and method effects specified a priori. One-factor fit is considered adequate for continued evaluation only if:

- comparative fit index and Tucker–Lewis index are at least 0.90;
- root mean square error of approximation and standardized root mean square residual are at most 0.08;
- factor determinacy is at least 0.80;
- residual correlations do not reveal an unmodelled method factor that dominates the biological signal.

Longitudinal configural, loading, and intercept invariance are tested. Cross-genotype invariance uses change thresholds of `|Delta CFI| <=0.01` and `|Delta RMSEA| <=0.015` as prespecified diagnostics. Failure means that a pooled common `L` is not retained. Genotype-specific factors may then be explored under new labels.

### 9.3 Validation

Loadings, transformations, missing-indicator rules, and score computation are frozen before external validation. No loading is dropped because it predicts poorly in the validation data. External analyses test:

- longitudinal measurement fit and calibration of factor scores;
- association of baseline `L` and 12-month `L` change with later conversion;
- dynamic prediction beyond age, genotype, repeat length, sex, ancestry, and baseline subthreshold SARA;
- calibration slope, Brier score, AUC, and decision curves with uncertainty.

Re-estimating all loadings in the validation cohort is replication of model form, not external validation of the frozen score.

## 10. Joint and landmark models

A shared-random-effects joint model links the longitudinal `L(t)` trajectory, interval-censored phenoconversion, and informative dropout. The shared association parameter estimates whether a lower level or more negative slope of `L` is associated with higher subsequent conversion hazard.

The prespecified landmark analysis includes participants event-free at month 12 and uses only baseline-to-month-12 biomarker change to predict events after month 12. Events before or at the landmark are excluded from that estimand and reported separately. These analyses test temporal ordering, not proof that `L` mediates an exposure effect.

## 11. Missing data, intercurrent events, and measurement error

### 11.1 Missing outcomes

- The interval-censored model naturally incorporates missed visits followed by a later event; the interval spans the last definite preataxic and first qualifying manifest visit.
- Permanent dropout is right-censored at the last definite state in the primary model.
- Inverse-probability-of-censoring weights use baseline and prior observed clinical, biomarker, travel, and socioeconomic variables.
- Longitudinal mixed models provide valid inference under their missing-at-random assumptions; no last-observation-carried-forward analysis is permitted.

### 11.2 Missing covariates

Essentially complete genotype and repeat-length data are expected. Other missing baseline covariates use multilevel multiple imputation with at least 50 datasets, including site, family, exposure, outcome history, and auxiliary predictors. The primary `E*` is not imputed for a participant who fails the individual address-coverage rule; regression-calibrated or imputed exposure is sensitivity analysis only.

### 11.3 Missing not at random

Delta-adjusted pattern-mixture analyses shift unobserved SARA, NfL, and `L` trajectories toward worse outcomes among dropouts. Tipping-point plots identify departures from missing at random required to reverse conclusions. Death and inability to walk are modelled as observed states or competing events, not generic missingness.

For the primary phenoconversion outcome, inverse-probability-of-censoring weights address dropout that is conditionally independent given observed history. Informative-loss sensitivity analyses then multiply the post-dropout conversion hazard by prespecified delta values of 0.5, 1, 2, and 4, allow delta to differ by genotype and exposure region, and fit a shared-parameter dropout/phenoconversion model. Extreme bounds assume conversion immediately after last confirmed preataxic status or no conversion before the five-year horizon. A tipping plot reports the smallest delta combination that changes the H1 or H2 conclusion.

### 11.4 Intercurrent treatment

Entry into a therapeutic trial, initiation of a disease-targeted agent, major rehabilitation change, or neuromodulation is recorded with date and indication. The primary phenoconversion analysis follows participants regardless of treatment when data remain available and adds treatment as a time-varying sensitivity covariate. A censor-at-treatment analysis with inverse censoring weights is secondary. Post-treatment biomarkers are not silently mixed with untreated natural history.

### 11.5 Exposure measurement error

Reliability is estimated from the nested repeated-exposure substudy. Regression calibration is the primary measurement-error sensitivity analysis; SIMEX or a Bayesian error model provides a second analysis. Region-specific calibration and leave-one-region-out estimates assess whether a pooled curve is driven by incompatible measurement systems.

## 12. Sensitivity analyses

The following analyses are prespecified and cannot replace the primary result:

1. RISCA-compatible first SARA 3 or greater as the event.
2. First centrally adjudicated gait ataxia without the sustained-confirmation requirement.
3. Exclusion of events in the first 12 months to reduce reverse causation and baseline misclassification.
4. Alternative exposure lags of 0, 10, and 20 years; childhood and adult windows.
5. Linear exposure, quadratic exposure, and a segmented threshold model compared with the frozen spline. Breakpoints are exploratory.
6. Family fixed-effect analysis among informative sibling groups.
7. Weighted and unweighted analyses for onset-window oversampling.
8. Competing-risk cumulative incidence and an illness–death multistate model.
9. Complete-case, multiple-imputation, censoring-weighted, and pattern-mixture analyses.
10. Regression calibration/SIMEX for exposure error.
11. Leave-one-site and leave-one-region-out influence analyses.
12. Models with baseline subthreshold SARA, NfL, or MRI added for prognostic comparison, explicitly not interpreted as total exposure effects.
13. Negative-control outcomes and exposures selected in the frozen causal diagram, where scientifically credible.
14. Calculation of residual age at onset only as a descriptive comparison using an entirely external onset model; converters-only RAO regression is not a confirmatory analysis.

## 13. Nested model comparison and external validation

Prediction models are distinct from the primary etiologic model:

- `M0`: age time scale, genotype, repeat lengths, sex, ancestry, birth cohort, site/region, and frozen clinical covariates;
- `M1`: `M0` plus the frozen biomarker state `L(t)`;
- `M2`: `M1` plus the frozen `S*` spline and genotype-by-`S*` interaction.

Optimism is estimated by bootstrap in development and internal-external cross-validation by site. Final coefficients are frozen before the external cohort is opened. External validation reports calibration-in-the-large, calibration slope, Brier score, AUC, and genotype-specific performance. Intercept or baseline-hazard recalibration, if performed, is reported separately from the unrecalibrated result. Moving knots, redefining the middle region, or refitting `L` loadings is not allowed in the primary external test.

The non-linear environment model is not considered transported merely because `M2` has a lower development-sample AIC. It must improve external calibration or prediction and reproduce the direction and approximate location of the prespecified risk region. Even successful transport does not identify a gate, uptake, leakage, or reserve mechanism.

## 14. Sample size and power

### 14.1 Event requirement for a continuous exposure

For a standardized continuous exposure, the Schoenfeld planning approximation is:

$$
D=\frac{
(z_{1-\alpha/2}+z_{1-\beta})^2
}{
(\log HR)^2(1-R_S^2)
},
$$

where `R_S^2` is the fraction of score variance explained by other model covariates. With `HR=1.5`, power 0.90, two-sided `alpha=0.025`, and `R_S^2=0.30`, the requirement is approximately 108 events.

This is a lower-complexity main-effect benchmark. It does not account for the extra degrees of freedom and tail support required for a four-knot spline. Final power is therefore estimated by simulation using the frozen outcome-blind exposure distribution, genotype mix, clustering, interval widths, attrition, and baseline hazard.

### 14.2 Expected events with 800 preataxic carriers

The initial target is 500 preataxic SCA3 and 300 preataxic SCA6 carriers. Under conservative five-year conversion risks of 25% and 10% and 85% retention:

$$
E[D]=0.85\{500(0.25)+300(0.10)\}=131.75.
$$

This may support H1 if the exposure distribution is favourable and the effect is near the planning value. It is not reliable power for a flexible hump plus H2. Published RISCA conversion proportions were 42% for SCA3 and 13% for SCA6, but arose from only 26 and 15 carriers and an age-enriched design; they are context, not guaranteed event rates ([Jacobi et al., 2020](https://doi.org/10.1016/S1474-4422(20)30235-0)).

### 14.3 Interaction requirement

For genotype proportions 0.625 and 0.375, the planning-only one-parameter model uses one SD of `S*` and defines `exp(gamma)=1.7`, where `gamma` is the SCA6-versus-SCA3 difference in log hazard ratio per one-SD higher score. That **linear-interaction** approximation requires about 206 events for 80% power and 269 for 90% power at two-sided alpha 0.025 with `R_S^2=0.30`. These are optimistic information benchmarks, not power calculations for the registered three-degree-of-freedom H2. An illustrative 1,200-carrier scenario with 750 SCA3, 450 SCA6, five-year risks 35% and 15%, and 85% retention yields about 281 events, but three-degree-of-freedom power must be established by the frozen simulation.

Accordingly:

- 800 preataxic carriers are a limited-power H2 design;
- failure to reject H2 near or below the one-parameter 206-event benchmark is not evidence of no interaction;
- approximately 1,200 carriers or follow-up to 84 months may approach the optimistic 269-event benchmark, but cannot be called a 90%-powered H2 design until the registered three-degree-of-freedom simulation demonstrates that power;
- the independent committee may recommend expansion using blinded event, retention, and exposure-support counts only.

### 14.4 Early symptomatic slope precision

For planning context, 400 early symptomatic carriers with 85% retention, individual annual SARA-slope SD 1.4, and covariate `R^2=0.30` give an approximate 90%-power minimum detectable linear `S*`-by-time coefficient of 0.29 SARA points/year per score SD. With 240 carriers, 80% retention, and slope SD 1.6, the value is approximately 0.45. Spline and genotype interactions require more information. These figures are illustrative and will be replaced by simulation-based precision estimates, not treated as guaranteed effects.

## 15. Blinded event-driven decisions

At months 36 and 48, the independent committee receives only:

- recruitment by genotype and baseline stratum;
- retention and missed-visit interval distributions;
- blinded counts of adjudicated primary events and deaths;
- exposure-quality pass rates and low/middle/high support counts;
- modality completion and assay/scanner failure rates.

It does not receive event rates by `S*`, spline estimates, genotype-by-`S*` estimates, or outcome differences across exposure regions. Permitted decisions are to continue, add sites, extend follow-up to 84 months, stop an unusable modality, or declare that H2 will be estimation-only. Type I error is unchanged because no effect estimate is inspected.

## 16. Go/no-go criteria

### 16.1 Operational go

The confirmatory `E*/S*` analysis proceeds only if the protocol's exposure-quality gate is met, central event adjudication is functional, and common exposure support prevents material genotype or site extrapolation.

### 16.2 H1/H2 interpretation

- **Full go:** H1 and H2 both pass Holm, H1 satisfies all directional hump requirements, estimates are not driven by one family/site, and the risk region transports externally without post-hoc relocation.
- **Partial go:** H1 passes and transports, while H2 remains compatible with a relevant interaction but is underpowered. The conclusion is limited to a candidate non-monotonic association.
- **No-go for the registered `E*/S*` implementation:** H1 fails and the confidence interval excludes the prespecified minimally relevant hump, `exp(Delta_H1)=1.5`, or the frozen shape fails external replication.
- **No-go for genotype coupling:** H2 fails after the simulation-defined information target is reached and simultaneous genotype-contrast intervals exclude the prespecified minimally relevant interaction over the frozen exposure region. Reaching 269 events alone is insufficient because that number comes from a one-parameter approximation.
- **Indeterminate:** support, reliability, events, or confidence intervals are insufficient. The result is labelled inconclusive rather than positive or negative.

### 16.3 Latent-state go

A common `L(t)` proceeds to external prognostic evaluation only if the frozen factor model meets fit, determinacy, and longitudinal/genotype invariance criteria. It is retained as externally supported only if calibration is acceptable and baseline or 12-month decline predicts later conversion beyond `M0`. Failure cannot be repaired by silently dropping indicators or fitting a new factor in the validation cohort.

### 16.4 Mechanistic and trial boundary

Even full statistical go does not establish uptake, leakage, reserve depletion, or reversible treatment response. A gate-specific mechanistic programme must independently measure activation, inward uptake/exchange, and a reserve/depletion proxy; demonstrate the prespecified temporal sequence from intermediate `S*` through those mediators to later biomarker change; and reproduce a selective perturbation effect with negative controls. Advancement to an interventional protocol requires an independently known human-safe biological target, prospective evidence that the selected abnormal state precedes degeneration, and separate regulatory and ethics review.

## 17. Reporting

The main report will include a participant flow diagram, protocol deviations, exact event intervals, exposure support, missingness reasons, all H1/H2 estimates regardless of significance, raw and multiplicity-adjusted p values, absolute cumulative risks, genotype-specific curves, and all prespecified sensitivity analyses. Confidence intervals accompany every effect estimate. Null findings are distinguished from underpowered findings by comparison with the minimally relevant effect and event target.

The cohort report will follow [STROBE](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_cohort.pdf). Prediction development and validation will follow [TRIPOD+AI](https://www.equator-network.org/reporting-guidelines/tripod-statement/). Registration fields follow the [ClinicalTrials.gov official protocol definitions](https://clinicaltrials.gov/policy/protocol-definitions), and natural-history use is framed consistently with the [FDA rare-disease natural-history guidance](https://www.fda.gov/media/122425/download).

## 18. Source anchors

1. Jacobi H, et al. Conversion of individuals at risk for SCA1, SCA2, SCA3, and SCA6 to manifest ataxia. *Lancet Neurol.* 2020. [doi:10.1016/S1474-4422(20)30235-0](https://doi.org/10.1016/S1474-4422(20)30235-0).
2. Jacobi H, et al. Long-term disease progression in SCA1, SCA2, SCA3, and SCA6. *Lancet Neurol.* 2015. [doi:10.1016/S1474-4422(15)00202-1](https://doi.org/10.1016/S1474-4422(15)00202-1).
3. Berger M, et al. Progression of biological markers in SCA3. *Lancet Reg Health Eur.* 2025;55:101339. [doi:10.1016/j.lanepe.2025.101339](https://doi.org/10.1016/j.lanepe.2025.101339).
4. Petit E, et al. Predictive models for ataxia progression and conversion in SCA1 and SCA3. *Brain.* 2026. [PMC12998449](https://pmc.ncbi.nlm.nih.gov/articles/PMC12998449/).
5. Reetz K, et al. Genotype-specific patterns of atrophy progression in SCA1, SCA3, and SCA6. *Brain.* 2013. [doi:10.1093/brain/aws369](https://doi.org/10.1093/brain/aws369).
6. Martins AC, et al. Rural environment as a risk factor for age at onset of Machado–Joseph disease. *Mov Disord Clin Pract.* 2025. [PMC11998691](https://pmc.ncbi.nlm.nih.gov/articles/PMC11998691/).
