from random import randint

numbers = []
for i in range(29):
    numbers.append(randint(0, 99))
print('Список:', numbers)

maximum = numbers[0]
for i in range(1, 29):
    if numbers[i]>maximum:
        maximum = numbers[i]
print('Максимальное значение:', maximum)

numbers.insert(0, maximum)
print(numbers)
