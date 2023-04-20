from random import randint
n = int(input())

numbers = []
for i in range(n):
    numbers.append(randint(0, 100))
print('Список:', numbers)

numbers.sort()
print('Сортированный список:', numbers)

m = max(numbers)
print('Максимальное число:', m)