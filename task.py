import csv
import pandas
with open('Crime.csv','r') as myfile:

reader = csv.reader(myfile)

rows = list(reader)

import csv

fin = open('Crime.csv')

words = ["Assault","Robbery","BREAK AND ENTER","THEFT FROM VEHICLE"]

found = {}

count = 0

for line in fin:

  for word in words:

      if word in line:

          count = count + 1

  found[word] = count

print(found)



df = pd.read_csv('Crime.csv')

list(set(df.Description))

g = list(df['Description'].unique())

print(g)
