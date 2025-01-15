'''Q. Write a program in Python to calculate factorial of a natural number.'''

def fact(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f
n=int(input('Enter a natural number for factorial:'))
f=fact(n)
print('Factorial of ',n,' is ',f)
