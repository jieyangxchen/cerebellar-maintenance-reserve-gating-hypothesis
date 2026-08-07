# The External Maintenance Factor–Reserve–Gating Hypothesis of Hereditary Cerebellar Degeneration

## A unified framework for environmental dependence, emergent network states, non-linear resource mismatch, and early intervention

**Article type:** Hypothesis/Perspective

**Author:** Jieyang Chen

**Draft version:** 0.1.0, 7 August 2026

**Evidence cut-off:** 7 August 2026

**Affiliation:** Independent author (no institutional affiliation claimed)

**Correspondence:** [278404704@qq.com](mailto:278404704@qq.com); public repository Issues are for non-sensitive discussion only.

## Abstract

Pathogenic variants explain the cause of many spinocerebellar ataxias (SCAs), but they do not uniquely determine when disease becomes manifest or how rapidly it progresses. In one pooled SCA3/Machado–Joseph disease cohort, expanded ATXN3 CAG length explained approximately 62% of age-at-onset variance; stable SCA6 repeat lengths and monozygotic-twin observations likewise leave room for modifier effects. We propose a falsifiable *model class*, not a newly discovered substance: known genetic pressure may interact with an independently measured external input, genotype-dependent coupling, and a finite homeostatic reserve. In one optional extension, the same input can activate a high-demand state and open exchange before supply is sufficient. This produces a testable non-monotonic prediction—low-input idling, intermediate-input maximal depletion, and high-input rebalancing.

The framework separates measured exposures $E(t)$, a prospectively locked derived score $S=h(E;\theta)$, a still-hypothetical biological input $X(t)$, coupling $R$ defined without future outcomes, one mechanistic reserve state $B(t)$, and a biomarker measurement model $L(t)$. None of $X$, $R$, $B$, the gate, outward leakage, or the predicted hump-shaped risk curve has yet been observed in human SCA. Existing studies support only component premises: onset heterogeneity and premanifest human biomarker changes in selected cohorts; and stage-dependent resilience, multicellular/circuit contributions, or partial reversibility in selected animal or cellular models. These facts do not establish the proposed mechanism.

We specify a five-year, multicentre SCA3/SCA6 cohort that tests one outcome-blind-selected exposure from a predeclared two-candidate shortlist, with interval-censored phenoconversion, restricted-cubic-spline contrasts, genotype-by-exposure interaction, longitudinal biomarkers, and external validation. We also propose two separate, target-specific trial concepts: a conditional SCA3 mutant-ATXN3-lowering phase 2 study, and an early-manifest SCA6 L-arginine phase 2b study. A circuit “downshift” experiment remains phase 0 and cannot start until a reliable human hyperactivity classifier demonstrates temporal precedence and washout reversibility. These interventions test early modifiability of known biology; they do not validate $X$. A registered implementation should be rejected when adequately informative external data exclude its prespecified non-linearity or interaction, when the latent biomarker state adds no out-of-sample information, or when simpler known-mechanism models explain the observations equally well; underpowered results remain indeterminate.

**Keywords:** spinocerebellar ataxia; SCA3; SCA6; age at onset; environmental modifier; reserve; non-monotonic exposure; phenoconversion; early intervention; falsifiability

## One-sentence thesis

Some hereditary cerebellar degenerations may contain a testable mismatch layer between genetic demand, externally conditioned system activation, and finite homeostatic reserve—but the unknown-input extension earns causal status only if it predicts new human data better than models containing known mechanisms alone.

## Claim hierarchy

Throughout this Perspective, claims are separated into four levels:

1. **Established observation:** directly supported in the cited population or model.
2. **Supported analogy:** demonstrates biological plausibility of one component, but not this model.
3. **Testable inference:** prospectively operationalized and capable of failure.
4. **Speculation:** motivates research but has no direct evidentiary support.

The complete claim-by-claim audit is available in the [evidence appendix](../evidence/evidence-audit.md) and [machine-readable matrix](../evidence/evidence-matrix.tsv).

![Nested causal framework](../figures/fig1-framework.svg)

**Figure 1. A nested, falsifiable maintenance–reserve–gating model.** Solid edges summarize empirically supported relationships in at least one cited system; dashed edges are hypothesis-specific. $E(t)$ is measured exposure and $S(t)=h\{E(t);\theta\}$ is a derived score frozen without outcomes; the dashed $\phi:S\rightarrow X$ bridge is itself hypothetical. $X(t)$, $B(t)$, and the $R/P$ path are mechanistic hypotheses. $L(t)$ is a candidate factor measured by observed biomarkers, not a second causal substance. Evidence for an individual solid edge does not validate the complete path.

## 1. The unresolved timing problem

The minimal genetic model of an SCA is compelling:

$$
G \rightarrow D_G \rightarrow \text{neuronal dysfunction} \rightarrow \text{degeneration},
$$

where $G$ is the causal genotype and $D_G$ includes abnormal protein, RNA, ion-channel, transcriptional, calcium, proteostatic, or mitochondrial pressure. This model explains why the disease occurs. It does not, by itself, uniquely determine the individual timetable.

