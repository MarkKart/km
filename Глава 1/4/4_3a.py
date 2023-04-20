fruits = ('яблоко','банан','апельсин','груша','мандарин')
number = ('5','8','3','5','10')


fr = str(input('Введите фрукт: '))

if fr in fruits:
    num = fruits.index(fr)
    print('Индекс фрукта = ', num)
    
for i in number:
    if num == i:
        print (number[i])
   
