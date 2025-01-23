'''Q. If a five-digit number is input through the keyboard, write a program to calculate the sum
of its digits.(Hint: Use the modulus operator ‘%’)'''

num = int(input("Enter a five-digit number:"))
sum_digits =0
number=num
while number > 0:
    sum_digits += number % 10
    number //= 10
print("Sum of digits of",num,":",sum_digits)
