import string # learn more: https://python.org/pypi/string
import csv
import pandas as pd
with open('Crime.csv','r') as myfile:
  r = csv.reader(myfile)
  rows = list(r)
  print("")
  
  
df = pd.read_csv('Crime.csv')
list(set(df.RUCR_EXT_D))
g = list(df['RUCR_EXT_D'].unique())
g = df.groupby('RUCR_EXT_D')
g['RUCR_EXT_D'].nunique()
print(list(g))