'''Q. If a five-digit number is input through the keyboard, write a program to reverse the number.'''

num= int(input("Enter a five-digit number:"))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)
