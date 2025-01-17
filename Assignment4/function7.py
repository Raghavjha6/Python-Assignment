'''Q. Write a program in Python to check whether an inputted number is palindrome.'''

def palindrome(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
num= int(input("Enter a number:"))
pal=palindrome(num)
if num==pal:
    print("Palindrome number.")
else:
    print("Not a Palindrome number.")
