print('Armstrong numbers between 1 and 500 are:-')
i=2
while i<500:
    n=i
    c=0
    while n>0:
        n=n//10
        c=c+1
    m=i
    sum=0
    while m>0:
        r=m%10
        sum=sum+(r**c)
        m=m//10
    if i==sum:
        print(i)
    i=i+1
