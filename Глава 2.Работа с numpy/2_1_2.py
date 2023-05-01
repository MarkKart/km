import numpy as np

a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2])
rows = len(a)
print('Количество строк', rows)

a.resize(9, 1) #вместо b.shape
print(a)

a.resize(3,3)
print(a)
MINcols = a.min(axis = 0)
MINrows = a.min(axis = 1)
print('Минимальное число в столбце:', MINcols)
print('Минимальное число в строке:', MINrows)

MAXcols = a.max(axis = 0)
MAXrows = a.max(axis = 1)
print('Максимальное число в столбце:', MAXcols)
print('Максимальное число в строке:', MAXrows)

SUMcols = a.sum(axis = 0)
SUMrows = a.sum(axis = 1)
print('Сумма в столбцах:', SUMcols)
print('Сумма в строках:', SUMrows)