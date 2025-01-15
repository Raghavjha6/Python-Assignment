'''Q. Write a program in Python to calculate Power(a,b) using function.'''

def power(a,b):
    c=a**b
    return c
a=int(input('Enter base:'))
b=int(input('Enter power:'))
pow=power(a,b)
print(a,' to the power ',b,' is ',pow)
