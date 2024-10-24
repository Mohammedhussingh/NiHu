import pandas as pd

file = 'bouman_8.xlsx'

df = pd.read_excel(file)

names = df.iloc[:,0].tolist()

print(names)