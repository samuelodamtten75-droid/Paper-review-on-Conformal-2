# Independent manuscript review

Recommendation: major revision before submission.

Scope: review of the supplied 24-page PDF, mathematical reasoning, cross-table arithmetic, and selected bibliographic checks. No original survey CSV, implementation, fitted models, predictions, calibration scores, or seed-level logs were supplied. Reported experimental results cannot therefore be independently reproduced. This review does not establish the provenance of the writing.

## Overall assessment

The central target is well defined and more relevant to outage preparation than prediction of a controller-dependent state of charge. Separating raw reserve coverage, capacity clipping, actual stored energy, and unmet demand is a substantive strength. The abstract reports adverse cost and distribution-shift outcomes openly. The backward recursion and the block-calibration proposition are internally coherent under their assumptions. The principal weaknesses concern reproducibility, terminology, survey declarations, and unfinished editing.

## Major comments

1. **The title overstates how physics enters learning (title; Sections 3.2–3.3).** The regressor minimizes ordinary pinball loss on a physics-derived label; it has no physical residual penalty, constrained architecture, or physics-constrained training. Dispatch constraints act afterward. Define the broader intended meaning of “physics-informed” or use: “Machine Learning with Conformal Calibration for Physics-Derived Battery Outage Reserves in Survey-Informed PV–Diesel Microgrid Simulations.” The existing Ghana wording can suggest field validation; retain “survey-informed” or “simulation study” prominently.

2. **The reproducibility claim is presently unsubstantiated by the supplied materials (Section 4.4; abstract; empty availability heading).** The text says the accompanying implementation includes 84 normalized profiles, simulation, calibration, dispatch and plotting. Supply those exact artifacts and a versioned release, or remove the present-tense claim. A repository containing transcribed result tables is a summary-data release, not reproduction of the experiment. The accompanying package expressly makes this distinction.

3. **Survey ethics and consent require factual clarification (Section 4.1; declarations).** The manuscript reports 110 consenting survey responses but declares consent and ethical approval “not applicable” because there were no human experiments. A survey can involve human participants without being an experiment. State the actual consent process, approving body and reference, or documented exemption/waiver and its basis. Do not invent approval retrospectively. Explain permitted reuse and release of normalized profiles; avoid publishing identifiable questionnaire responses. The present record cannot establish which institutional determination applies.

4. **Funding statements conflict (declarations).** I.A.B. acknowledges a named King Khalid University research grant, whereas Funding says “Not applicable.” Clarify whether that grant supported this work, an author’s participation, or another activity; align both statements with the actual support and required funder wording. Add the missing competing-interests declaration using verified facts.

5. **The forecast-to-control timing needs a precise index convention (Equations 4, 17–22).** R_t serves t+1 through t+H, whereas the reserve floor restricts interval-t discharge. Explicitly state that the interval-t action seeks to retain the reserve in e_{t+1}. Explain when L_t and V_t become observable and when the command is issued. The existing quasi-static assumption helps, but the implementation must follow exactly that convention. A real-time controller using completed-hour measurements needs delayed features or a separate nowcast. This is a timing clarification, not proof of leakage.

6. **Conformal coverage is conditional on the simulator’s sampling structure (Section 3.4).** B=120 and alpha=0.1 give k=109 and 109/121=90.083%. Disjoint three-day supports and identically distributed daily draws justify the stated nominal block setup, conditional on fixed templates and fitted models. Independence of daily latent draws alone would not justify the result under seasonality or a calendar trend. Report calibration maximum scores and the selected order statistic, and identify all randomness used in fitting. The guarantee averages over calibration samples and a new block; it is not conditional on the particular threshold observed. Adjacent test-day score events overlap and must not be treated as independent Bernoulli trials.

7. **The engineering benefit is diesel displacement at higher nominal proxy cost (Tables 6 and 8).** Nominal unmet energy is zero for every policy. The study therefore does not demonstrate a nominal reduction in loss of load. Relative to greedy dispatch, the learned policy increases grid imports and cost; relative to calibrated persistence, it costs less but uses more diesel. Avoid a global claim of economic superiority, optimal operation, or improved supply reliability. A constrained economic MPC benchmark is needed if superiority to predictive optimization is claimed; otherwise explicitly limit comparisons to the stated priority policies.

