'''Q. If cost price and selling price of an item is input through the keyboard, write a program to 
determine whether the seller has made profit or incurred loss. Also determine how much profit 
he made or loss he incurred.'''

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    print("Profit:", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss:", cost_price - selling_price)
else:
    print("No profit, no loss.")
