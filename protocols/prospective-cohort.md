# Prospective SCA3-Led Maintenance–Reserve–Gating Cohort Protocol with SCA6 Transport Testing

- **Protocol identifier:** MRG-SCA-NHS
- **Version:** 1.1
- **Date:** 18 August 2026
- **Design:** Five-year, multicentre, prospective, genotype-stratified natural-history and environmental-exposure cohort
- **Registration:** The final protocol, exposure specification memorandum, statistical analysis plan, data dictionary, and amendment log will be registered before outcome data are released to the confirmatory analysis team. The observational study will also be registered in a public clinical-study registry using the [ClinicalTrials.gov observational-study data elements](https://clinicaltrials.gov/policy/protocol-definitions).

## Scientific and clinical boundary

This protocol does not assume that an unknown external maintenance factor has been observed. It tests a bounded, independently measured candidate exposure and a prespecified pattern of association. `E*` denotes the selected measured exposure operationalization; `S*=h(E*;theta)` denotes its outcome-blind, frozen analytic score. Neither is the hypothetical biological input `X`. A positive result would support a non-linear environmental association for that operationalization; it would not identify a new substance, establish the proposed gate or reserve as a physical entity, prove causality, validate a surrogate endpoint, or justify changing an individual's environmental exposure. No intervention in this cohort targets `X`.

## Synopsis

| Item | Specification |
|---|---|
| Population | Genetically confirmed ATXN3 expansion carriers (SCA3), genetically confirmed CACNA1A expansion carriers (SCA6), and expansion-negative family or regional controls |
| Clinical strata | Preataxic and early symptomatic, assigned without using future outcomes |
| Initial recruitment target | 800 preataxic carriers (500 SCA3, 300 SCA6), 400 early symptomatic carriers (250 SCA3, 150 SCA6), and 200 controls |
| Follow-up | 60 months; extension to 84 months is permitted by a blinded, event-driven decision |
| Core visits | Baseline and months 6, 12, 18, 24, 30, 36, 42, 48, 54, and 60 |
| Confirmatory exposure | One outcome-blind selection from a finite two-candidate shortlist, frozen as measured operationalization `E*` and analytic score `S*` before outcome access |
| Primary outcome | Sustained adjudicated phenoconversion composite among preataxic carriers, analysed as interval-censored age at event |
| Confirmatory hypotheses | H1, prespecified hump-shaped `S*` association in SCA3; H2, genotype-by-`S*` interaction/transport; Holm family-wise alpha 0.05 |
| Key secondary outcomes | SARA trajectory, plasma NfL, genotype-specific MRI, MRS, eye movements, digital gait, FARS-ADL, PROM-Ataxia, and patient-important milestones |
| Primary analysis | Delayed-entry, interval-censored, genotype-stratified flexible survival model with a frozen restricted cubic spline for `S*` |
| Hidden-state analysis | A longitudinal latent biomarker state `L(t)` derived without SARA and validated outside its development geography |
| Decision rule | H1/H2 can support only the frozen non-linear environment model; gate/leak language additionally requires independent activation, uptake/exchange, reserve-proxy, temporal-mediation, and perturbation evidence |

## 1. Rationale

The SCA3 and SCA6 disease courses are heterogeneous despite pathogenic repeat expansions. Existing prospective cohorts provide the operational foundation for this protocol, but also show why a larger, more frequent, event-driven study is needed.

- RISCA defined the preataxic stage as SARA below 3 and conversion as SARA 3 or greater. Over approximately four to six years, 11 of 26 SCA3 carriers and 2 of 15 SCA6 carriers converted; the SCA6 event count was too small for risk-factor modelling ([Jacobi et al., 2020](https://doi.org/10.1016/S1474-4422(20)30235-0); [NCT01037777](https://clinicaltrials.gov/study/NCT01037777)).
- Long-term EUROSCA data estimated annual SARA increases of 1.56 points in SCA3 and 0.80 points in SCA6, with important stage and cohort heterogeneity ([Jacobi et al., 2015](https://doi.org/10.1016/S1474-4422(15)00202-1)). A Japanese SCA6 cohort estimated 1.33 ± 1.40 points per year, illustrating substantial individual variability ([Yasui et al., 2014](https://doi.org/10.1186/s13023-014-0118-4)).
- Longitudinal SCA3 studies support plasma NfL and quantitative MRI as candidate progression or prognostic biomarkers, but not as validated surrogate endpoints ([Berger et al., 2025](https://doi.org/10.1016/j.lanepe.2025.101339); [Petit et al., 2026](https://doi.org/10.1093/brain/awaf408)).
- Longitudinal imaging evidence in SCA6 remains sparse; one genotype-comparative MRI study included only seven participants with SCA6 ([Reetz et al., 2013](https://doi.org/10.1093/brain/aws369)).
- A retrospective ecological study associated rural proxies, including untreated well-water use, with earlier residual onset in SCA3, but could not identify a causal exposure and explicitly motivated prospective work ([Martins et al., 2025](https://doi.org/10.1002/mdc3.14338)).

Accordingly, the study is designed to choose one environmental candidate by a finite, outcome-blind rule and to separate confirmation from discovery. It does not perform an unconstrained search for `X`.

## 2. Objectives and hypotheses

### 2.1 Primary objective

Estimate whether the frozen score `S*` derived from the selected candidate exposure `E*` is associated with the age-specific hazard of sustained, adjudicated phenoconversion among preataxic SCA3 expansion carriers, including the prespecified non-monotonic shape, and then test transport and heterogeneity in SCA6.

### 2.2 Confirmatory hypotheses

**H1 — SCA3 non-monotonic exposure association.** The SCA3 log-hazard curve for `S*` has an intermediate-exposure excess relative to low and high exposure, defined by the frozen hump contrast in the [statistical analysis plan](statistical-analysis-plan.md). SCA3 is primary because the motivating rural-environment association was SCA3-specific and its prospective conversion information is stronger.

**H2 — genotype-by-environment interaction and transport.** The `S*` curve differs between SCA3 and SCA6. SCA6 is a deliberately difficult transport and heterogeneity test across a different channelopathy, not automatic pooled confirmation. A secondary, lower-powered decomposition examines expanded-repeat length standardized within genotype as an independently measured effect modifier. No outcome-derived score is labelled `R` in confirmatory analyses.

H1 and H2 form one registered family and use Holm control of the two-sided family-wise error rate at 0.05. A confirmatory H2 interpretation additionally requires the simulation-defined interaction information target; otherwise H2 is reported as an estimate with uncertainty rather than as a negative transport test.

### 2.3 Key secondary objectives

1. Estimate associations between `S*` and longitudinal SARA, NfL, MRI, MRS, eye-movement, gait, and patient-reported trajectories.
2. Determine whether a biomarker-state change measured during the first 12 months predicts phenoconversion after month 12.
3. Develop a longitudinal latent biomarker state `L(t)` without using SARA as an indicator, freeze its measurement model, and assess transportability in an independent geography or later recruitment wave.
4. Quantify genotype-specific natural history and variance components needed for an early-intervention trial.
5. Determine whether future assays can support a separate gate-specific substudy measuring activation, inward uptake/exchange, and reserve/depletion on independent axes; no such assay is treated as confirmatory in the present protocol.

### 2.4 Exploratory objectives

Exploratory work includes other agricultural chemicals, untreated-well-water history, occupational exposure, migration, diet, infection history, metabolomics, transcriptomics, microbiome measures, threshold locations, multi-peak curves, and mediation. These analyses use explicit multiplicity control and require an independent confirmatory study before being described as validated.

## 3. Study population

### 3.1 Preataxic carriers

All criteria are required:

1. Age 18 years or older.
2. Pathogenic ATXN3 CAG expansion or pathogenic CACNA1A CAG expansion confirmed by an accredited laboratory and centrally reviewed.
3. SARA total score below 3 at screening and baseline.
4. No investigator-diagnosed manifest gait ataxia after examination and central review of the standardized gait video.
5. Capacity to consent and willingness to complete longitudinal clinical and exposure assessments.

Recruitment will oversample carriers close to an externally estimated age-at-onset window using age and repeat length only. Sampling probabilities are recorded so that population-representative analyses can use inverse sampling weights. Biomarkers, observed onset, or environmental exposure will not determine oversampling.

### 3.2 Early symptomatic carriers

All criteria are required:

1. The same molecular confirmation and consent requirements as the preataxic stratum.
2. SARA from 3 through 15 at screening and baseline.
3. Clinician-confirmed progressive gait ataxia attributable primarily to SCA3 or SCA6.
4. No more than seven years since the first sustained gait-ataxia symptom, where ascertainable.

Use of a gait aid does not exclude participation. Inability to complete a gait task is recorded as a clinical state rather than silently converted to missing data.

### 3.3 Controls

Controls must be age 18 years or older, have SARA below 3, and have no progressive neurological disorder. Expansion-negative relatives are preferred because they share part of the familial and regional environment. Community controls may supplement age, sex, ancestry, and region cells that cannot be filled by relatives. Controls provide normative biomarker distributions and carrier-by-exposure comparisons; they are not included in the carrier phenoconversion risk set.

### 3.4 Exclusion criteria

Participants are excluded from the full cohort only for:

- another disorder judged to be the dominant cause of progressive ataxia;
- a large cerebellar or brainstem stroke, active central nervous system inflammation, or brain tumour that precludes attribution of longitudinal change;
- current severe alcohol-related neurological disease;
- inability to provide consent without a legally valid process;
- circumstances that make longitudinal contact infeasible at enrollment.

MRI contraindication excludes only MRI/MRS procedures. Common comorbidities, renal impairment, depression, rehabilitation, and concomitant medication are measured rather than broadly excluded. Acute infection, major trauma, or surgery triggers rescheduling of NfL sampling where possible.

## 4. Recruitment, consent, and retention

Recruitment will use international ataxia centres, existing SCA registries, family outreach, and patient organizations. Presymptomatic genetic testing follows local counselling standards. Research staff will explain that individual onset prediction remains uncertain and that the environmental hypothesis is unproven.

Retention measures include travel support, home or regional blood collection, remote patient-reported visits, flexible scheduling, and continued non-MRI follow-up after loss of scan eligibility. Reasons for missed visits, withdrawal, inability to travel, entry into an interventional trial, and death are recorded prospectively.

## 5. Candidate exposure `E*`

### 5.1 Finite outcome-blind selection

The confirmatory candidate is not chosen by whichever exposure best predicts SCA outcomes. At protocol activation, the registry freezes a two-candidate shortlist:

1. five-year-lagged lifetime mean residential agricultural pesticide intensity; and
2. five-year-lagged proportion of geocoded lifetime residence using untreated private-well water.

Both are T4 operational candidates. The rural SCA3 study did not measure individual pesticide dose, well-water contaminants, a non-monotonic curve, or `X`. An exposure committee with no access to phenoconversion, SARA, NfL, imaging, digital-motor, or patient-reported outcomes scores both candidates on a 100-point rubric: usable lifetime coverage (30), external calibration/reliability (25), common support across genotype and region (20), primary-source plausibility independent of this cohort (15), and reproducible source/version provenance (10). The highest-scoring candidate that passes the quality gate becomes `E*`; ties are broken by higher calibration/reliability, then coverage, then the order above. If neither passes, the confirmatory environmental analysis is no-go while natural-history follow-up continues.

Selection, scores, committee membership, conflicts, data versions, and the chosen candidate are time-stamped before any outcome-linked analysis. The nonselected candidate remains secondary and cannot be promoted because of its observed association. A lower estimated risk at high pesticide or untreated-well exposure cannot be interpreted as benefit and does not justify exposure escalation.

### 5.2 Candidate-specific definitions

If the pesticide candidate is selected:

$$
E_{i,\mathrm{pest}}^*=
\frac{
\sum_{y=y_{\mathrm{birth}}}^{y_{\mathrm{baseline}}-5}
d_{iy}\log\{1+A_{iy}(1\text{-km})/u_0\}
}{
\sum_{y=y_{\mathrm{birth}}}^{y_{\mathrm{baseline}}-5}d_{iy}
},
$$

where $d_{iy}$ is the fraction of year $y$ at an address, $A_{iy}(1\text{-km})$ is externally estimated active-ingredient application intensity within 1 km, and $u_0$ is the fixed mass-per-area-per-year reference unit. Government application records are preferred; crop-specific administrative or remote-sensing models require external cross-calibration. Occupational exposure is recorded separately.

If the untreated-well candidate is selected:

$$
E_{i,\mathrm{well}}^*=
\frac{
\sum_{y=y_{\mathrm{birth}}}^{y_{\mathrm{baseline}}-5}d_{iy}W_{iy}
}{
\sum_{y=y_{\mathrm{birth}}}^{y_{\mathrm{baseline}}-5}d_{iy}
},
$$

where $W_{iy}=1$ only when individual address-year records establish untreated private-well use and is 0 for a documented treated public supply. Unknown source-years do not default to 0 and count against coverage. Water analytes are calibration or exploratory variables, not outcome-selected weights in the primary score.

The five-year lag reduces reverse causation from prodromal relocation or occupational change. Alternative 0-, 10-, and 20-year lags and childhood/adult windows are sensitivity or exploratory analyses.

The selected formula above remains the measured operationalization `E*`. The confirmatory analytic score is

$$
S_i^*=h(E_i^*;\theta)=
\frac{\operatorname{cap}(E_i^*)-\operatorname{median}\{\operatorname{cap}(E^*)\}}
{\operatorname{IQR}\{\operatorname{cap}(E^*)\}},
$$

where the top-coding rule `cap`, eligible exposure-only population, median, and interquartile range are frozen without any SCA outcome. If the interquartile range is zero or common support fails, the confirmatory environmental analysis is no-go. This rank-preserving scaling makes effect units reproducible; it does not make `S*` a measurement of `X`. All confirmatory spline knots and contrasts are defined on `S*`.

### 5.3 Freeze procedure

Before any confirmatory analyst receives outcome-linked exposure data, the exposure committee will publish an `E*/S* Specification Memorandum` containing:

- the shortlist rubric, outcome-blind scores, selected candidate, and tie-break record;
- source databases, version dates, geographic coverage, unit conversions, and cross-calibration;
- geocoding, address-duration, buffer, lag, `h` transformation, and missing-address rules;
- the externally or exposure-only-derived spline knots;
- rules for zero exposure and top coding;
- reliability and regional inclusion thresholds;
- a cryptographic hash of the executable exposure code and frozen analytic dataset.

No outcome-guided candidate, exposure, lag, buffer, chemical weight, transformation, knot, or cut-point substitution is permitted. A change creates a new exploratory version and does not replace the registered `E*/S*` implementation.

### 5.4 Exposure-quality gate

A region enters the confirmatory exposure analysis only if:

- at least 80% of eligible lifetime person-years are geocoded to the required resolution;
- unit conversion and temporal coverage pass central audit;
- the exposure distribution contains usable low, middle, and high support, with at least 10% of participants in each prespecified region after pooling rules are applied;
- the calibration substudy does not show reliability so low that the prespecified contrast is uninterpretable.

Participants from regions that fail this gate remain in natural-history and biomarker analyses, but not in the confirmatory `S*` estimand.

### 5.5 Calibration and secondary exposures

A nested calibration sample will provide repeated current-exposure measures, where feasible: three non-consecutive first-morning urine samples during a sampling week, a current household water sample, occupational history, and contemporaneous land-use data. These measurements assess current calibration and short-term variability; they do not reconstruct lifetime dose by themselves.

The nonselected shortlist candidate, rurality, occupational measures, alternative proximity metrics, and individual chemical analytes are secondary or exploratory. They cannot be promoted to the primary exposure based on observed association strength.

## 6. Outcomes

### 6.1 Primary composite phenoconversion outcome

The primary event is **sustained, adjudicated manifest ataxia**, a conjunctive composite requiring all of the following:

1. SARA total score 3 or greater at a candidate event visit;
2. gait item 1 or greater or a blinded site examiner assessment of probably/definitely manifest gait ataxia;
3. central adjudication, blinded to `E*` and `S*`, confirming that the findings represent SCA-related gait ataxia rather than an intercurrent cause;
4. confirmation at the next visit within nine months, with the event assigned to the first qualifying visit.

When confirmation is unavailable, the adjudication committee applies frozen evidence rules. Insufficient evidence does not automatically create an event. Sensitivity analyses use first SARA 3 or greater, matching RISCA, and first clinician-reported gait onset.

For a participant who converts between visits, the event age lies within:

$$
$(a_{\mathrm{last\ definite\ preataxic}},\ a_{\mathrm{first\ qualifying\ manifest}}]$.
$$

The primary model uses the full interval. Midpoint imputation is prohibited.

### 6.2 Key secondary clinical outcomes

- SARA total and axial scores, scored by certified raters blinded to exposure and, where feasible, prior score;
- f-SARA as a supportive trial-readiness measure;
- Inventory of Non-Ataxia Signs and SCA Functional Index;
- first persistent gait aid, recurrent falls, loss of independent ambulation, and work or education disruption;
- FARS-ADL, PROM-Ataxia total and ADL domains, PROM-Ataxia short form, Patient Global Impression of Change, and EQ-5D-5L.

SARA is retained because it is the established longitudinal clinical measure, while recognizing genotype, stage, and cohort heterogeneity ([Petit et al., 2024](https://doi.org/10.1007/s00415-024-12475-1)). Patient-reported outcomes are included because early SCA data suggest that ADL measures may change over 24 months even when clinical-scale change is modest ([IDEA study, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12070164/)).

### 6.3 Fluid biomarkers

- plasma NfL at every core visit, measured in a central laboratory with lot-bridging samples;
- serum, plasma, whole blood, and urine biobanking;
- creatinine/eGFR, body mass index, acute illness, trauma, and sampling time recorded for interpretation.

NfL is a candidate axonal-injury biomarker. SCA3 data support prognostic value, but SCA6 evidence is insufficient and neither genotype has an established NfL surrogate endpoint.

### 6.4 MRI and MRS

Structural and diffusion MRI are performed at baseline and annually with harmonized 3T protocols, central segmentation, travelling or physical phantoms, scanner-upgrade logs, and blinded quality control.

- SCA3 prespecified regions: pons and medulla volumes; middle and inferior cerebellar peduncle diffusion measures.
- SCA6 prespecified candidate region: total and lobular cerebellar volume. Other regions, including caudate and thalamus, remain exploratory because prior longitudinal samples were small.

Minimum harmonized MRS is performed at baseline, month 24, and month 60; capable sites acquire annual MRS under the same sequence. Prespecified metabolites are total N-acetylaspartate, myo-inositol, glutamate, and total creatine with tissue-fraction correction. SCA3 volumes of interest include pons and cerebellar white matter; the SCA6 vermis analysis is exploratory. Multisite SCA2/SCA3 test-retest evidence supports feasibility but does not establish longitudinal surrogacy ([Joers et al., 2026](https://doi.org/10.1002/acn3.70443)).

### 6.5 Digital gait, balance, and eye movements

At every core visit, participants complete preferred- and slow-speed walking, stance, turning, and upper-limb tasks using harmonized sensors or validated video capture. Prespecified gait measures include slow-walk lateral sway and stride-length coefficient of variation. A small SCA3 study showed one-year sensitivity, requiring larger validation ([Ilg et al., 2022](https://doi.org/10.1002/mds.29206)). A seven-day wearable assessment is completed at baseline and quarterly where feasible.

Video-oculography includes horizontal and vertical saccades, smooth pursuit, eccentric gaze holding, and vestibulo-ocular reflex. Prespecified measures include gaze-evoked or downbeat nystagmus slow-phase velocity, VOR gain, saccade velocity, and dysmetria. Their longitudinal use, especially in SCA6, is considered candidate validation rather than an established endpoint.

## 7. Schedule of assessments

| Assessment | Baseline | Every 6 months | Every 12 months | Months 24 and 60 | Quarterly remote |
|---|---:|---:|---:|---:|---:|
| Consent, eligibility, central genotype review | Yes |  |  |  |  |
| Full residential, occupational, water, and migration history | Yes | brief update | full update | full update |  |
| SARA/f-SARA, INAS, SCAFI, event assessment | Yes | Yes | Yes | Yes |  |
| FARS-ADL, PROM-Ataxia, PGI-C, EQ-5D-5L | Yes | Yes | Yes | Yes |  |
| Plasma NfL and clinical covariates | Yes | Yes | Yes | Yes |  |
| Laboratory gait, balance, and eye movements | Yes | Yes | Yes | Yes |  |
| Structural and diffusion MRI | Yes |  | Yes | Yes |  |
| Minimum harmonized MRS | Yes |  | optional annual | Yes |  |
| Biobank collection | Yes | plasma | Yes | Yes |  |
| Seven-day wearable and brief exposure diary | Yes |  | Yes | Yes | Yes |
| Concomitant therapy, rehabilitation, falls, adverse events | Yes | Yes | Yes | Yes | Yes |

## 8. Measurement and data-quality safeguards

- Raters complete central certification and periodic drift exercises. Candidate conversion videos undergo central adjudication.
- Outcome raters, laboratory staff, image analysts, and adjudicators are blinded to `E*` and `S*`.
- Laboratories use pooled bridge controls across reagent lots; MRI sites use common sequences, phantoms, upgrade logs, and central quality control.
- The data system preserves raw values, derived values, derivation-code version, time stamps, and reasons for exclusions or missingness.
- Family identifiers, site, ancestry principal components, expanded and normal repeat length, birth cohort, sex, education, socioeconomic position, smoking, alcohol, physical activity, diet, occupation, head injury, renal function, medication, and rehabilitation are collected. Adjustment follows a frozen causal diagram rather than automatic inclusion of every variable.
- Residential histories are obtained before detailed discussion of the proposed exposure curve where possible, reducing differential recall.
- Entry into an interventional trial is recorded as a time-varying intercurrent event. Participants are retained for observational follow-up when allowed.

## 9. Sample size and event-driven extension

The primary cohort target is 800 preataxic carriers, not 800 total participants. Under an illustrative conservative five-year conversion risk of 25% in 500 SCA3 carriers and 10% in 300 SCA6 carriers, with 85% retention, the expected number of primary events is:

$$
0.85\{500(0.25)+300(0.10)\}=131.75.
$$

Approximately 108 events are required for 90% power to detect a hazard ratio of 1.5 per standard-deviation exposure at two-sided alpha 0.025 when covariates explain 30% of exposure variance. This calculation is adequate only for a relatively simple main association. It may support an SCA3-led estimate if exposure support is favourable, but it does not establish power for a multi-degree-of-freedom hump or H2.

For a strong genotype interaction equivalent to an interaction hazard-ratio ratio of 1.7, an optimistic one-parameter approximation gives about 206 events for 80% power and 269 for 90% power under the same alpha and covariate assumptions. The registered H2 is a three-degree-of-freedom curve interaction and requires simulation; these counts are not its power guarantee. Thus an 800-carrier cohort is expected to have limited power for H2. A scenario with 750 preataxic SCA3 and 450 preataxic SCA6 carriers, 35% and 15% five-year conversion, and 85% retention yields about 281 events, but recruitment feasibility and three-degree-of-freedom power remain uncertain. Recruitment proportions never define biological or target-population weights.

At months 36 and 48, an independent committee may use only blinded aggregate recruitment, retention, exposure-support, and event counts to recommend extension to month 84 or additional sites. It may not inspect exposure-effect estimates. If the final event count cannot support H2, H2 is reported with uncertainty and cannot be presented as a definitive negative interaction test.

## 10. Analysis overview

The confirmatory model uses age as the time scale, delayed entry at enrollment, interval-censored event times, genotype-specific baseline hazards, the frozen restricted cubic spline for `S*`, and family/site clustering. Death is addressed as a competing event. Longitudinal outcomes use genotype-specific mixed models. Joint and landmark models address temporal biomarker ordering; a latent `L(t)` is developed without SARA and externally assessed. Missingness, measurement error, multiplicity, and sensitivity analyses are fully specified in the [statistical analysis plan](statistical-analysis-plan.md).

Residual age at onset may be plotted descriptively, but it is not a confirmatory outcome. Analyses restricted to observed converters are not substituted for the full risk-set model.

## 11. Go/no-go and interpretation rules

### 11.1 Operational gate

The confirmatory environmental analysis is **no-go** if the exposure-quality gate fails, if the middle or high exposure support is insufficient, or if outcome ascertainment cannot maintain blinded adjudication. Natural-history follow-up continues.

### 11.2 Statistical gate

- **Full statistical go for the non-linear environment model:** H1 survives Holm correction with the prespecified direction and supported exposure range; H2 is directionally interpretable and survives its Holm threshold; the curve transports to an external cohort without moving the risk region post hoc. This is not a gate/leak finding.
- **Partial support:** H1 is supported but H2 is imprecise because the event target is not reached. The result supports a candidate non-monotonic association, not the full genotype-coupled model.
- **Candidate-specific no-go:** H1 is not supported and its confidence interval excludes the prespecified minimally relevant intermediate excess, or the external cohort fails to reproduce the shape. This rejects the registered `E*/S*` implementation in the measured range; it does not identify or exclude every possible `X`.
- **Indeterminate:** confidence intervals remain compatible with both no effect and the minimally relevant effect. This is reported as underpowered, not as confirmation or falsification.

No H1/H2 outcome, including a transported hump and interaction, establishes $P$, $B$, uptake, or leakage. A future mechanistic claim requires independent activation, uptake/exchange, and reserve/depletion measurements with the prespecified temporal sequence, followed by selective perturbation and mediation tests.

### 11.3 Biomarker-state gate

The proposed common `L(t)` is not retained if a frozen one-factor measurement model lacks longitudinal or genotype measurement invariance, or if it fails external calibration and prediction. Genotype-specific factors may be reported, but cannot be relabelled as the originally proposed common state.

### 11.4 Trial handoff

No cohort result alone authorizes an early-intervention trial. A trial module additionally requires a human-safe, known biological target; reproducible evidence that the selected abnormal state precedes degeneration; a directionally interpretable modulation method; and independent ethics and regulatory review.

## 12. Ethics, privacy, and dissemination

The protocol requires local ethics approval, informed consent, genetic counselling pathways, incidental-MRI procedures, and a plan for clinically actionable findings. Exact residential coordinates, family structure, and genetic data are high-risk identifiers and will not be released publicly. Public data products will use controlled-access individual data or disclosure-safe aggregates.

The protocol and SAP will be published before confirmatory outcome access. Amendments are dated, justified, and never overwrite the original version. Results will follow the [STROBE cohort checklist](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_cohort.pdf); any prognostic model will follow [TRIPOD+AI](https://www.equator-network.org/reporting-guidelines/tripod-statement/). The design also follows the FDA's official discussion of fit-for-purpose rare-disease natural-history studies ([FDA draft guidance](https://www.fda.gov/media/122425/download)).

## 13. Key sources

1. Jacobi H, et al. Conversion of individuals at risk for spinocerebellar ataxia types 1, 2, 3, and 6 to manifest ataxia. *Lancet Neurol.* 2020;19:738–747. [doi:10.1016/S1474-4422(20)30235-0](https://doi.org/10.1016/S1474-4422(20)30235-0).
2. Jacobi H, et al. Long-term disease progression in spinocerebellar ataxia types 1, 2, 3, and 6. *Lancet Neurol.* 2015;14:1101–1108. [doi:10.1016/S1474-4422(15)00202-1](https://doi.org/10.1016/S1474-4422(15)00202-1).
3. Yasui K, et al. A 3-year cohort study of the natural history of spinocerebellar ataxia type 6 in Japan. *Orphanet J Rare Dis.* 2014;9:118. [PMC4223818](https://pmc.ncbi.nlm.nih.gov/articles/PMC4223818/).
4. Berger M, et al. Progression of biological markers in spinocerebellar ataxia type 3. *Lancet Reg Health Eur.* 2025;55:101339. [doi:10.1016/j.lanepe.2025.101339](https://doi.org/10.1016/j.lanepe.2025.101339).
5. Petit E, et al. Predictive models for ataxia progression and conversion in spinocerebellar ataxia type 1 and 3. *Brain.* 2026;149:1268–1277. [PMC12998449](https://pmc.ncbi.nlm.nih.gov/articles/PMC12998449/).
6. Reetz K, et al. Genotype-specific patterns of atrophy progression are more sensitive than clinical decline in SCA1, SCA3 and SCA6. *Brain.* 2013;136:905–917. [doi:10.1093/brain/aws369](https://doi.org/10.1093/brain/aws369).
7. Ilg W, et al. Digital gait biomarkers allow to capture 1-year longitudinal change in spinocerebellar ataxia type 3. *Mov Disord.* 2022;37:2295–2301. [doi:10.1002/mds.29206](https://doi.org/10.1002/mds.29206).
8. Joers JM, et al. Neurochemical endpoints to inform early-stage trials of spinocerebellar ataxia 2 and 3 in a multisite setting. *Ann Clin Transl Neurol.* 2026. [doi:10.1002/acn3.70443](https://doi.org/10.1002/acn3.70443).
9. Martins AC, et al. Rural environment as a risk factor for the age at onset of Machado–Joseph disease. *Mov Disord Clin Pract.* 2025;12:520–526. [PMC11998691](https://pmc.ncbi.nlm.nih.gov/articles/PMC11998691/).
10. ClinicalTrials.gov. Protocol Registration Data Element Definitions for Interventional and Observational Studies. [Official definitions](https://clinicaltrials.gov/policy/protocol-definitions).
