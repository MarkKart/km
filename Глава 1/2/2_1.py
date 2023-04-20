R = float(input())

R_2 = pow(R,2)
R_3 = pow(R,3)
S = 3.14*R_2 #площадь большого круга
S_p = 4*3.14*R_2 #площадь поверхности сферы
V = (4/3)*3.14*R_3

print(round(S,2))
print(round(S_p,2))
print(round(V,2))