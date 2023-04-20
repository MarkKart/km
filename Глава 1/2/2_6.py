X1 = int(input())
Y1 = int(input())
Z1 = int(input())
X2 = int(input())
Y2 = int(input())
Z2 = int(input())

SP = X1*X2+Y1*Y2+Z1*Z2                          #скалярное произведение

zn = pow(pow(X1,2)+pow(Y1,2)+pow(Z1,2),0.5)     #знаменатель
zn_1 = pow(pow(X2,2)+pow(Y2,2)+pow(Z2,2),0.5)   #знаменатель
z = zn*zn_1
cos = SP/z                                      #угол между векторами

VP = (Y1*Z2-Y2*Z1)*(Z1*X2-X1*Z2)*(X1*Y2-Y1*X2) #векторное произведение

print('скалярное произведение = ', SP)
print('угол между векторами = ', cos)
print('векторное произведение = ', VP)