8. **Actual reserve attainment is not evaluated directly.** Add outage-start stored energy, requested reserve, reserve shortfall frequency and magnitude, and event-level unmet load. Separate outages within H from longer outages. All simulated durations are 4–8 hours while H=6, so the label cannot cover every complete outage. Report outage counts, durations and worst event shortfalls, especially for critical-load interpretations.

9. **Baseline calibration fairness merits sensitivity analysis (Section 4.3).** Learned scale max(10,q0.9−q0.5) and persistence scale max(10,0.2R_pers) differ structurally. The comparison is legitimate as specified, but the 34.1% cost advantage cannot be attributed solely to learning without testing other fixed, independently selected persistence scales or an additive block correction. Calibrate every alternative on the same blocks and select scale designs before inspecting test results. Similarly, assess terminal-label coverage against its own target as well as the prefix target.

10. **The reported numerical verification needs executable evidence (Section 5.1).** Release the 600 LP windows, feasibility statuses, solver tolerances and reserve differences. Net demand drawn only from −90 to 90 kW with Pd=90 cannot exercise strict discharge-power infeasibility. Add cases above Pd and targeted capacity-overflow cases where R_t≤C but a later backward threshold exceeds C. Release maximum-balance-residual checks for every controller and scenario.

11. **Simulation and model details remain incomplete for exact reproduction.** Provide the original 84 profiles and parsing audit; RNG implementation and stream order; fitted-model random states; full ridge preprocessing and intercept settings; random-forest depth, bootstrap and random state; quantile binning settings; joblib version; CPU, thread count and timing procedure. The equations do not uniquely recover RNG draw order. State whether 110/220/440 iteration sensitivity was planned and how the fixed budget was chosen after seeing validation losses. Final refitting after validation selection is legitimate.

12. **Normalization and representativeness need a sensitivity assessment (Sections 4.1–4.2).** Equal-weight normalized facilities and the assumed 1,000-kWh daily scale do not estimate community energy use. Test category weights, the 0.35 cooling duty factor, schedule centers and demand scale. The current explicit simulation caveats are appropriate and should remain.

## Mathematical and numerical checks

- Equation 6 expands to the maximum positive prefix sum in Equation 7. The proof correctly requires every backward threshold to fit within capacity, together with the discharge-power condition. A small R_t by itself does not establish feasibility.
- A useful counterexample is stored-energy increments [−10,+10] with C=5: initial reserve is zero but the later threshold is 10, so capacity makes the window infeasible. Include this diagnostic test.
- Equation 9 is no larger than Equation 7; late surplus cannot repair an early unmet deficit.
- The claim that charging/discharging remain feasible is supported by the min constraints, given feasible initial energy and positive efficiencies. This storage statement does not guarantee that total load can be served.
- Quantile sorting is a defensible postprocessing rule for calibration. It may change the interpretation and empirical accuracy of each individually fitted quantile. The processed “median” covering 64.7% is not an arithmetic contradiction: targets have substantial mass at zero (greedy hourly coverage 30.1%). Report pinball losses and conditional coverage by hour and target magnitude before interpreting quantile quality.
- MAE reduction: (30.39−14.53)/30.39=52.19%. Diesel reduction: (1623−165)/1623=89.83%. Grid increase: (69.29−39.04)/39.04=77.48%. Cost increase: (16194−12932)/12932=25.22%. Cost reduction versus calibrated persistence: (24565−16194)/24565=34.08%. These agree with the rounded headline percentages.
- The prose reports a paired diesel reduction of 1457 kWh; subtraction of rounded Table 6 means gives 1458. This can arise from unrounded values. Provide seed-level results and specify rounding rather than changing a paired result solely from rounded means. The same issue applies to stress differences.
- Partition counts check: training 8730, validation 2130, refit 10890, calibration 2880, annual assessment 8760 origins. The last calibration central day is 816. Its support through day 817 fits within 820 generated days.
- Survey counts check: 110−5−2=103; 84+19=103; 43+18+17+6=84; 103×15=1545; 786+447+140+164+8=1545.
- Appendix cost check using reported rounded figures: greedy 0.165×39040+550+0.02×(156324+140713)=12932.34 USD; learned 0.165×69290+54+0.02×(123882+111481)=16194.11 USD. Both match Table 6 within rounding.
- Appendix battery-energy check: with eta=sqrt(0.90), reported AC flows imply changes of −0.022557581 MWh (greedy), +0.013492385 MWh (learned block), and −0.000421637 MWh (fixed). Reported final-minus-initial energies are −0.022, +0.013 and 0 MWh. Residuals are −0.558, +0.492 and −0.422 kWh, all within the approximately 2.001 kWh combined display-rounding allowance. Thus these entries are consistent with Equation 31 at reported precision. The included arithmetic check independently calculates them.


