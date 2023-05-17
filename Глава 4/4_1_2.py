import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ekb_weather.csv')
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M')
print(df.info())