# Data dictionary and provenance

Source: supplied manuscript, “Physics-Informed Machine Learning with Conformal Calibration for Battery Outage Reserve Prediction in PV–Diesel Microgrids in Rural Ghana”, 24-page PDF reviewed 19 October 2026.

Table 4.csv: reserve prediction MAE/RMSE, kWh; mean and sample SD over 10 nominal annual paths.
Table 5.csv: hourly and daily raw prefix-reserve coverage (%), requested reserve (kWh), means and sample SD over 10 nominal paths. Every method is evaluated against the prefix target, including the terminal-trained alternative.
Table 6.csv: nominal annual diesel output (kWh), grid import (MWh), fuel (L), cost proxy (USD), with sample SD over 10 paths.
Table 7.csv: ablation means: median MAE (kWh), daily coverage (%), raw reserve (kWh), grid (MWh), cost (USD).
Table 8.csv: stressed annual means; diesel and unmet energy in kWh; grid in MWh; cost USD; coverage %. No SD is supplied in this table.
Table 9.csv: energy accounting means in MWh except EFC (cycles). Appendix energy-balance concerns are flagged in the private review and arithmetic checks.
Survey Counts.csv: aggregate counts from Section 4.1; contains no individual survey record.
Parameters.json: declared scenario and model settings, not a full environment or generator specification.

Every CSV row is reported summary evidence. Values are rounded and cannot reconstruct paired confidence intervals or underlying time series. “quantile / hourly” denotes identical reported operation because the hourly correction is zero.
