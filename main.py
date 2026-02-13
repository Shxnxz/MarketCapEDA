import pandas as pd

file = 'data.csv'

df = pd.read_csv(file)
#Check Missing Value
print(df.isnull().sum())