In a five-region cohort of 786 people with SCA3/MJD, expanded ATXN3 CAG length explained approximately 62% of age-at-onset variance [1]. That value is cohort-specific, not a universal constant. A 2026 study associated rare APOE ε4 homozygosity with onset about six years earlier in a Brazilian subgroup, but the signal was initial, subgroup-specific, and absent for common APOE contrasts [2]. In a four-family SCA6 series, two large families had stable 22- and 23-repeat expanded alleles, while the age at onset across affected participants was 24–63 years [3]. A study of only two monozygotic twin pairs—one SCA2 and one clinically diagnosed episodic ataxia type 2—reported quantitative discordance in eye movements, postural stability, severity, and regional involvement [4]. These observations justify looking for germline modifiers, somatic instability, stochastic biology, measurement error, and external influences. They do not identify a common environmental factor.

A broader causal description is therefore:

$$
\text{disease course}=f(G,\,G_{\mathrm{modifier}},\,\text{somatic change},\,\text{age},\,\text{environment},\,\text{reserve},\,\text{network state}).
$$

The proposal here asks whether the last four terms can sometimes be represented by a parsimonious dynamic mismatch model. It is deliberately nested inside known molecular pathology and competes with simpler alternatives.

## 2. From an unknown “factor” to an operational model

The phrase *external maintenance factor* can be misleading because it suggests that a single molecule has already been found. No such factor is known. The scientifically useful object is instead an **external maintenance input model** with six constrained elements.

### 2.1 Measured exposure $E(t)$

$E(t)$ contains observable quantities: geocoded residential histories linked to independently curated environmental records, water source, occupation, diet, infection, medication, physical activity, social conditions, and other measured variables. A confirmatory analysis may use only a prespecified candidate $E^*$, a fixed time window, and a fixed measurement rule. Untargeted exposome discovery is exploratory.

### 2.2 Derived exposure score $S(t)$ and hypothetical input $X(t)$

If several measured components are combined, the derived score must be declared before outcome analysis:

$$
S(t)=h\{E(t);\theta\},
$$

with fixed weights, lags, transformations, and missing-data rules. $S$ is observed or computable once the exposure data and mapping are frozen; its interpretation as a biological maintenance input is not observed. The latent input $X$ is therefore kept distinct. Any bridge,

$$
X(t)=\phi\{S(t);\psi\},
$$

must itself be prespecified and biologically justified. The illustrative convention $X=S$ used in Figure 2 is a model assumption, not an empirical finding. An unrestricted post-hoc $S$, $X$, $\phi$, or $\psi$ can fit almost any pattern and is scientifically empty. Failure cannot be rescued by redefining them after seeing the outcome.

### 2.3 Coupling $R$

$R$ denotes a genotype- and physiology-dependent tendency to activate or maintain a candidate module. It may be a vector, $\mathbf R=(R_1,\ldots,R_m)$, but confirmatory work should begin with a low-dimensional, independently measured quantity. $R$ cannot be defined as “high in people who develop disease early”; that would make the model circular. Until a valid external measurement is available, the testable proxy is a prespecified genotype-by-exposure interaction, not an inferred personal “level.”

### 2.4 Dynamic reserve $B(t)$

$B(t)$ is the only proposed mechanistic latent state. It represents the remaining capacity to absorb known pathogenic, ageing, and activity-dependent demands. It is not assumed to be one metabolite. The model predicts that clinical transition occurs when reserve crosses a threshold, but any biological interpretation must be tied to observable trajectories.

### 2.5 Biomarker state $L(t)$

$L(t)$ is a statistical measurement model:

$$
\mathbf Y(t)=\Lambda L(t)+\boldsymbol\epsilon(t),
$$

where $\mathbf Y(t)$ may include NfL, genotype-specific MRI/MRS, eye movements, electrophysiology, and digital gait. $L$ is not a second causal fluid or field. It is useful only if the factor structure is invariant enough across time and site, predicts future outcomes in held-out cohorts, and adds information beyond its component biomarkers.

This reduction matters. Without it, $S$, $X$, $R$, $B$, and $L$ can substitute for one another and the model becomes non-identifiable.

## 3. Minimal dynamics and the gating extension

For a single illustrative biological input, reserve dynamics can be written as:

$$
\frac{dB}{dt}=U\{X,P(X)\}-\mathcal L\{B,X,P(X)\}-M\{R,A(X)\}-D_G-D_{\mathrm{age}},
$$

where $U$ is uptake, $\mathcal L$ is outward loss, $M$ is activity-dependent consumption, and the final terms represent known genetic and ageing burdens. One possible gate is:

$$
P(X)=\frac{X^{n_P}}{K_P^{n_P}+X^{n_P}},
\qquad
A(X)=\frac{X^{n_A}}{K_A^{n_A}+X^{n_A}}.
$$

For multiple input classes $q$, uptake may depend on concentration $C_q$, uptake efficiency $\eta_q$, activation efficacy $a_{iq}$, and resource value $w_q$. The key theoretical condition is not a fixed “quality ratio,” but the possibility that activation rises faster than useful supply:

