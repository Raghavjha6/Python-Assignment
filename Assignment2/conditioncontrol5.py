'''Q. A five-digit number is entered through the keyboard. Write a program to obtain the reversed 
number and to determine whether the original and reversed numbers are equal or not.'''

num= int(input("Enter a number:"))
n=num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if n==rev:
    print("Reversed number is equal.")
else:
    print("Reversed number is not equal.")

