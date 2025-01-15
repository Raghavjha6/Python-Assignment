r=int(input('Enter the range:'))
l=[]
print('Enter your number:')
for i in range(r):
    l.append(int(input()))
j=1
while j<len(l):
    i=j
    while i<len(l):
        if l[j-1]>l[i]:
            l[j-1],l[i]=l[i],l[j-1]
        i=i+1
    j=j+1
print('After selection sort:')
for i in range(r):
    print(l[i], end=' ')