$$
a_{iq}\gg w_q \quad \text{over part of the exposure range}.
$$

In the source code for Figure 2, one dimensionless example uses:

$$
U=\eta PX,
$$

$$
\mathcal L=\lambda P\max(B-\kappa X,0),
$$

$$
M=m_0+m_1A(X),
$$

with a constant genetic/age drain. The parameters are chosen to display the hypothesized shape; they are not fitted to patients and have no dose interpretation. Figure 2 adopts $X=S$ solely to place the hypothetical dynamics on a visible standardized axis.

![Illustrative non-monotonic curve](../figures/fig2-nonlinear-gating.svg)

**Figure 2. A predicted non-monotonic response under one illustrative parameter set.** The horizontal axis is the hypothetical input $X$, and the plotted convention $X=S$ is used only for this illustration. At very low input, activation and exchange are small, producing an idle state with limited replenishment but limited activation-linked loss. At intermediate input, activation and outward loss can exceed uptake, creating maximal modeled depletion. At sufficiently high input, uptake dominates and net balance is restored. Every curve, boundary, and parameter is illustrative. No human SCA dataset currently demonstrates these four zones.

### 3.1 Four predicted regions

The gating extension predicts four qualitative regions:

- **Zone I, low-input idle:** $A\approx0$, $P\approx0$; there is little uptake but limited activation-linked loss.
- **Zone II, activation–supply mismatch:** activation and exchange increase before useful supply is sufficient; $dB/dt$ becomes most negative.
- **Zone III, partial supply:** uptake grows and depletion pressure falls, but reserve may still decline.
- **Zone IV, rebalancing:** uptake meets or exceeds aggregate loss; $dB/dt\ge0$ in the illustrative system.

The observed disease-risk function can therefore be hump-shaped, plateaued, or, with multiple input classes, multimodal. For an initial confirmatory study, however, a single prespecified central-versus-extremes contrast is more defensible than searching over arbitrary peak counts.

### 3.2 Identifiability and competing mechanisms

The same biomarker trajectory may result from low uptake, high consumption, high outward loss, or increasing $D_G$. Sparse observations cannot identify these processes separately. Identifiability requires perturbation, dense time series, external exposure calibration, or informative biological measurements. A statistical hump does not prove gating; it can arise from exposure misclassification, survivor selection, reverse causation, competing risks, mixtures of monotonic subgroups, or unmeasured confounding. These alternatives must be represented explicitly in a causal graph and sensitivity analyses.

### 3.3 What would distinguish gating from generic non-linearity?

The cohort's spline model can screen for a reproducible non-linear environmental association; it cannot by itself identify $P$, $B$, uptake, or leakage. A later gate-specific mechanistic substudy would need at least three independently measured axes: an activation marker $A$, an inward uptake or exchange proxy $U$, and a reserve/depletion proxy. The prespecified discriminating sequence is: intermediate $S$ first increases $A$ and exchange, $U$ fails to rise proportionally, and the reserve-proxy slope subsequently worsens before clinical change. A perturbation that selectively changes the proposed gate or activation process should then alter those ordered mediators and downstream biomarkers, with negative-control exposures and pathways remaining stable. Without this temporal and perturbational evidence, a hump plus genotype interaction supports only a non-linear environment model, not the proposed gate–leak mechanism.

## 4. What existing evidence does—and does not—support

### 4.1 Stage-dependent resilience is a plausible analogy

An SCA6 mouse study reported that ER/proteostasis stress and an HSP90-dependent unfolded-protein response preceded later hyperexcitability and motor impairment [5]. This is a useful analogy for early pathogenic pressure plus temporary resilience. It does not demonstrate a finite external reserve $B$. Moreover, the SCA6$^{84Q/+}$ model uses a repeat far longer than typical human SCA6 alleles, so translation requires caution.

In the Purkinje-cell-specific conditional SCA1[82Q] transgenic model, early suppression of mutant ATXN1 reversed measured pathology and motor impairment more fully than late suppression [6]. That establishes stage-dependent reversibility in that mouse model, not in human SCA generally.

### 4.2 Network and multicellular states can be causal

In Sca1 mice, molecular-layer interneuron hyperactivity preceded overt Purkinje neuron degeneration; chemogenetic suppression improved calcium signalling, delayed degeneration, and improved motor outcomes, whereas inducing related hyperactivity in healthy mice generated aspects of pathology [7]. This is the strongest experimental analogy for an early pathological “downshift.” The causal evidence is in mice, not in human cerebellar circuits.

Other experiments support a multicellular view. Bergmann-glia-specific disruption can produce non-cell-autonomous Purkinje-cell degeneration [8], and oligodendroglial mutant ATXN1 expression in mice can cause myelin abnormalities, Purkinje axonopathy, and motor impairment [9]. These findings make a systems-level state plausible; they do not imply that an external $X$ is required.

### 4.3 Excess signalling can be pathogenic, but direction is context-specific

