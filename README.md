
## Workflow: EDA → cleaning/feature engineering → frequency GLM → severity GLM → Tweedie combined model → validation → rating table.
## Dataset: https://www.kaggle.com/datasets/floser/french-motor-claims-datasets-fremtpl2freq

## Dataset Description: freMTPL2freq

| Column | Meaning |
|---|---|
| `IDpol` | Unique policy ID and join key to `freMTPL2sev`. |
| `ClaimNb` | Number of claims during the exposure period. |
| `Exposure` | Policy duration in years (fraction of a year). Some values greater than 1 may indicate data errors. |
| `VehPower` | Vehicle engine power (ordinal, 4–15). |
| `VehAge` | Vehicle age in years. |
| `DrivAge` | Driver age in years. |
| `BonusMalus` | French no-claims bonus/malus score (50 = best; above 100 = malus). |
| `VehBrand` | Vehicle brand code (nominal, approximately 11 levels). |
| `VehGas` | Fuel type: Diesel or Regular. |
| `Area` | Area density category (A = rural to F = urban). |
| `Density` | Population density of the policyholder's town. |
| `Region` | French administrative region (INSEE). |

## Files (run in order)
**01_data_loading.py** — fetch/load freMTPL2freq (+ freMTPL2sev), basic sanity checks

**02_eda.py** — portfolio summary, frequency by rating factor, severity analysis, loss/frequency heatmaps, overdispersion test, missing values, correlation matrix

**03_feature_engineering.py** — outlier capping, banding, interactions, encoding

**04_frequency_glm.py** — Poisson / Negative Binomial frequency GLM with log(Exposure) offset

**05_severity_glm_and_tweedie.py** — Gamma severity GLM + Tweedie combined pure-premium GLM

**06_diagnostics_and_validation.py** — deviance residuals, lift charts, Gini/Lorenz, train/test split, calibration

**07_rating_table.py** — final multiplicative relativity table from fitted GLMs
