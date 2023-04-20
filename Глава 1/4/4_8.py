from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(0, 100))
print('Список:', numbers)

max_va = numbers.index(max(numbers))
min_va = numbers.index(min(numbers))

numbers[max_va],numbers[min_va]=numbers[min_va],numbers[max_va]
print(numbers)