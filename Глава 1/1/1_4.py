n = int(input())

s = n//100
d = n//10-s*10
e = n%10

p = s*d*e

print (s,d,e)
print ('Произведение', p)
