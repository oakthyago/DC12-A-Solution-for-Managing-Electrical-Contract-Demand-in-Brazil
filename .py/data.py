import numpy as np
import pandas as pd

df = pd.read_excel("C13.xlsx")
#df.set_index(['F_MATRICULA','F_ANO'],inplace=True)
#df.sort_index(inplace=True)
#df.loc[(slice(None),2003),'DC12'] =0
#df.reset_index(inplace=True)
#df.to_excel("Teste2.xlsx")
#df = pd.read_excel("Teste2.xlsx")
#df.set_index(['F_MATRICULA','F_ANO','F_MES'],inplace=True)
#df.sort_index(inplace=True)
#df.loc[(slice(None),2003,[1,2,3,4,5,6]),'DC6']=0
#df.reset_index(inplace=True)
#df.to_excel("Teste3.xlsx")
booleans =[]
n=0
x=0
last=0
for length in df.MATRICULA:
    if length != last:
        for a in range(12):
            booleans.append(True)
        last = length
        x=0
    else:
        if x < 11:
            x=x+1
        else:
            booleans.append(False)

is_long = pd.Series(booleans)
df.loc[is_long,'DC12'] = np.nan

booleans =[]
n=0
last=0
x=0
for length in df.MATRICULA:
    if length != last:
        for a in range(6):
            booleans.append(True)
        last = length
        x=0
    else:
        if x < 5:
            x=x+1
        else:
            booleans.append(False)

is_long = pd.Series(booleans)
df.loc[is_long,'DC6'] = np.nan

df.to_excel("C14.xlsx")