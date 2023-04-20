from random import randint
n = int(input())

numbers = []
for i in range(n):
    numbers.append(randint(0, 100))
print('Список:', numbers)

s = sum(numbers)
print('Сумма:', s)

sr = s/n
print('Среднее значение:', sr)

disp = sum((x-sr)**2 for x in numbers)/n
print('Дисперсия:', disp)

otkl = pow(disp, 0.5)
print('Стандартное отклонение:', otkl)