A mouse model carrying the patient-associated GRM1 p.Y792C gain-of-function variant developed progressive motor and region-specific Purkinje-cell abnormalities [10]. A 2026 study of the moonwalker TRPC3 variant and the cerebellum-enriched Δ28 isoform found constitutive channel activity and calcium-dependent cell death in HEK293 cells; co-expression of Purkinje-enriched PMCA2 partly rescued survival in that cell system [11]. The latter was not an in-vivo Purkinje-cell rescue. Together, these studies show that “more activity” is not automatically beneficial. They do not establish a universal hyperactive subtype or justify blanket circuit inhibition.

### 4.4 Missing input can be restored in a defined knockout system

CBLN1–neurexin–GluD2 is a defined cerebellar synaptic-organizing system. Recombinant Cbln1 can rapidly restore aspects of parallel-fibre–Purkinje-cell synaptic organization in adult cbln1-null mice, and a later study reported transient improvement in selected gait measures [12,13]. This is a genuine missing-input rescue in a knockout model. It is not evidence for a common external factor in polyglutamine SCAs.

Likewise, purified human GluD2 reconstituted in artificial DPHPC lipid bilayers displayed D-serine- and GABA-gated currents [14]. Under 10 mM D-serine, reported open probability was $8.85\pm1.02\%$ at 37°C and $1.03\pm0.14\%$ at 22°C. Wild-type GluD2 currents remained difficult to observe in standard whole-cell expression conditions. This result demonstrates strong context dependence under a specific reductionist preparation; it neither validates $X$ nor makes every negative experiment uninformative.

### 4.5 Human biomarker readiness is uneven

NfL is elevated before manifest ataxia in SCA3 cohorts, including two multicentre cohorts in which abnormality was estimated several years before expected onset [15]. Longitudinal ESMI data in 291 carriers and 121 controls found stage-dependent changes in NfL and MRI, with pons volume showing high responsiveness across stages [16]. These results support trial enrichment and disease-activity measurement, but NfL and MRI are not established surrogate endpoints for clinical benefit.

A 2026 four-centre MRS study in 18 SCA2 participants, 25 SCA3 participants, and 29 controls found reproducible neurochemical differences over short retest intervals; estimates required site/vendor adjustment and differed by genotype [17]. It was not a presymptomatic longitudinal prediction study. MRS should therefore remain genotype-specific and generally secondary until responsiveness and clinical meaning are established.

### 4.6 Environmental evidence is exploratory

An exploratory study of 188 SCA3/MJD participants from 109 families associated municipality-level rural proxies with approximately 1.8 years earlier residual age at onset [18]. The variables were 2010 ecological proxies—population density, rural population proportion, and untreated-well-water proportion—rather than individual lifetime exposures. They were correlated, median-dichotomized, and only marginally significant. The study did not measure $S$ or $X$, establish causality, or test a non-monotonic dose curve. It motivates better exposure measurement; it does not support the gating mechanism.

### 4.7 Human neuromodulation evidence argues for restraint

A randomized crossover study of 20 people with mixed neurodegenerative ataxias reported clinical and physiological improvements after a cerebellar-anodal/spinal-cathodal montage [19]. A separate randomized study in 20 people with SCA3 found that two weeks of cerebellar anodal tDCS did not improve SARA or cerebellar brain inhibition relative to sham [20]. Neither study selected a validated hyperactive subtype, and anodal tDCS cannot be equated with biological “downshifting.” This mixed record supports phenotype-first target validation, not immediate therapeutic generalization.

## 5. Six falsifiable predictions

### Prediction 1: a preregistered non-monotonic contrast

For one independently measured and outcome-blind-derived $S^*$, the risk or disease-activity curve should show greater adverse association in a central exposure region than at both low and high reference regions. A significant quadratic term is insufficient. The confirmatory contrast is:

$$
C_{\mathrm{hump}}=f(S_{50})-\frac{f(S_{10})+f(S_{90})}{2}>0,
$$

with both directional components, simultaneous confidence intervals, and a peak inside a prespecified central range.

### Prediction 2: effect modification fixed before outcomes

The exposure association should differ between SCA3 and SCA6, or by an independently measured coupling variable. Until $R$ can be measured without outcomes, a genotype-by-$S^*$ interaction is the confirmatory test. A post-hoc “high-$R$” group derived from onset is prohibited.

### Prediction 3: temporal ordering after exposure change

Following a major migration or independently documented exposure shift, biomarker slopes should change before SARA. The design tests time-varying exposure with lags and negative-control windows; it does not assume immediate anatomical change.

### Prediction 4: pathological activity precedes structural loss

A reproducible human activity signature must precede, not merely accompany, subsequent MRI or clinical deterioration after adjustment for baseline disease stage. This is a prerequisite for any circuit-downshift study.

### Prediction 5: upstream intervention changes more than one axis

An intervention targeting a genuinely upstream module should produce coherent changes in target engagement, physiology, imaging or fluid disease activity, and later function. Improvement of one noisy endpoint alone is not sufficient.

### Prediction 6: external prediction rather than retrospective explanation

