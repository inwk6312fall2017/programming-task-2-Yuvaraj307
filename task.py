import string # learn more: https://python.org/pypi/string
import csv
import pandas as pd
df = pd.read_csv('Crime.csv')
list(set(df.RUCR_EXT_D))
df.head(9)
g = list(df['RUCR_EXT_D'].unique())
gi = df.groupby('RUCR_EXT_D')
oi = df.groupby('RUCR')
print(gi['RUCR_EXT_D'].nunique(), oi['RUCR'].nunique())
