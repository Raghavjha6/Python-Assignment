'''Q. Write a program in Python to calculate sum of Fibonacci series.'''

def fibo_sum(r):
    a=0
    b=1
    print("Fibonaci series:")
    print(a)
    print(b)
    sum=1
    while r>2:
        c=a+b
        sum=sum+c
        print(c)
        a=b
        b=c
        r=r-1
    else:
        return sum
r= int(input("Enter number of terms: "))
sum=fibo_sum(r)
print('Fibonacci series sum=',sum)
