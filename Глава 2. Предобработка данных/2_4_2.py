import pandas as pd

df = pd.read_csv('https://elteha.ru/data_science/precious_metal.csv', sep=';')
#print(df)

NEWdf = ['gold', 'silver', 'platinum', 'palladium', 'date']
DF = df.set_axis(NEWdf, axis = 'columns', inplace = True)
print(DF)

DF1 = df.rename(columns ={'GOLDA':'gold', 'Silver':'silver', 'platinu':'platinum', 'Palla':'palladium', 'Date':'date'})
print(DF1)