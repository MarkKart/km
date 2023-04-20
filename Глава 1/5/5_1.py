A = {1,6,7,3,5,4,8,0,9,2}
B = {3,6,9,4,6,2,1,5,7,8}

out = A.union(B)    #Объединение
print('Объединение: ', out)

out_1 = A.intersection(B)
print('Пересечение: ', out_1)

out_2 = A.difference(B)
print('Разность: ', out_2)

out_3 = A.symmetric_difference(B)
print('Симметричная разность: ', out_3)