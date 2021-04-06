
import pandas as pd
import numpy as np

df = pd.read_excel("C13.xlsx")
df.replace(0,np.nan)
df.to_excel("C14.xlsx")