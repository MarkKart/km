from random import randint
n = int(input())
sum = 0

numbers = []
for i in range(n):
    numbers.append(randint(0, 100))
print('Список:', numbers)

for i in numbers:
    sum +=i
print('Сумма чисел:', sum)    
