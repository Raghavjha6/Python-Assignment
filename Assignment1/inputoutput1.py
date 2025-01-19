'''Q. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic 
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross 
salary.'''

basic = float(input("Enter Ramesh's basic salary: "))
da = 0.40 * basic
hra = 0.20 * basic
gross = basic + da + hra
print("Gross Salary: ", gross)
