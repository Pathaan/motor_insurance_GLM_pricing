
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
``

<img width="1102" height="565" alt="image" src="https://github.com/user-attachments/assets/77887639-9004-441b-b7ea-4b14b2bfe31b" />

