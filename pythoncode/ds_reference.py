print('Simple Assignment')
shoplist = ['apple', 'banana', 'carrot', 'mango']
mylist = shoplist

del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

mylist = shoplist[:]
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)