The latent biomarker state and any coupling score must improve calibration and prediction in sites or cohorts not used for model construction. Failure of measurement invariance, calibration, or external prediction rejects that implementation.

## 6. Prospective validation programme

The complete protocol and statistical analysis plan are provided separately: [prospective cohort](../protocols/prospective-cohort.md) and [SAP](../protocols/statistical-analysis-plan.md).

### 6.1 Population and follow-up

The confirmatory natural-history programme is a five-year, multicentre, family-aware cohort of genetically confirmed SCA3 and SCA6 expansion carriers, including preataxic participants with $\mathrm{SARA}<3$, early-manifest participants, and primarily expansion-negative relatives as controls. Clinical, NfL, ocular-motor, and digital measures occur every six months; remote gait sampling occurs every three months; structural/diffusion MRI is annual; genotype-specific MRS occurs at baseline, month 24, and month 60. Exposure history is collected independently from outcome assessors.

Phenoconversion is defined prospectively as the first visit with both $\mathrm{SARA}\ge3$ and a blinded expert rating of probable or definite manifest gait ataxia, confirmed at the next six-month visit. The primary time-to-event analysis uses age as the time scale, delayed entry, interval censoring, prespecified family/site structure, and competing-risk sensitivity analysis. Residual age at onset is descriptive only because it propagates error from a first-stage genetic prediction and can be distorted by ascertainment and survival.

### 6.2 Confirmatory exposure and multiplicity

Before outcome unblinding, an outcome-blind exposure panel applies a registered rubric to a finite two-candidate shortlist—five-year-lagged residential agricultural pesticide intensity and five-year-lagged untreated-private-well residence—and selects one measured operationalization $E^*$. Its rank-preserving, median/IQR-scaled analysis score $S^*=h(E^*;\theta)$ is frozen from exposure-only data; all confirmatory splines and interactions use $S^*$. The rubric uses only external plausibility, measurement reliability, data completeness, common support, and reproducible provenance, with frozen tie-breaks and no SCA outcomes. Both candidates are T4 operationalizations; neither $E^*$ nor $S^*$ is evidence for $X$. The nonselected candidate remains secondary. A lower observed risk at a high pesticide or untreated-well score would not imply benefit and must never motivate exposure escalation. Broad exposome scans remain exploratory with false-discovery-rate control.

Two confirmatory hypotheses—non-monotonicity and genotype interaction—share family-wise error via Holm adjustment. Restricted cubic splines and the central-versus-extremes contrast are locked. Internal–external validation leaves out sites or regions in turn; a separate cohort is preferred when available.

### 6.3 Sample-size logic

The cohort is event-driven. Under a simplified standardized continuous-exposure model, hazard ratio 1.5 per SD, two-sided alpha 0.025, 90% power, and covariate (R^2=0.30), a Schoenfeld-style approximation gives about 108 events. If 500 preataxic SCA3 and 300 preataxic SCA6 carriers have five-year conversion risks of 25% and 10%, respectively, with 85% retention, approximately 132 conversions are expected. That may support a main exposure analysis but is not robustly powered for a multi-degree-of-freedom genotype interaction. A planning expansion to 750 SCA3 and 450 SCA6 carriers under 35% and 15% conversion assumptions yields roughly 281 observed events. Final sizing requires simulation of interval censoring, family clustering, exposure error, site heterogeneity, and the locked spline. If recruitment stops near 800 preataxic carriers, genotype interaction is estimative or exploratory unless observed information justifies otherwise.

### 6.4 Latent biomarker state

The candidate $L(t)$ is built without SARA to prevent circular prediction. A longitudinal factor model uses NfL, genotype-specific MRI/MRS, ocular-motor physiology, and digital measures; it tests site/genotype measurement invariance, uses cross-validation, and then predicts phenoconversion and functional decline. The model is abandoned if it is unstable, merely reproduces NfL, or does not improve external prediction. Predictive gain for $L$ would validate only the measurement model; it would not identify mechanistic reserve $B$.

## 7. Early-intervention programme

The [trial protocol](../protocols/early-intervention-trial.md) deliberately separates SCA3 and SCA6. There is no biologically defensible common drug intervention and no pooled primary efficacy test.

![Prospective validation and trial gates](../figures/fig3-study-program.svg)

**Figure 3. Prospective validation and gated early-intervention programme.** A shared natural-history and measurement core feeds separate genotype/target-specific intervention modules. The SCA3 and SCA6 trials test known targets, not the unknown input. The circuit module stays inactive until prospective human evidence meets four gates. A failed cohort signal stops model escalation and cannot be repaired by redefining $S$, $X$, or $R$.

### 7.1 Conditional SCA3 mutant-ATXN3-lowering phase 2

Allele-specific ASO proof-of-concept in SCA3 patient iPSC-derived neurons reduced mutant ataxin-3 by about 80% for the tested linked-SNP strategy while largely preserving wild type [21]. This is an in-vitro, haplotype-limited result. VO659, a different CAG-repeat-targeting ASO strategy, is registered as an open-label phase 1/2a study in SCA1, SCA3, and Huntington disease; as of 7 August 2026 the registry lists recruitment but no posted results and no SCA efficacy conclusion [22].

