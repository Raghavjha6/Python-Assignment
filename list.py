l1=[10,20,30,40,50]
l2=[1,2,3,4]
for i in l1:
    print(i,end=' ')
print()
print(l1*3)     #multiple time printing
print(l1+l2)    #concatenation
l1.append(50) #append
print(l1)
l1.extend([60,70])    #extend
print(l1)
l1.append([60,70])    #append
print(l1)
l2.insert(2,100)  #insert
print(l2)
print(l2.index(100)) #INDEX
del l1
del l2

