'''Q. Two numbers are entered through the keyboard. Write a program to find the value of one number 
raised to the power of another.'''

a=int(input('Enter base:'))
b=int(input('Enter power:'))
pow=1
i=1
while i<=b:
    pow=pow*a
    i=i+1
print(a,'to the power',b,'is',pow)
