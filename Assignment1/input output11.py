'''Q. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn 
is input through the keyboard in hundreds, find the total number of currency notes of each
denomination the cashier will have to give to the withdrawer.'''

amount = int(input("Enter the amount to withdraw (in hundreds): "))
hundred_notes = amount // 100
remaining_amount = amount % 100
fifty_notes = remaining_amount // 50
remaining_amount = remaining_amount % 50
ten_notes = remaining_amount // 10
print("100 denomination notes: ",hundred_notes)
print("50 denomination notes: ",fifty_notes)
print("10 denomination notes: ",ten_notes)
