a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
elif c>=b and c>=a:
    print(c)
else:
    print('Ни одно из условий не выполнено')     