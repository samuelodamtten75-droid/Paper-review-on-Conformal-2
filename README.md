# Battery outage reserve: summary data and mathematical utilities

Status: partial evidence package extracted from the supplied manuscript, not the original experimental repository. No annual result is independently reproduced here.

All CSVs are transcriptions of rounded manuscript tables. They are not measurements or fresh simulation results. Uncertainty columns reproduce the manuscript's annual sample standard deviations. Blank uncertainty fields mean not reported in that table, not zero. See DATA DICTIONARY.md.

Run `python check.py` for arithmetic and deterministic mathematical checks (standard library only). `reserve.py` independently implements Equations 5–8 and 13–15. This is new reference code, not recovered author code. It does not train models, generate community profiles, or reproduce annual dispatch.

Missing for full reproduction: the 84 anonymized normalized 24-hour survey profiles; parsing audit and permitted-use documentation; original simulator and random stream order; feature/partition construction; model fitting and saved estimators; original calibration maxima; hourly predictions and dispatch; ten-seed metrics; LP verification; original figure code; and an exact environment lock file. These have not been reconstructed or invented.

Upload the contents of this GitHub Package folder to the desired repository. Keep the private review and proposed contribution allocation outside the public repository. A summary-data release can be published as such, but must not be described as complete reproducibility materials. No publication to GitHub has been performed.

No data or code license is assigned here. Obtain rights-holder agreement before applying a license or publishing source survey material. Do not include personal questionnaire records.
