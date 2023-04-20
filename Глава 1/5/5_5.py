animals = {'dog' : 'собака', 'cat' : 'кошка', 'rabbit': 'кролик'}

while (True):
    print('Введите ключ: ')
    n = input()
    if n=='stop':
        break
    print('Введите значение: ')
    v=input()
    animals[n]=v
print(animals)    
    

