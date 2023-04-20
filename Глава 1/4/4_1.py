n = int(input())
k = int(input())
total_even = 0
total_odd = 0
listn = []

for i in range(n,k):
    listn.append(i)
print(listn)

for i in listn:
    if i%2 ==0:
        total_even +=i
    else:
        total_odd +=i
print('Сумма четных:', total_even, 'Сумма нечетных:', total_odd)

if total_even>total_odd:
    print('Сумма четных элементов больше')
else:
    print('Сумма нечетных элементов больше: total_even<total_odd')