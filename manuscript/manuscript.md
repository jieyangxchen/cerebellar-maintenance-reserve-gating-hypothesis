# The Maintenance–Reserve–Gating Hypothesis of Hereditary Cerebellar Ataxia

## A testable model of non-linear modifier effects and delayed phenoconversion

**Proposed article category:** Hypothesis article for *Medical Hypotheses*

**Running title:** Maintenance–reserve–gating hypothesis in hereditary ataxia

**Author:** Jieyang Chen

**ORCID:** 0009-0001-9247-2085 ([profile](https://orcid.org/0009-0001-9247-2085))

**Manuscript version:** 0.3.0, 31 August 2026

**Evidence cut-off:** 19 August 2026

**Affiliation:** Independent Researcher, Hangzhou, China

**Correspondence:** [278404704@qq.com](mailto:278404704@qq.com)

**Public repository:** [https://github.com/jieyangxchen/cerebellar-maintenance-reserve-gating-hypothesis](https://github.com/jieyangxchen/cerebellar-maintenance-reserve-gating-hypothesis)

## Abstract

Pathogenic variants cause many spinocerebellar ataxias (SCAs), but they do not uniquely determine when carriers phenoconvert or how rapidly they progress. Established structural and functional cerebellar-reserve concepts explain how compensation can delay clinical expression. We propose a narrower extension: in some susceptible genotypes, a measured external exposure may activate demand or exchange before it supplies enough useful input to sustain the activated state, producing non-linear reserve depletion and delayed phenoconversion.

The hypothesis has two evidentiary layers. The directly testable layer separates measured exposure $E(t)$ from an outcome-blind, prospectively frozen score $S=h(E;\theta)$ and asks whether $S$ shows a reproducible non-linear association with phenoconversion and biomarker trajectories. The optional mechanistic layer posits an unidentified input $X(t)$, genotype-dependent coupling, activation/exchange gating, and dynamic reserve $B(t)$. A hump-shaped association would support only the first layer. The gating mechanism additionally requires independently measured activation, uptake/exchange, and reserve proxies to change in the predicted temporal order and to respond to selective perturbation.

Current human SCA evidence does not demonstrate $X$, a gate, outward loss, or a low-input idle–intermediate depletion–high-input rebalance curve. It supports only component premises: onset heterogeneity, cerebellar reserve, selected preataxic biomarkers, and model-specific multicellular causation or early reversibility. We specify prospective SCA3 testing, SCA6 transport testing, competing explanations, and layer-specific rejection rules. Failure of external replication, mediator ordering, or improvement over known-mechanism models rejects the corresponding layer. This is a testable etiological hypothesis, not a treatment recommendation.

**Keywords:** Spinocerebellar Ataxias; Cerebellum; Environmental Exposure; Disease Progression; Biomarkers; Genetic Predisposition to Disease

## Hypothesis and evidentiary boundary

Some hereditary cerebellar ataxias may contain a mismatch between genetic demand, externally conditioned activation, and dynamic reserve. The unidentified-input extension earns causal status only if it predicts new data, produces the specified mediator order, and survives selective perturbation better than known-mechanism models.

We separate claims into four levels:

1. **Established observation:** directly supported in the cited population or model.
2. **Supported analogy:** demonstrates biological plausibility of one component, but not this model.
3. **Testable inference:** prospectively operationalized and capable of failure.
4. **Speculation:** motivates research but has no direct evidentiary support.

The complete claim-by-claim audit is available in the [evidence appendix](../evidence/evidence-audit.md) and [machine-readable matrix](../evidence/evidence-matrix.tsv). The nested architecture and evidentiary boundary are summarized in Fig. 1.

![Nested causal framework](../figures/fig1-framework.svg)

**Fig. 1** A nested, falsifiable maintenance–reserve–gating model. Solid edges summarize empirically supported relationships in at least one cited system; dashed edges are hypothesis-specific. $E(t)$ is measured exposure and $S(t)=h\{E(t);\theta\}$ is a derived score frozen without outcomes; the dashed $\phi:S\rightarrow X$ bridge is itself hypothetical. $X(t)$, $B(t)$, and the $R/P$ path are mechanistic hypotheses. $L(t)$ is a candidate factor measured by observed biomarkers, not a second causal substance. Evidence for an individual solid edge does not validate the complete path. $D_G$, genotype-linked pathogenic pressure; ER, endoplasmic reticulum; MLIN, molecular-layer interneuron; NfL, neurofilament light chain; MRI, magnetic resonance imaging; MRS, magnetic resonance spectroscopy

## 1. The unresolved timing problem

The minimal genetic model of a spinocerebellar ataxia (SCA) is compelling:

$$
G \rightarrow D_G \rightarrow \text{neuronal dysfunction} \rightarrow \text{degeneration},
$$

where $G$ is the causal genotype and $D_G$ includes abnormal protein, RNA, ion-channel, transcriptional, calcium, proteostatic, or mitochondrial pressure. This model explains why the disease occurs. It does not, by itself, uniquely determine the individual timetable.

In a five-region cohort of 786 people with SCA3/Machado–Joseph disease (MJD), expanded ATXN3 CAG length explained approximately 62% of age-at-onset variance [1]. That value is cohort-specific, not a universal constant. A 2026 study associated rare APOE ε4 homozygosity with onset about six years earlier in a Brazilian subgroup, but the signal was initial, subgroup-specific, and absent for common APOE contrasts [2]. In a four-family SCA6 series, two large families had stable 22- and 23-repeat expanded alleles, while the age at onset across affected participants was 24–63 years [3]. A study of only two monozygotic twin pairs—one SCA2 and one clinically diagnosed episodic ataxia type 2—reported quantitative discordance in eye movements, postural stability, severity, and regional involvement [4]. These observations justify looking for germline modifiers, somatic instability, stochastic biology, measurement error, and external influences. They do not identify a common environmental factor.

A broader causal description is therefore:

$$
\text{disease course}=f(G,\,G_{\mathrm{modifier}},\,\text{somatic change},\,\text{age},\,\text{environment},\,\text{reserve},\,\text{network state}).
$$

The proposal here asks whether the last four terms can sometimes be represented by a parsimonious dynamic mismatch model. It is deliberately nested inside known molecular pathology and competes with simpler alternatives.

## 2. Relation to established concepts of cerebellar reserve

The term *cerebellar reserve* already has a defined scientific lineage. A consensus framework distinguishes structural reserve—the ability of spared cerebellar or extracerebellar systems to compensate for focal injury—from functional reserve within gradually affected cerebellar tissue [5]. It treats reserve as a moderator between pathology and clinical outcome and emphasizes plasticity, environmental enrichment, and the possibility of compensation or restoration while functional circuitry remains available. The related “Time Is Cerebellum” principle argues that treatment is most likely to preserve function before advanced cell loss [6].

The present framework builds on, rather than replaces, those concepts. Its proposed $B(t)$ is narrower and more speculative: a dynamic state whose trajectory is determined by known pathogenic pressure, ageing, activity-dependent demand, and candidate input-related fluxes. It is not a synonym for neuron count, cognitive reserve, synaptic plasticity, or an established biomarker. If observed biomarkers can be explained fully by existing structural or functional reserve without the proposed input-dependent dynamics, the new layer is unnecessary.

The distinctive claim is therefore not that reserve exists. It is that, for a prespecified input and susceptible genotype, activation and exchange could rise before useful supply, producing a directional non-monotonic prediction and an ordered mediator sequence. Those additional claims must fail independently of the broader cerebellar-reserve concept.

## 3. A two-layer operational framework

We avoid the phrase *external maintenance factor* because it suggests that a molecule or field has already been found. No such entity is known. The testable framework separates an observable modifier layer from an optional mechanistic extension.

### 3.1 Observable modifier layer: $E(t)$ and $S(t)$

$E(t)$ contains observable quantities: geocoded residential histories linked to independently curated environmental records, water source, occupation, diet, infection, medication, physical activity, social conditions, and other measured variables. A confirmatory analysis may use only a prespecified candidate $E^*$, fixed time window, and fixed measurement rule. Untargeted exposome discovery is exploratory.

If several measured components are combined, the derived score must be declared before outcome analysis:

$$
S(t)=h\{E(t);\theta\},
$$

with fixed weights, lags, transformations, and missing-data rules. $S$ is observed or computable once the exposure data and mapping are frozen. The first layer tests only whether $S$ improves externally validated prediction or shows the prespecified association with phenoconversion and biomarker change. It does not require $S$ to be a nutrient, beneficial exposure, or direct measure of a maintenance substance.

### 3.2 Mechanistic extension: $X(t)$ and the $S\rightarrow X$ bridge

The biological input $X$ remains hypothetical and distinct from $S$. Any bridge,

$$
X(t)=\phi\{S(t);\psi\},
$$

must itself be prespecified, biologically calibrated, and tested independently of clinical outcomes. The illustrative convention $X=S$ used in Fig. 2 is a model assumption, not an empirical finding. An unrestricted post-hoc $S$, $X$, $\phi$, or $\psi$ can fit almost any pattern and is scientifically empty. Failure cannot be rescued by redefining them after seeing the outcome.

### 3.3 Coupling $R$

$R$ denotes a genotype- and physiology-dependent tendency to activate or maintain a candidate module. It may be a vector, $\mathbf R=(R_1,\ldots,R_m)$, but confirmatory work should begin with a low-dimensional, independently measured quantity. $R$ cannot be defined as “high in people who develop disease early”; that would make the model circular. Until a valid external measurement is available, the testable proxy is a prespecified genotype-by-exposure interaction, not an inferred personal “level.”

### 3.4 Dynamic reserve $B(t)$ and clinical transition

$B(t)$ is the only proposed mechanistic latent state. It represents the remaining capacity to absorb known pathogenic, ageing, and activity-dependent demands. It is not assumed to be one metabolite. To connect reserve dynamics to the cohort outcome, the simplest threshold observation model is:

$$
T_{\mathrm{conversion}}=\inf\{t:B(t)\le B_c\}.
$$

A smoother alternative links lower reserve to higher instantaneous risk:

$$
\lambda(t\mid B)=\lambda_0(t)\exp\left[\gamma\{B_c-B(t)\}_+\right],\qquad \gamma>0.
$$

These are competing observation models, not established biology. They make explicit that a non-monotonic depletion rate does not automatically imply a non-monotonic clinical hazard: the result also depends on baseline reserve, exposure history, genetic burden, censoring, and survival. A registered analysis must simulate and distinguish those links before treating a clinical hump as a prediction of the reserve equation.

### 3.5 Biomarker state $L(t)$

$L(t)$ is a statistical measurement model:

$$
\mathbf Y(t)=\Lambda L(t)+\boldsymbol\epsilon(t),
$$

where $\mathbf Y(t)$ may include neurofilament light chain (NfL), genotype-specific magnetic resonance imaging (MRI) and magnetic resonance spectroscopy (MRS), eye movements, electrophysiology, and digital gait. $L$ is not a second causal fluid or field. It is useful only if the factor structure is invariant enough across time and site, predicts future outcomes in held-out cohorts, and adds information beyond its component biomarkers.

This reduction matters. Without it, $S$, $X$, $R$, $B$, and $L$ can substitute for one another and the model becomes non-identifiable.

## 4. Minimal dynamics and the gating extension

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

For multiple input classes $q$, uptake may depend on concentration $C_q$, uptake efficiency $\eta_q$, activation efficacy, and resource value. After normalization to candidate-specific reference scales, write the activation and useful-supply responses as $\widetilde A_i(\widetilde X)$ and $\widetilde U_q(\widetilde X)$. The key theoretical condition is not a dimensionally ambiguous fixed “quality ratio,” but a prespecified interval in which activation gain exceeds useful-supply gain:

$$
\frac{d\widetilde A_i}{d\widetilde X}>
\frac{d\widetilde U_q}{d\widetilde X}.
$$

The normalization, comparison interval, and candidate-specific measurements must be declared before outcome analysis.

In the source code for Fig. 2, one dimensionless example uses:

$$
U=\eta PX,
$$

$$
\mathcal L=\lambda P\max(B-\kappa X,0),
$$

$$
M=m_0+m_1A(X),
$$

with a constant genetic/age drain. We chose the parameters to display the hypothesized shape; they are not fitted to patients and have no dose interpretation. Fig. 2 adopts $X=S$ solely to place the hypothetical dynamics on a visible standardized axis.

The proposed shape is not a generic consequence of a Hill gate. It requires at least three qualitative conditions over the comparison interval:

1. at low $X$, activation and exchange are sufficiently small that activation-linked demand and outward loss remain limited relative to the comparison states;
2. over an intermediate range, the increase in $M+\mathcal L$ exceeds the increase in useful uptake $U$; and
3. at high $X$, uptake eventually meets or exceeds combined activity-dependent demand, loss, and the genetic/ageing drain.

If the first condition fails, low input may be the most harmful state. If the second fails, no intermediate depletion maximum occurs. If the third fails, the curve remains monotonic or plateaus without rebalancing. Parameter sweeps and exposure-history simulations are therefore required before a candidate implementation can claim that a hump is robust rather than hand-selected.

The resulting low-input idle, intermediate depletion, and high-input rebalance pattern is shown in Fig. 2.

![Illustrative non-monotonic curve](../figures/fig2-nonlinear-gating.svg)

**Fig. 2** A predicted non-monotonic response under one illustrative parameter set. The horizontal axis is the hypothetical input $X$, and the plotted convention $X=S$ is used only for this illustration. At very low input, activation and exchange are small, producing an idle state with limited replenishment but limited activation-linked loss. At intermediate input, activation and outward loss can exceed uptake, creating maximal modeled depletion. At sufficiently high input, uptake dominates and net balance is restored. Every curve, boundary, and parameter is illustrative. The human SCA evidence reviewed here does not demonstrate these four zones

### 4.1 Four predicted regions

The gating extension predicts four qualitative regions:

- **Zone I, low-input idle:** $A\approx0$, $P\approx0$; there is little uptake but limited activation-linked loss.
- **Zone II, activation–supply mismatch:** activation and exchange increase before useful supply is sufficient; $dB/dt$ becomes most negative.
- **Zone III, partial supply:** uptake grows and depletion pressure falls, but reserve may still decline.
- **Zone IV, rebalancing:** uptake meets or exceeds aggregate loss; $dB/dt\ge0$ in the illustrative system.

Under the threshold or hazard observation model, the observed disease-risk function can be hump-shaped, plateaued, monotonic, or, with multiple input classes, multimodal. A central-versus-extremes contrast is a disciplined first implementation, not proof that the biological peak must occur at the sample median. A mechanistically calibrated threshold would be preferable to quantile placement when a validated activation or uptake marker becomes available.

### 4.2 Identifiability and competing mechanisms

The same biomarker trajectory may result from low uptake, high consumption, high outward loss, or increasing $D_G$. Sparse observations cannot identify these processes separately. Identifiability requires perturbation, dense time series, external exposure calibration, or informative biological measurements. A statistical hump does not prove gating; it can arise from exposure misclassification, survivor selection, reverse causation, competing risks, mixtures of monotonic subgroups, or unmeasured confounding. These alternatives must be represented explicitly in a causal graph and sensitivity analyses.

### 4.3 What would distinguish gating from generic non-linearity?

The cohort's spline model can screen for a reproducible non-linear environmental association; it cannot by itself identify $P$, $B$, uptake, or outward loss. A later gate-specific mechanistic substudy would need at least three independently measured axes: an activation marker $A$, an inward uptake or exchange proxy $U$, and a reserve/depletion proxy. The prespecified discriminating sequence is: intermediate $S$ first increases $A$ and exchange, $U$ fails to rise proportionally, and the reserve-proxy slope subsequently worsens before clinical change. A perturbation that selectively changes the proposed gate or activation process should then alter those ordered mediators and downstream biomarkers, with negative-control exposures and pathways remaining stable. Without this temporal and perturbational evidence, a hump plus genotype interaction supports only a non-linear environment model, not the proposed gate–loss mechanism.

## 5. What existing evidence does—and does not—support

### 5.1 Stage-dependent resilience is a plausible analogy

An SCA6 mouse study reported that endoplasmic reticulum (ER)/proteostasis stress and an HSP90-dependent unfolded-protein response preceded later hyperexcitability and motor impairment [7]. This is a useful analogy for early pathogenic pressure plus temporary resilience. It does not demonstrate a finite external reserve $B$. Moreover, the SCA6$^{84Q/+}$ model uses a repeat far longer than typical human SCA6 alleles, so translation requires caution.

In the Purkinje-cell-specific conditional SCA1[82Q] transgenic model, early suppression of mutant ATXN1 reversed measured pathology and motor impairment more fully than late suppression [8]. That establishes stage-dependent reversibility in that mouse model, not in human SCA generally.

### 5.2 Network and multicellular states can be causal

In Sca1 mice, molecular-layer interneuron (MLIN) hyperactivity preceded overt Purkinje neuron degeneration; chemogenetic suppression improved calcium signalling, delayed degeneration, and improved motor outcomes, whereas inducing related hyperactivity in healthy mice generated aspects of pathology [9]. This is the strongest experimental analogy for an early pathological “downshift.” The causal evidence is in mice, not in human cerebellar circuits.

Other experiments support a multicellular view. Bergmann-glia-specific disruption can produce non-cell-autonomous Purkinje-cell degeneration [10], and oligodendroglial mutant ATXN1 expression in mice can cause myelin abnormalities, Purkinje axonopathy, and motor impairment [11]. These findings make a systems-level state plausible; they do not imply that an external $X$ is required.

### 5.3 Excess signalling can be pathogenic, but direction is context-specific

A mouse model carrying the patient-associated GRM1 p.Y792C gain-of-function variant developed progressive motor and region-specific Purkinje-cell abnormalities [12]. A 2026 study of the moonwalker TRPC3 variant and the cerebellum-enriched Δ28 isoform found constitutive channel activity and calcium-dependent cell death in human embryonic kidney 293 (HEK293) cells; co-expression of Purkinje-enriched plasma-membrane Ca²⁺-ATPase 2 (PMCA2) partly rescued survival in that cell system [13]. The latter was not an in-vivo Purkinje-cell rescue. Together, these studies show that “more activity” is not automatically beneficial. They do not establish a universal hyperactive subtype or justify blanket circuit inhibition.

### 5.4 Missing input can be restored in a defined knockout system

CBLN1–neurexin–GluD2 is a defined cerebellar synaptic-organizing system. Recombinant Cbln1 can rapidly restore aspects of parallel-fibre–Purkinje-cell synaptic organization in adult cbln1-null mice, and a later study reported transient improvement in selected gait measures [14,15]. This is a genuine missing-input rescue in a knockout model. It is not evidence for a common external factor in polyglutamine SCAs.

Likewise, purified human GluD2 reconstituted in artificial 1,2-diphytanoyl-sn-glycero-3-phosphocholine (DPHPC) lipid bilayers displayed D-serine- and γ-aminobutyric acid (GABA)-gated currents [16]. Under 10 mM D-serine, reported open probability was $8.85\pm1.02\%$ at 37°C and $1.03\pm0.14\%$ at 22°C. Wild-type GluD2 currents remained difficult to observe in standard whole-cell expression conditions. This result demonstrates strong context dependence under a specific reductionist preparation; it neither validates $X$ nor makes every negative experiment uninformative.

### 5.5 Human biomarker readiness is uneven

NfL is elevated before manifest ataxia in SCA3 cohorts, including two multicentre cohorts in which abnormality was estimated several years before expected onset [17]. Longitudinal data from a multicentre cohort of 291 carriers and 121 controls showed stage-dependent changes in NfL and MRI, with pons volume showing high responsiveness across stages [18]. These results support trial enrichment and disease-activity measurement, but NfL and MRI are not established surrogate endpoints for clinical benefit.

A 2026 four-centre MRS study in 18 SCA2 participants, 25 SCA3 participants, and 29 controls found reproducible neurochemical differences over short retest intervals; estimates required site/vendor adjustment and differed by genotype [19]. It was not a preataxic longitudinal prediction study. MRS should therefore remain genotype-specific and generally secondary until responsiveness and clinical meaning are established.

A 2026 Ataxia Global Initiative consensus statement provided disease-specific recommendations for quantitative MRI endpoints in SCA1, SCA2, and SCA3 and emphasized their potential role in participant selection and monitoring for early trials [26]. This strengthens the rationale for a harmonized imaging core, but a consensus recommendation does not make MRI a validated surrogate for clinical benefit.

### 5.6 Environmental evidence is exploratory

An exploratory analysis found that municipality-level rural proxies were associated with approximately 1.8 years earlier residual age at onset among 188 SCA3/MJD participants from 109 families [20]. The variables were 2010 ecological proxies—population density, rural population proportion, and untreated-well-water proportion—rather than individual lifetime exposures. They were correlated, median-dichotomized, and only marginally significant. The study did not measure $S$ or $X$, establish causality, or test a non-monotonic dose curve. It motivates better exposure measurement; it does not support the gating mechanism.

### 5.7 Human neuromodulation evidence argues for restraint

A randomized crossover study of 20 people with mixed neurodegenerative ataxias reported clinical and physiological improvements after a cerebellar-anodal/spinal-cathodal transcranial direct-current stimulation (tDCS) montage [21]. A separate randomized study in 20 people with SCA3 found that two weeks of cerebellar anodal tDCS did not improve the Scale for the Assessment and Rating of Ataxia (SARA) or cerebellar brain inhibition relative to sham [22]. Neither study selected a validated hyperactive subtype, and anodal tDCS cannot be equated with biological “downshifting.” This mixed record supports phenotype-first target validation, not immediate therapeutic generalization.

## 6. Six falsifiable predictions

### Prediction 1: a preregistered non-monotonic contrast

For one independently measured and outcome-blind-derived $S^*$, the risk or disease-activity curve should show greater adverse association in a central exposure region than at both low and high reference regions. A significant quadratic term is insufficient. The confirmatory contrast is:

$$
C_{\mathrm{hump}}=f(S_{50})-\frac{f(S_{10})+f(S_{90})}{2}>0,
$$

with both directional components, simultaneous confidence intervals, and a peak inside a prespecified central range.

For the primary SCA3 phenoconversion analysis, $f$ is the prespecified fitted log-hazard curve. Any use of this contrast for a biomarker or functional outcome requires a separately frozen outcome scale and model.

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

## 7. Prospective validation programme

The public repository identified on the title page contains the complete prospective-cohort protocol, statistical analysis plan, and early-intervention concepts. The manuscript retains only the decisions needed to make the hypothesis falsifiable.

### 7.1 SCA3 test bed and SCA6 transport test

The primary test is an event-driven, multicentre, family-aware cohort of genetically confirmed preataxic and early-manifest SCA3 carriers. SCA3 is the first test bed because the motivating rural-environment analysis was SCA3-specific and human phenoconversion data are comparatively mature. SCA6 is a deliberately difficult transport test across a distinct channelopathy; it is not assumed to share the same exposure curve or coupling. Expansion-negative relatives provide the preferred control group where feasible.

Before outcome access, an independent exposure panel applies a registered rubric to a finite candidate list and freezes one measured exposure $E^*$, its lag, spatial rule, and score $S^*=h(E^*;\theta)$. The primary endpoint is prospectively defined phenoconversion, analyzed with age as the time scale, delayed entry, interval censoring, family/site structure, and competing-risk sensitivity analyses. The confirmatory model compares the locked spline and central-versus-extremes contrast against a known-mechanism model, then tests calibration in held-out sites and a geographically separate SCA3 cohort. SCA6 tests transport only after the SCA3 implementation is frozen.

The motivating pesticide-intensity and untreated-private-well measures are exposure proxies, not maintenance resources or measurements of $X$. Any lower estimated risk at high exposure requires analyses of exposure error, selection, survivor bias, and unmeasured confounding; it cannot be interpreted as beneficial exposure or justify escalation.

### 7.2 Biomarker and information requirements

Clinical, neurofilament light chain (NfL), ocular-motor, digital gait, structural MRI, and genotype-specific MRS measurements provide longitudinal outcomes. A candidate biomarker factor $L(t)$ is constructed without SARA, tested for site/genotype measurement invariance, and evaluated only on future prediction. It is rejected if it is unstable, merely reproduces NfL, or does not improve external calibration.

The cohort is event-driven rather than fixed by an optimistic interaction effect. A simplified benchmark requires approximately 108 phenoconversions for a hazard ratio of 1.5 per standard deviation, 90% power, two-sided alpha 0.025, and covariate $R^2=0.30$. The repository's illustrative 800-carrier scenario yields approximately 132 conversions under stated assumptions—potentially enough for an SCA3-led exposure estimate if common support is adequate, but not robust evidence for a flexible genotype interaction. Final sizing requires frozen simulation of interval censoring, clustering, exposure error, site heterogeneity, and genotype-specific support.

## 8. Early-intervention implications of known biology

The repository's trial concepts deliberately separate SCA3 and SCA6. They illustrate early modifiability of known targets; they neither test nor validate $X$, $P$, or the proposed reserve fluxes. There is no biologically defensible common drug intervention or pooled efficacy test. Fig. 3 summarizes the separation between natural-history testing and later target-specific intervention.

![Prospective validation and trial gates](../figures/fig3-study-program.svg)

**Fig. 3** Prospective validation and gated early-intervention programme. A shared natural-history and measurement core feeds separate genotype- and target-specific examples. The SCA3 and SCA6 concepts test known targets, not the unknown input. The circuit module stays inactive until prospective human evidence meets four gates. A failed cohort signal stops model escalation and cannot be repaired by redefining $S$, $X$, or $R$. 5-y, five-year; CSF, cerebrospinal fluid; f-SARA, functional SARA; $G\times S^*$, genotype-by-score interaction; H1, prespecified SCA3 hump contrast; NfL, neurofilament light chain; MRI, magnetic resonance imaging; MRS, magnetic resonance spectroscopy; PRO, patient-reported outcome; SARA, Scale for the Assessment and Rating of Ataxia; SCA, spinocerebellar ataxia

Allele-specific antisense-oligonucleotide proof of concept in SCA3 patient-derived neurons and an ongoing CAG-repeat-targeting clinical programme justify target-engagement-led development, but neither establishes clinical benefit [23,24]. A small SCA6 L-arginine trial produced an imprecise 48-week estimate and does not support a shared maintenance input [25]. These examples illustrate why genotype-specific known-target trials should remain separate from tests of the environmental hypothesis.

A circuit-targeted phase 0 study is not currently justified. It should proceed only after a reproducible human activity signature shows test–retest reliability, precedes decline after stage adjustment, can be moved toward a healthy reference without blanket inhibition, and returns toward baseline during a prespecified washout. Its first endpoint would be target engagement and reversibility, not clinical efficacy. “Downshift” means selective, reversible, pathology-specific modulation; it never means structural injury.

## 9. Nested model comparison

We evaluate the hypothesis against three nested models:

- **M0, known-mechanism model:** causal genotype, repeat length, age, sex, ancestry, site, family, measured known modifiers, disease stage, and established exposures.
- **M1, biomarker measurement model:** M0 plus the frozen, cross-validated biomarker state $L(t)$.
- **M2, non-linear environment model:** M1 plus the locked non-linear $S^*$ term and genotype-by-$S^*$ interaction.

These are prospective prediction models, not a causal adjustment sequence. Only biomarker information measured before the prediction horizon may enter $L$, and the primary H1 total-association analysis is estimated separately without conditioning on a potentially mediating $L$.

M2 is retained only if it improves calibration and predictive performance in held-out sites or cohorts, reproduces the direction of the central-versus-extremes contrast, and survives exposure-error and selection-bias sensitivity analyses. A lower information criterion in the development data is not enough. M2 does not identify $P$, $B$, uptake, or outward loss. Gate-specific language requires the independent activation–uptake–reserve sequence and perturbational evidence defined above.

## 10. Layer-specific falsification rules

Failure must be assigned to the layer actually tested:

1. **Registered exposure/score implementation ($E^*/S^*$):** it is rejected if adequately informative data exclude the prespecified hump, temporal ordering is compatible with reverse causation, or the frozen shape fails external replication. This does not by itself exclude every environmental influence.
2. **Coupling module ($R$):** the proposed genotype-dependent coupling is rejected if the genotype-by-$S^*$ interaction is adequately excluded and an independently defined $R$ adds no reproducible external information. A main environmental association could still remain.
3. **Biomarker measurement module ($L$):** the common factor is rejected if it fails longitudinal/genotype measurement invariance, calibration, or external prediction. This result neither proves nor disproves mechanistic reserve $B$.
4. **Circuit-downshift module:** it is rejected if a reproducible human high-activity signature never precedes deterioration, or if selective normalization produces target engagement but no downstream disease-activity signal in adequately powered studies. This does not decide the environmental model.
5. **Gate–loss mechanism:** it is rejected if independent activation, uptake/exchange, and reserve proxies do not show the registered temporal ordering, or if selective perturbation of the proposed gate fails to change those mediators despite adequate engagement. A statistical hump alone cannot rescue this mechanism.
6. **Need for the external-input layer:** the broader layer is rejected when externally validated models containing known DNA repair, somatic expansion, established cerebellar reserve, HSP90-dependent unfolded-protein response, calcium, mitochondrial, synaptic, glial, and behavioural mechanisms match or outperform it without $S\rightarrow X$ assumptions.

The current programme permits at most two candidate families: the outcome-blind-selected primary candidate and, only after a new registration in a non-overlapping external cohort, one test of the remaining shortlist candidate. The secondary result in the original cohort cannot promote it. Two adequately informative external failures end confirmatory expansion of this external-input model class; new candidates would require a visibly new hypothesis and protocol, not a post-hoc repair of this one.

## 11. Ethical and clinical boundaries

The unknown input has no established identity, dose, delivery route, or safety profile. Clinicians and patients must not administer X, unvalidated electromagnetic fields, radiation, supplements, drugs, neural injury, or gene manipulation based on this hypothesis. Observational exposure research should minimize disclosure risk from residential histories and avoid stigmatizing rural communities. Genetic-carrier recruitment requires counselling, privacy protection, and jurisdiction-specific handling of incidental and predictive findings.

Trial concepts in this repository are not ready-to-use clinical orders. Each requires agent ownership, manufacturing and toxicology data, regulatory authorization, independent ethics review, trial registration, data monitoring, site qualification, and participant-informed consent. Concurrent randomized controls are essential; historical natural-history data may inform design but should not replace the primary control group.

## 12. Limitations

First, the framework is underdetermined: several flux combinations can generate the same reserve trajectory. Second, a hand-selected parameter set can display a hump even when the shape is not robust; candidate-specific parameter sweeps and exposure-history simulations are still required. Third, the proposed input score may collapse biologically unrelated exposures, and the current rural proxies are not direct measures of a maintenance resource. Fourth, the link from reserve to clinical transition is itself a model choice. Fifth, onset measures are noisy and influenced by diagnosis, recall, and access to care, while migration and survival can induce time-varying confounding and selection. Sixth, biomarkers differ by genotype, site, platform, renal function, infection, trauma, and disease stage. Seventh, rare-disease recruitment may be insufficient for flexible interactions, especially in SCA6. Eighth, the drug examples test early intervention in known pathways, not the external-input mechanism. Finally, the framework may prove unnecessary if established modifier and cerebellar-reserve mechanisms provide equal or better explanation.

## 13. Conclusion

The maintenance–reserve–gating hypothesis is a constrained model class nested within established cerebellar-reserve theory. Its value does not depend on asserting that a novel field or substance exists. It asks whether measured external exposures, genotype, and dynamic homeostatic capacity produce a prospectively predictable, non-linear transition before advanced structural degeneration.

Current evidence supports onset heterogeneity, established structural and functional cerebellar reserve, early biomarker abnormalities in selected human cohorts, and model-specific multicellular causation or stage-dependent reversibility. It does not support $X$, a gate, outward loss, or a hump-shaped human risk curve. The decisive next step is an SCA3-led, preregistered test of one reliably measured exposure, followed by external replication and SCA6 transport testing. Gate-specific language requires an independent activation–uptake–reserve sequence and perturbation. If those tests fail, existing reserve and known molecular mechanisms should replace the added layer.

## Declarations

### Data and code availability

No participant-level or experimental data are associated with this article. Figure source, deterministic sample-size scenarios, protocols, evidence audit, and repository checks are public in the repository identified on the title page. The figures were generated programmatically with Python and Matplotlib; source code and vector exports are provided in that repository. The research-planning documents are not substitutes for sponsor-approved protocols or statistical analysis plans.

### Ethics approval and consent

Not applicable. This article is a hypothesis and critical review and reports no research involving human participants, animals, participant data, or biological material.

### Author contribution

Jieyang Chen conceived the hypothesis, performed the literature organization and claim audit, designed the proposed research programme, prepared the figures and reproducibility materials, and drafted and revised the manuscript.

### Acknowledgements

None.

### Funding

This work received no external funding.

### Competing interests

The author declares no competing interests. The author retains copyright in the associated public repository and may consider future commercial-licensing requests. No commercial funding or payment was received for this work.

### Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the author used OpenAI Codex to support manuscript organization, language and readability editing, figure and repository-check code, and internal consistency review. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication. OpenAI Codex is not an author.

## References

1. Akçimen F, Martins S, Liao C, Bourassa CV, Catoire H, Nicholson GA, et al. [Genome-wide association study identifies genetic factors that modify age at onset in Machado-Joseph disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138549/). *Aging*. 2020;12(6):4742–4756. doi:10.18632/aging.102825.
2. Meyer CC, de Mattos EP, Burger RM, Blumenstock G, Pereira Sena P, Gordon C, et al. [Association of rare apolipoprotein E ε4 homozygosity with an earlier age at onset in spinocerebellar ataxia type 3](https://pubmed.ncbi.nlm.nih.gov/41854058/). *Hum Mol Genet*. 2026;35(5):ddag016. doi:10.1093/hmg/ddag016.
3. Gomez CM, Thompson RM, Gammack JT, Perlman SL, Dobyns WB, Truwit CL, et al. [Spinocerebellar ataxia type 6: gaze-evoked and vertical nystagmus, Purkinje cell degeneration, and variable age of onset](https://pubmed.ncbi.nlm.nih.gov/9403487/). *Ann Neurol*. 1997;42(6):933–950. doi:10.1002/ana.410420616.
4. Anderson JH, Christova PS, Xie TD, Schott KS, Ward K, Gomez CM. [Spinocerebellar ataxia in monozygotic twins](https://pubmed.ncbi.nlm.nih.gov/12470184/). *Arch Neurol*. 2002;59(12):1945–1951. doi:10.1001/archneur.59.12.1945.
5. Mitoma H, Buffo A, Gelfo F, Guell X, Fucà E, Kakei S, et al. [Consensus Paper. Cerebellar Reserve: From Cerebellar Physiology to Cerebellar Disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC6978293/). *Cerebellum*. 2020;19(1):131–153. doi:10.1007/s12311-019-01091-9.
6. Mitoma H, Manto M, Hampe CS. [Time Is Cerebellum](https://pmc.ncbi.nlm.nih.gov/articles/PMC6007694/). *Cerebellum*. 2018;17(4):387–391. doi:10.1007/s12311-018-0925-6.
7. Huang H, Charron TL, Fu M, Dunn M, Jones DM, Kumar P, et al. [Resilience to Endoplasmic Reticulum Stress Mitigates Membrane Hyperexcitability Underlying Late Disease Onset in a Murine Model of SCA6](https://pmc.ncbi.nlm.nih.gov/articles/PMC12894513/). *Ann Neurol*. 2026;99(2):502–522. doi:10.1002/ana.78042.
8. Zu T, Duvick LA, Kaytor MD, Berlinger MS, Zoghbi HY, Clark HB, et al. [Recovery from Polyglutamine-Induced Neurodegeneration in Conditional SCA1 Transgenic Mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC6729947/). *J Neurosci*. 2004;24(40):8853–8861. doi:10.1523/JNEUROSCI.2978-04.2004.
9. Pilotto F, Douthwaite C, Diab R, Ye X, Al Qassab Z, Tietje C, et al. [Early molecular layer interneuron hyperactivity triggers Purkinje neuron degeneration in SCA1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10431915/). *Neuron*. 2023;111(16):2523–2543.e10. doi:10.1016/j.neuron.2023.05.016.
10. Wang X, Imura T, Sofroniew MV, Fushiki S. [Loss of adenomatous polyposis coli in Bergmann glia disrupts their unique architecture and leads to cell nonautonomous neurodegeneration of cerebellar Purkinje neurons](https://pmc.ncbi.nlm.nih.gov/articles/PMC3287075/). *Glia*. 2011;59(6):857–868. doi:10.1002/glia.21154.
11. Lee C, Grijalva RM, Tejwani L, Bae E, Chase A, Ro H, et al. [Oligodendrocyte dysfunction contributes to motor deficits and Purkinje cell axonopathy in spinocerebellar ataxia type 1](https://www.jci.org/articles/view/195723). *J Clin Invest*. 2026;136(12):e195723. doi:10.1172/JCI195723.
12. Ibrahim MF, Boyanova S, Cheng YC, Ligneul C, Bains RS, Johnpulle TC, et al. [Enhanced mGluR1 function causes motor deficits and region-specific Purkinje cell dysfunction](https://pubmed.ncbi.nlm.nih.gov/41525334/). *Brain*. 2026;149(8):2774–2790. doi:10.1093/brain/awaf477.
13. Bell B, Jaramillo-Granada AM, Romero LO, Gutierrez IA, Mallampalli VKPS, Fan G, et al. [Functional and structural basis of a hypermorphic TRPC3 variant](https://pmc.ncbi.nlm.nih.gov/articles/PMC13015894/). *Sci Adv*. 2026;12(13):eaec9284. doi:10.1126/sciadv.aec9284.
14. Ito-Ishida A, Miura E, Emi K, Matsuda K, Iijima T, Kondo T, et al. [Cbln1 Regulates Rapid Formation and Maintenance of Excitatory Synapses in Mature Cerebellar Purkinje Cells In Vitro and In Vivo](https://pmc.ncbi.nlm.nih.gov/articles/PMC6670322/). *J Neurosci*. 2008;28(23):5920–5930. doi:10.1523/JNEUROSCI.1030-08.2008.
15. Takeuchi E, Ito-Ishida A, Yuzaki M, Yanagihara D. [Improvement of cerebellar ataxic gait by injecting Cbln1 into the cerebellum of cbln1-null mice](https://pmc.ncbi.nlm.nih.gov/articles/PMC5906462/). *Sci Rep*. 2018;8(1):6184. doi:10.1038/s41598-018-24490-0.
16. Wang H, Ahmed F, Khau J, Mondal AK, Twomey EC. [Delta-type glutamate receptors are ligand-gated ion channels](https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/). *Nature*. 2025;647(8091):1063–1071. doi:10.1038/s41586-025-09610-x.
17. Wilke C, Haas E, Reetz K, Faber J, Garcia-Moreno H, Santana MM, et al. [Neurofilaments in spinocerebellar ataxia type 3: blood biomarkers at the preataxic and ataxic stage in humans and mice](https://pubmed.ncbi.nlm.nih.gov/32510847/). *EMBO Mol Med*. 2020;12(7):e11803. doi:10.15252/emmm.201911803.
18. Berger M, Garcia-Moreno H, Ferreira M, Hübener-Schmid J, Schaprian T, Wegner P, et al. [Progression of biological markers in spinocerebellar ataxia type 3: longitudinal analysis of prospective data from the ESMI cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270660/). *Lancet Reg Health Eur*. 2025;55:101339. doi:10.1016/j.lanepe.2025.101339.
19. Joers JM, Wei Y, Deelchand DK, Berrington A, Park YW, Banan G, et al. [Neurochemical Endpoints to Inform Early-Stage Trials of Spinocerebellar Ataxia 2 and 3 in a Multisite Setting](https://pubmed.ncbi.nlm.nih.gov/42260718/). *Ann Clin Transl Neurol*. 2026. doi:10.1002/acn3.70443.
20. Martins AC, Furtado GV, Pinheiro JDS, Saraiva-Pereira ML, Jardim LB. [Rural Environment as a Risk Factor for the Age at Onset of Machado-Joseph Disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC11998691/). *Mov Disord Clin Pract*. 2025;12(4):520–526. doi:10.1002/mdc3.14338.
21. Benussi A, Dell'Era V, Cantoni V, Bonetta E, Grasso R, Manenti R, et al. [Cerebello-spinal tDCS in ataxia: A randomized, double-blind, sham-controlled, crossover trial](https://pubmed.ncbi.nlm.nih.gov/30135258/). *Neurology*. 2018;91(12):e1090–e1101. doi:10.1212/WNL.0000000000006210.
22. Maas RPPWM, Teerenstra S, Toni I, Klockgether T, Schutter DJLG, van de Warrenburg BPC. [Cerebellar Transcranial Direct Current Stimulation in Spinocerebellar Ataxia Type 3: a Randomized, Double-Blind, Sham-Controlled Trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC9059914/). *Neurotherapeutics*. 2022;19(4):1259–1272. doi:10.1007/s13311-022-01231-w.
23. Hauser S, Helm J, Kraft M, Korneck M, Hübener-Schmid J, Schöls L. [Allele-specific targeting of mutant ataxin-3 by antisense oligonucleotides in SCA3-iPSC-derived neurons](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649108/). *Mol Ther Nucleic Acids*. 2022;27:99–108. doi:10.1016/j.omtn.2021.11.015.
24. ClinicalTrials.gov. [A Phase 1/2a, Open-label Trial to Investigate the Safety, Tolerability, Pharmacokinetics and Pharmacodynamics of Multiple Ascending Doses of Intrathecally Administered VO659 in Participants With Spinocerebellar Ataxia Types 1, 3 and Huntington's Disease](https://clinicaltrials.gov/study/NCT05822908). ClinicalTrials.gov identifier: NCT05822908. Updated 19 August 2026; accessed 21 August 2026.
25. Ishihara T, Tada M, Kanemitsu Y, Takahashi Y, Ishikawa K, Ikenaka K, et al. [L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701440/). *eClinicalMedicine*. 2024;78:102952. doi:10.1016/j.eclinm.2024.102952.
26. Öz G, Cocozza S, Rezende TJR, Henry PG, Faber J, Harding IH, et al. [MRI end-points for clinical trials in ataxias: recommendations from the Ataxia Global Initiative MRI Biomarkers Working Group](https://pubmed.ncbi.nlm.nih.gov/42236987/). *Nat Rev Neurol*. 2026;22(7):439–456. doi:10.1038/s41582-026-01218-7.
