n = float(input())
k = int(input())

N = n*k
R = N//1
K = (N%1)*100

print('Нужно заплатить', (int(R)), round(K,2 ))