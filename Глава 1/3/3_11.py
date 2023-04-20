a = int(input())
b = int(input())
c = int(input())

D = (b**2)-4*a*c
D1 = pow(D,0.5)
x = ((-1)*b)/(2*a)
x_1 = (((-1)*b)-D1)/(2*a)
x_2 = (((-1)*b)+D1)/(2*a)

if D<0:
    print('нет корней')
elif D==0:
    print(x)
elif D>0:
    print(x_1, x_2)

    

