n = int(input())
max = 0

while n != 0:
    if n>max:
        max=n
    n = int(input())
print(max)    
print ('Вы ввели 0, программа завершена')