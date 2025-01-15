l=[4,7,0,3,9,12]
item=int(input('Enter the item to be searched:'))
for i in range(len(l)):
    if l[i]==item:
        print('Found at index',i)
        break
else:
    print('Item not found')
