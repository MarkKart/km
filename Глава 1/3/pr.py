x=int(input())
y = int(input())
p = int(input())
i = 0
while x < y:
    x *= 1+p/100
    i += 1
print(i)