mylist = [[1,2,3], [4,5,6], [7,8,9]]

print(mylist)

mylist.sort(key=lambda i: i[1])
print(mylist)