'''Q. Write a program in Python to find the square of any number using the function.'''

def sq(a):
    c=a**2
    return c
n=int(input('Enter the number for square:'))
sq=sq(n)
print('Square of',n,'is',sq)
