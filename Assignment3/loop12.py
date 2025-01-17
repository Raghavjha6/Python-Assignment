'''Q. Write a program to add first seven terms of the following series using a for loop:
1/1!+2/2!+3/3!+⋯ +n/n!'''

j=1
sum=0
while j<=7:
    i=j
    f=1
    while i>0:
        f=f*i
        i=i-1
    sum=sum+j/f
    j=j+1
else:
    print('sum of the series=',sum)
    

