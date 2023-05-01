import pandas as pd

df = pd.read_csv('precious_metal_new2.csv')
MAX = df['gold'].max()
print(MAX)
MIN = df['gold'].min()              
print(MIN)
STANDART = (df['gold']-mi)/(ma-mi)      
print('стандартная нормализация:',STANDART)
SRED = df['gold'].mean()       
print(SRED)
SOTCL = df['gold'].std()              
print(SOTCL)
MINMAXNORM = (df['gold']-SRED)/SOTCL
print('min-max нормализация:', MINMAXNORM)
