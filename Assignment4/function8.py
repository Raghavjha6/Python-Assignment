'''Q. Write a program in Python to calculate combinatoric C(n,r) using function.'''

def fact(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f
n=int(input('Enter value of n for combination:'))
r=int(input('Enter value of r for combination:'))
c=fact(n)/(fact(n-r)*fact(r))
print('combinatoric ',n,'C',r,' is ',c)
