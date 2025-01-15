l1=[8,10,15,26,29,35,60,72]
item=60
b=0
l=len(l1)-1
while b<=l:
    m=(b+l)//2
    if item==l1[m]:
        print("Item found at index",m)
        break
    elif item>l1[m]:
        b=m+1
    else:
        l=m-1
else:
    print("Item not found")
    
