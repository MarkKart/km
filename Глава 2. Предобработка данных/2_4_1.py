import pandas as pd

df = pd.read_csv('https://elteha.ru/data_science/precious_metal.csv', sep=';')
print(df.info())