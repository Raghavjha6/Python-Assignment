'''Q. Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs. 
12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for 
fractional part of an hour.'''

for i in range(10):
    hours_worked = int(input("Enter hours worked by employee:"))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * 12
        print("Employee",i+1,"earns Rs.",overtime_pay,"in overtime pay.")
    else:
        print("Employee",i+1,"does not earn any overtime pay.")
