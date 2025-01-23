'''Q. If a four-digit number is input through the keyboard, write a program to obtain the sum of
the first and last digit of this number.'''

num = int(input("Enter a four-digit number: "))
last = num % 10 
while num >0:
    first=num%10
    num //= 10
print("Sum of the first and last digit is:",last+first)
