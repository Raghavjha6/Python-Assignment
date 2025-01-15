'''Q. Write a program in Python to check if a given number is even or odd using the function.'''
def evenodd(n):
    if n%2==0:
        print('Even number.')
    else:
        print('Odd number.')
n=int(input('Enter a number:'))
evenodd(n)
