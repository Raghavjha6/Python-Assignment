'''Q. If the total selling price of 15 items and the total profit earned on them is input through the 
keyboard, write a program to find the cost price of one item.'''

selling_price = float(input("Enter total selling price of 15 items: "))
profit = float(input("Enter total profit: "))
cost_price = selling_price - profit
cp_per_item = cost_price / 15
print("Cost price of one item: ", cp_per_item)