Accordingly, the proposed SCA3 phase 2 activates only after an agent has SCA3-specific human safety, a recommended phase 2 dose, and CSF target engagement without concerning wild-type/total ATXN3, NfL, or MRI signals. Approximately 120 participants are randomized 1:1 to active drug or intrathecal placebo for 104 weeks. The co-primary endpoints must both succeed: week-26 change in CSF mutant ATXN3 and week-104 annualized pons-volume change. The central 40%-slowing scenario corresponds to about 120 randomized participants after 15% attrition; 30% slowing would need roughly 210 and 50% about 78. Simulation with agent-specific covariance replaces these approximations before launch.

Very-early-manifest SCA3 is enrolled first. Preataxic, biomarker-positive participants enter only after at least 12 early-manifest active recipients complete 26 weeks and the independent data monitoring committee supports expansion. Because intrathecal ASO exposure is not quickly reversible, this is better described as **dose-adjustable molecular lowering**, not a reversible circuit downshift.

### 7.2 SCA6 early-manifest L-arginine phase 2b

A 40-person phase 2 trial of L-arginine in SCA6 enrolled participants with SARA at least 10 (mean baseline approximately 15) and estimated a 48-week SARA difference of −1.52 points (95% CI −3.10 to 0.06; $p=0.0582$) [23]. The imprecision prevents an efficacy claim. Serious adverse events occurred in 2/20 active and 5/20 placebo participants; the fatal pneumonia and reversible liver abnormality in the active arm were classified as serious adverse reactions because causality could not be ruled out. A larger trial therefore needs a conservative effect assumption and enhanced safety monitoring.

The proposed trial randomizes up to 240 genetically confirmed early-manifest participants 1:1 to oral L-arginine or matched placebo for 72 weeks, followed by 12 weeks of blinded withdrawal. The first 40 randomized participants are restricted to SARA 10–12, overlapping the evidence-supported range. Prespecified numerical safety and blinded-feasibility gates then permit sequential expansion to SARA 5–9 and only later SARA 3–4. Final recruitment is capped at 80 participants per band, and the primary marginal effect uses fixed one-third band weights. Those earlier strata are untested populations with different floor, placebo-response, and safety uncertainty. Entry otherwise requires repeated qualifying SARA, disease duration no more than eight years, and ability to walk 10 m. The primary endpoint is the equally weighted mean of blinded SARA change at weeks 68 and 72. A one-point difference with SD 2.5 requires about 100 evaluable participants per arm; 15% attrition yields approximately 118 per arm, rounded to 120. A 0.75-point effect would require about 416 total, and 0.6 points about 646; the 240-person study therefore cannot exclude smaller effects.

Functional outcomes, patient global change, standardized video, digital gait, MRI/MRS, and NfL are secondary or exploratory. Neither NfL nor MRS substitutes for clinical benefit. Hepatic, renal, metabolic, aspiration, pneumonia, and adherence surveillance are explicit, with independent safety review.

### 7.3 Circuit-targeted phase 0

A circuit study is not currently ready. It activates only when all four conditions hold:

1. the human hyperactivity classifier has test–retest reliability $\mathrm{ICC}\ge0.75$;
2. the classifier prospectively precedes decline after stage adjustment;
3. the intervention moves the signature toward a healthy reference rather than imposing blanket inhibition; and
4. the physiological effect returns toward baseline within a prespecified 2–4 week washout without persistent loss.

The first primary endpoint is target engagement and washout reversibility, not SARA or disease modification. “Downshift” always means selective, reversible, pathology-specific modulation; it never means structural injury or destruction.

## 8. Nested model comparison

The hypothesis is evaluated against three nested models:

- **M0, known-mechanism model:** causal genotype, repeat length, age, sex, ancestry, site, family, measured known modifiers, disease stage, and established exposures.
- **M1, biomarker measurement model:** M0 plus the frozen, cross-validated biomarker state $L(t)$.
- **M2, non-linear environment model:** M1 plus the locked non-linear $S^*$ term and genotype-by-$S^*$ interaction.

M2 is retained only if it improves calibration and predictive performance in held-out sites or cohorts, reproduces the direction of the central-versus-extremes contrast, and survives exposure-error and selection-bias sensitivity analyses. A lower information criterion in the development data is not enough. M2 does not identify $P$, $B$, uptake, or leakage. Gate-specific language requires the independent activation–uptake–reserve sequence and perturbational evidence defined above.

## 9. Layer-specific falsification rules

Failure must be assigned to the layer actually tested:

