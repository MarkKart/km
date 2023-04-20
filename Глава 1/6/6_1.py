a = int(input())
b = int(input())

def func_1(n1,n2):
    total = n1+n2
    return total

def func_2(n1, n2):
    differ = n1-n2
    return differ

def func_3(n1,n2):
    multip = n1*n2
    return multip

def func_4(n1,n2):
    division = n1/n2
    return division

print(func_1(a,b), func_2(a,b), func_3(a,b), func_4(a,b))
