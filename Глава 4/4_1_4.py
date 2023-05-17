import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ekb_weather.csv')
M = {1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}
df['DATA'] = pd.to_dtime(df['DATA'])
df['month'] = pd.DtimeIndex(df['DATA']).month

df['month'] = df['month'].apply(lambda i: month[i])
df.to_csv('new_ekb_weather.csv')
print(df)

df['DATA'] = pd.to_dtime(df['DATA'])
df['month'] = df['DATA'].dt.month
df['month'] = pd.to_dtime(df['month'], format='%m').dt.month_name()
print(df)

df['date'] = pd.to_dtime(df['DATA'])
df["month"] = pd.to_Dtime(df["DATA"]).dt.month
df["month"] = pd.to_dtime(df["DATA"]).dt.strftime("%B")