'''Q. A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 
6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 
days your membership will be cancelled. Write a program to accept the number of days the 
member is late to return the book and display the fine or the appropriate message.'''

days=int(input("How many days is the member late?:"))
if days<=5:
    print("The member has to pay fine of 50 paise.")
elif days>=6 and days<=10:
    print("The member has to pay fine of Rs 1.")
elif days>10 and days<30:
    print("The member has to pay fine of Rs 5.")
elif days>=30:
    print("Membership Cancelled.") 