1. **Registered exposure/score implementation ($E^*/S^*$):** it is rejected if adequately informative data exclude the prespecified hump, temporal ordering is compatible with reverse causation, or the frozen shape fails external replication. This does not by itself exclude every environmental influence.
2. **Coupling module ($R$):** the proposed genotype-dependent coupling is rejected if the genotype-by-$S^*$ interaction is adequately excluded and an independently defined $R$ adds no reproducible external information. A main environmental association could still remain.
3. **Biomarker measurement module ($L$):** the common factor is rejected if it fails longitudinal/genotype measurement invariance, calibration, or external prediction. This result neither proves nor disproves mechanistic reserve $B$.
4. **Circuit-downshift module:** it is rejected if a reproducible human high-activity signature never precedes deterioration, or if selective normalization produces target engagement but no downstream disease-activity signal in adequately powered studies. This does not decide the environmental model.
5. **Gate–loss mechanism:** it is rejected if independent activation, uptake/exchange, and reserve proxies do not show the registered temporal ordering, or if selective perturbation of the proposed gate fails to change those mediators despite adequate engagement. A statistical hump alone cannot rescue this mechanism.
6. **Need for the external-input layer:** the broader layer is rejected when externally validated models containing known DNA repair, somatic expansion, HSP90/UPR, calcium, mitochondrial, synaptic, glial, and behavioural mechanisms match or outperform it without $S\rightarrow X$ assumptions.

The current programme permits at most two candidate families: the outcome-blind-selected primary candidate and, only after a new registration in a non-overlapping external cohort, one test of the remaining shortlist candidate. The secondary result in the original cohort cannot promote it. Two adequately informative external failures end confirmatory expansion of this external-input model class; new candidates would require a visibly new hypothesis and protocol, not a post-hoc repair of this one.

## 10. Ethical and clinical boundaries

The unknown input has no established identity, dose, delivery route, or safety profile. Clinicians and patients must not administer X, unvalidated electromagnetic fields, radiation, supplements, drugs, neural injury, or gene manipulation on the basis of this hypothesis. Observational exposure research should minimize disclosure risk from residential histories and avoid stigmatizing rural communities. Genetic-carrier recruitment requires counselling, privacy protection, and jurisdiction-specific handling of incidental and predictive findings.

Trial concepts in this repository are not ready-to-use clinical orders. Each requires agent ownership, manufacturing and toxicology data, regulatory authorization, independent ethics review, trial registration, data monitoring, site qualification, and participant-informed consent. Concurrent randomized controls are essential; historical natural-history data may inform design but should not replace the primary control group.

## 11. Limitations

First, the framework is underdetermined: several flux combinations can generate the same reserve trajectory. Second, the proposed input score may collapse biologically unrelated exposures. Third, onset measures are noisy and influenced by diagnosis, recall, and access to care. Fourth, migration is selective and can induce time-varying confounding. Fifth, biomarkers differ by genotype, site, platform, renal function, infection, trauma, and disease stage. Sixth, rare-disease recruitment may be insufficient for flexible interactions. Seventh, the two proposed drug trials test early intervention in known pathways, not the external-input mechanism. Finally, the framework may prove unnecessary if established modifier mechanisms provide equal or better explanation.

## 12. Conclusion

The external maintenance factor–reserve–gating hypothesis is best treated as a constrained model class. Its value does not depend on asserting that a novel field or substance exists. It asks whether measured external exposures, genetic coupling, and finite homeostatic capacity produce a prospectively predictable, non-linear transition before advanced structural degeneration.

Current evidence supports onset heterogeneity, model-specific multicellular causation or plausibility in mice, early biomarker abnormalities in selected human cohorts, and stage-dependent resilience or partial reversibility in selected experimental systems. It does not support $X$, a gate, outward leakage, or a hump-shaped human risk curve. The decisive next step is therefore not speculative treatment. It is a preregistered cohort that can make the statistical implementation fail, followed—only where independently justified—by genotype- and target-specific randomized trials of known biology. If gate-specific temporal mediation and perturbation subsequently survive external tests, the mechanism will have earned attention. If they do not, the simpler explanation should replace it.

## Data, code, and reporting

