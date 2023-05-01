import numpy as np

a = np.array([[4,2], [9,1]])
b = np.array([[5,3], [2,5]])

MASIV = np.row_stack([a,b])
print('Массив из 4x2:')
print(MASIV)

Srez = MASIV[0:3, :]
print('Срез:')
print(Srez)

print('Сумма элементов:',Srez.sum())
print('Макс. элемент:',Srez.max())
print('Мин. элемент:',Srez.min())

MASIVNEW = np.column_stack([a,b])
print('Массив 2x4:')
print(MASIVNEW)

SrezNEW = MASIVNEW[:1, 0:3]
print('Срез:')
print(SrezNEW)
print('Сумма элементов:',SrezNEW.sum())
print('Максимальный элемент:',SrezNEW.max())
print('Минимальный элемент:',SrezNEW.min())