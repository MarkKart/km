m = float(input())
h = float(input())

IMT = round(m/(pow(h,2)),2)
N = 18.5
M = 30

print('ИМТ человека =', IMT)
print(N<=IMT<=M)