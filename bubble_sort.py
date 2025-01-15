r=int(input('Enter the range:'))
l=[]
print('Enter your numbers:')
for i in range(r):
    l.append(int(input()))
for j in range(r-1):
    for i in range(r-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print('After bubble sort:')
for i in range(r):
    print(l[i], end=' ')
