'''Q. Write a program to find the range of a set of numbers. Range is the difference between the 
smallest and biggest number in the list.'''

numbers = []
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break
    numbers.append(int(num))

if numbers:
    range_of_numbers = max(numbers) - min(numbers)
    print("The range of the set of numbers is:", range_of_numbers)
else:
    print("No numbers were entered.")
