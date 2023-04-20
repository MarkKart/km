n = int(input())
m = int(input())
N = int(input())

D = n+m/100
P = D*N
p1 = P//1
p2 = P%1
p3 = p2*100


print ('Нужно заплатить' , (int(p1)),  round(p3,2 ))