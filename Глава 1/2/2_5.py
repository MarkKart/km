
a = float(input())
b = float(input())

G = pow(a,2)+pow(b,2)    #квадрат гипотенузы
c = pow(G,0.5)           #гипотенуза
sin = a/c
cos = b/c
tg = a/b
sin_1 = b/c
cos_1 = a/c
tg_1 = b/a

print('Гипотенуза:', c)
print('синус, косинус, тангенс для 1 угла:', sin, cos, tg)
print('синус, косинус, тангенс для 2 угла:', sin_1, cos_1, tg_1)