This article contains no participant-level data. Figure source, deterministic sample-size scenarios, protocols, evidence audit, and repository checks are public in this repository. Trial concepts follow the logic of [SPIRIT 2025](https://www.bmj.com/content/389/bmj-2024-081477), [CONSORT 2025](https://www.bmj.com/content/389/bmj-2024-081123), and [ICH E9(R1)](https://www.ema.europa.eu/en/ich-e9-statistical-principles-clinical-trials-scientific-guideline), but they are not substitutes for a sponsor-approved final protocol or SAP.

AI-assisted tools were used for literature organization, drafting and editing, code generation, and internal consistency checks. They are not authors. The named author remains responsible for source verification, scientific claims, analyses, disclosures, and any submitted version.

## Competing interests and funding

Author-supplied competing-interest and funding declarations are not included in this repository version. They must be completed and reconfirmed by every author before journal submission.

## References

1. Akçimen F, et al. [Genome-wide association study identifies genetic factors that modify age at onset in Machado-Joseph disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138549/). *Aging*. 2020. doi:10.18632/aging.102825.
2. Meyer CC, et al. [Association of rare apolipoprotein E ε4 homozygosity with an earlier age at onset in spinocerebellar ataxia type 3](https://pubmed.ncbi.nlm.nih.gov/41854058/). *Human Molecular Genetics*. 2026. doi:10.1093/hmg/ddag016.
3. Gomez CM, et al. [Spinocerebellar ataxia type 6: variable age of onset](https://pubmed.ncbi.nlm.nih.gov/9403487/). *Ann Neurol*. 1997. doi:10.1002/ana.410420616.
4. Anderson JH, et al. [Spinocerebellar ataxia in monozygotic twins](https://pubmed.ncbi.nlm.nih.gov/12470184/). *Arch Neurol*. 2002. doi:10.1001/archneur.59.12.1945.
5. Huang H, et al. [Resilience to ER stress mitigates late membrane hyperexcitability in a murine SCA6 model](https://pmc.ncbi.nlm.nih.gov/articles/PMC12894513/). *Ann Neurol*. 2026. doi:10.1002/ana.78042.
6. Zu T, et al. [Recovery from polyglutamine-induced neurodegeneration in conditional SCA1 transgenic mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC6729947/). *J Neurosci*. 2004. doi:10.1523/JNEUROSCI.2978-04.2004.
7. Pilotto F, et al. [Early molecular layer interneuron hyperactivity triggers Purkinje neuron degeneration in SCA1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10431915/). *Neuron*. 2023. doi:10.1016/j.neuron.2023.05.016.
8. Wang X, et al. [Bergmann glia-specific loss of APC and non-cell-autonomous Purkinje-cell degeneration](https://pmc.ncbi.nlm.nih.gov/articles/PMC3287075/). *Glia*. 2011. doi:10.1002/glia.21154.
9. Lee C, et al. [Oligodendrocyte dysfunction contributes to motor deficits and Purkinje cell axonopathy in SCA1](https://www.jci.org/articles/view/195723). *J Clin Invest*. 2026. doi:10.1172/JCI195723.
10. Ibrahim MF, et al. [Enhanced mGluR1 function causes motor deficits and region-specific Purkinje cell dysfunction](https://pubmed.ncbi.nlm.nih.gov/41525334/). *Brain*. 2026. doi:10.1093/brain/awaf477.
11. Bell B, et al. [Functional and structural basis of a hypermorphic TRPC3 variant](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015894/). *Sci Adv*. 2026. doi:10.1126/sciadv.aec9284.
12. Ito-Ishida A, et al. [Cbln1 regulates rapid formation and maintenance of excitatory synapses](https://pmc.ncbi.nlm.nih.gov/articles/PMC6670322/). *J Neurosci*. 2008. doi:10.1523/JNEUROSCI.1030-08.2008.
13. Takeuchi E, et al. [Improvement of cerebellar ataxic gait by injecting Cbln1 into cbln1-null mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC5906462/). *Sci Rep*. 2018. doi:10.1038/s41598-018-24490-0.
14. Wang H, et al. [Delta-type glutamate receptors are ligand-gated ion channels](https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/). *Nature*. 2025. doi:10.1038/s41586-025-09610-x.
15. Wilke C, et al. [Neurofilaments in SCA3 at preataxic and ataxic stages](https://pubmed.ncbi.nlm.nih.gov/32510847/). *EMBO Mol Med*. 2020. doi:10.15252/emmm.201911803.
16. Berger M, et al. [Progression of biological markers in SCA3: longitudinal ESMI data](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270660/). *Lancet Reg Health Eur*. 2025. doi:10.1016/j.lanepe.2025.101339.
17. Joers JM, et al. [Neurochemical endpoints for early-stage SCA2/SCA3 trials in a multisite setting](https://pubmed.ncbi.nlm.nih.gov/42260718/). *Ann Clin Transl Neurol*. 2026. doi:10.1002/acn3.70443.
18. Martins AC, et al. [Rural environment as a risk factor for age at onset of Machado-Joseph disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC11998691/). *Mov Disord Clin Pract*. 2025. doi:10.1002/mdc3.14338.
19. Benussi A, et al. [Cerebello-spinal tDCS in ataxia](https://pubmed.ncbi.nlm.nih.gov/30135258/). *Neurology*. 2018. doi:10.1212/WNL.0000000000006210.
20. Maas RPPWM, et al. [Cerebellar tDCS in SCA3: randomized sham-controlled trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC9059914/). *Neurotherapeutics*. 2022. doi:10.1007/s13311-022-01231-w.
21. Hauser S, et al. [Allele-specific targeting of mutant ataxin-3 in SCA3 iPSC-derived neurons](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649108/). *Mol Ther Nucleic Acids*. 2022. doi:10.1016/j.omtn.2021.11.015.
22. ClinicalTrials.gov. [NCT05822908: VO659 in SCA1, SCA3 and Huntington disease](https://clinicaltrials.gov/study/NCT05822908). Status checked 7 August 2026.
23. Ishihara T, et al. [L-arginine in SCA6: multicentre randomized phase 2 trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701440/). *eClinicalMedicine*. 2024. doi:10.1016/j.eclinm.2024.102952.

The complete machine-readable bibliography is in [references.bib](references.bib).