## Exact editing corrections

- Section 2.1 contains literal “citepnarayan2020”. Restore a valid citation and include its verified bibliography entry; it is absent from the displayed reference list. Do not guess the intended Narayan paper.
- Section 2.1 contains “citephartvigsson2018”. Replace it with the proper citation to the existing Hartvigsson and Ahlgren entry [2].
- Section 2.2: insert a space in “[7]combines”.
- Section 3.5 contains a corrupted sentence: “... e_t in [0,C].. The stored energy limits the available capacity limits charging, while discharging +1.” Replace the entire passage with: “For any nonnegative input trajectory and reserve forecast, Equations (18)–(19) preserve 0≤e_{t+1}≤C whenever 0≤e_t≤C. Available capacity limits charging, and available stored energy limits discharging. Storage feasibility therefore does not depend on statistical calibration.”
- Figure 1 selects windows using R_t≤C and power feasibility, but this alone does not establish capacity feasibility. Require I_t^C=I_t^P=0 or verify the chosen example separately before calling it feasible.
- Author Contributions and Data and Code Availability are empty. Complete both using verified information.
- Verify the corresponding author’s institutional address and postal code; no correspondence email is displayed. Confirm official department names and journal affiliation formatting with the authors.
- Remove clinical-trial and publication-consent headings if the target journal does not require them and they are inapplicable; retain an accurate participant-consent statement for the survey.

## Claim and writing audit

Writing style cannot establish whether a text was generated by a particular tool; a detection percentage would be unsupported. The concrete concerns are an overstated physics-informed title, an unavailable accompanying implementation, unverified LP and runtime claims, and inconsistent declarations. “Reproducible connection” in the abstract should become “connection” until the complete release is accessible. “Independent test seeds” establish within-simulator performance, not field generalization. The manuscript already makes this distinction carefully. Maintain those limitations. Avoid claims of optimal dispatch, guaranteed uninterrupted supply, measured Ghanaian savings, adaptive calibration, or battery-life extension, none of which is demonstrated.

## Author contributions

The PDF contains the author names but no roles. The accompanying paragraph is a proposed allocation for confirmation by every author, not a verified contribution record. Initials: S.O.O., A.Y., S.B., T.M., M.Y., E.A., and I.A.B. Do not infer funding acquisition solely from an acknowledgement or allocate contributions merely from author order.

## Repository release requirements

The attached GitHub folder contains transcribed summary tables, provenance notes, parameters, independently implemented reserve/calibration utilities, and transparent missing-material requirements. It contains no fabricated survey profiles, annual trajectories, calibrated models, or confidence intervals. It does not reproduce manuscript figures or annual experiments. Add the original anonymized templates, original end-to-end code, environment lock file, seed-level outputs, raw predictions, calibration maxima, LP diagnostics and plotting scripts before claiming full reproducibility. Set an actual data/code license only after rights holders agree; no license has been assigned on their behalf.

## Selected reference checks

Publisher pages confirm that the cited 2026 Energies papers exist: https://doi.org/10.3390/en19102297 and https://doi.org/10.3390/en19174093 . Official scikit-learn documentation confirms histogram quantile regression uses pinball loss: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html . These selected checks are not a complete reference audit. The unresolved Narayan entry remains unresolved.
