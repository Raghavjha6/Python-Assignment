print('Prime numbers from 1 to 300 are:-')
i=1
while i<=300:
    n=i
    c=0
    j=2
    while j<=i//2:
        if i%j==0:
            break   
        j=j+1
    else:
        print(i,end=' ')
    i=i+1
