R1 = float(input())
R2 = float(input())
R3 = float(input())
U = float(input())
 
r =  (1/R1)+(1/R2)+(1/R3)
R = 1/r   #сопротивление для параллельного
I = U/R   #сила тока для параллельного

print('Сила тока =', round(I,2))