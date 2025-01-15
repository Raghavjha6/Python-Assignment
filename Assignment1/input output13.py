'''Q. If a five-digit number is input through the keyboard, write a program to print a new number 
by adding one to each of its digits. For example if the number that is input is 12391 then the 
output should be displayed as 23402.'''

number = int(input("Enter a five-digit number: "))
new_number = 0
for digit in number:
    new_number =new_number +(digit + 1) % 10
print("New number: ", new_number)
