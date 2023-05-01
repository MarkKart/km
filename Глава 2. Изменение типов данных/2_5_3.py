import pandas as pd

df = pd.read_csv('precious_metal_new2.csv')

df = df.loc[:, ['gold', 'gold_usd', 'silver', 'silver_usd',
                'platinum', 'platinum_usd', 'palladium', 'palladium_usd',
                'date']]
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M')
print(df)

df['Month'] = pd.datetimeindex(df['date']).month

print(df['Month'])

