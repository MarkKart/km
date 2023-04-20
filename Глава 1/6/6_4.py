n = int(input())

def faktorial(n):
    fakt = 1
    for i in range(1, n+1):
        fakt *= i
    return fakt
print('Факториал =', faktorial(n))