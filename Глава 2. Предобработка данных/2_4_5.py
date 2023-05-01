import pandas as pd

df = pd.read_csv('https://elteha.ru/data_science/precious_metal.csv', sep=';')
print(df)

NEWdf = ['gold', 'silver', 'platinum', 'palladium', 'date']
DF = df.set_axis(NEWdf, axis = 'columns', inplace = True)
print(DF)

DF1 = df.rename(columns ={'GOLDA':'gold', 'Silver':'silver', 'platinu':'platinum', 'Palla':'palladium', 'Date':'date'})
print(DF1)

DF1 = DF1.fillna(0)

def replace_symbol(x):
    x = str(x)
    x = float(x.replace(',','.'))
    return x
DF1['gold'] = DF1['gold'].apply(replace_symbol)
DF1['silver'] = DF1['silver'].apply(replace_symbol)
DF1['platinum'] = DF1['platinum'].apply(replace_symbol)
DF1['palladium'] = DF1['palladium'].apply(replace_symbol)
print(DF1)

gold_mean = DF1['gold'].mean()
print('gold_mean', gold_mean)
silver_mean = DF1['silver'].mean()
print('silver_mean', silver_mean)
platinum_mean = DF1['platinum'].mean()
print('platinum_mean', platinum_mean)
palladium_mean = DF1['palladium'].mean()
print('palladium_mean', palladium_mean)

