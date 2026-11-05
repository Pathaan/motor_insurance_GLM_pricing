import pandas as pd
import numpy as np
df_freq = pd.read_csv("D:/Actuary/Projects Actuarial/data/freMTPL2freq.csv")
df_sev = pd.read_csv("D:/Actuary/Projects Actuarial/data/freMTPL2sev.csv")
df_freq.head()
df_sev.head()
df_freq.describe()
df_freq.dtypes