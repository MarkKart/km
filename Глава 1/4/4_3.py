string = 'яблоко,банан,апельсин,груша,мандарин'
string_1 = '5,8,3,5,10'
fruits = tuple(map(str, string.split(',')))
number = tuple(map(int, string_1.split(',')))


print(fruits)
for i in number:
    print(number[i])
