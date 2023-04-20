I1 = float(input())
I2 = float(input())
I3 = float(input())
R1 = float(input())
R2 = float(input())
R3 = float(input())

I = I1+I2+I3   
r =  (1/R1)+(1/R2)+(1/R3)
R = 1/r   #сопротивление для параллельного
U = I*R   #напряжение для параллельного

print('Напряжение =', U)