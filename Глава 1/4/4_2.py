string = '2,3,4,5'
string_1 = '6,7,8,9'

tuplen = tuple(map(int, string.split(',')))
tuplen_1 = tuple(map(int, string_1.split(',')))

print(tuplen)
print(tuplen_1)

ma = max(tuplen)
mi = min(tuplen)
ma_1 = max(tuplen_1)
mi_1 = min(tuplen_1)
res = abs(ma-ma_1)
res_1 = abs(mi-mi_1)

print('Максимум в 1:', ma, 'Максимум в 2:', ma_1)
print('Минимум в 1:', mi, 'Минимум в 2:', mi_1)
print('Разница максимумов:', res, 'Разница минимумов:', res_1)

