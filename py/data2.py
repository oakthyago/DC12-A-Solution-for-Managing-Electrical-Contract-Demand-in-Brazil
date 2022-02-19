import pandas as pd
import numpy as np

df = pd.read_excel("C12.xlsx")
booleans = []
boo = []
n = 0
last = 0
x = 0
y = 1
for length in df.F_MATRICULA:
    if length != last:
        booleans.append(True)
        boo.append(y)
        last = length
        y = y + 1

    else:

        booleans.append(False)

is_long = pd.Series(booleans)
df2=df.loc[is_long,'DC12']
df2= df2+boo
df.loc[:,'Unnamed: 0']=np.nan
df.loc[is_long,'Unnamed: 0'] = df2
df.to_excel("C13.xlsx")