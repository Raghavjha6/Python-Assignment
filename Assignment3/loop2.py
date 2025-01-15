'''Q. Write a program to find the factorial value of any number entered through the keyboard.'''

n=int(input('Enter a natural number for factorial:'))
num=n
f=1
while n>0:
    f=f*n
    n=n-1
print('Factorial of',num,'is',f)
