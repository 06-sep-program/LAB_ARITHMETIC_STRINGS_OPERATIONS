#Grocery store prograrm
price = 2.99
quantity = 3
tax_rate_For_Print = 7.5
tax_rate=0.075
subtotal= quantity * price
tax=subtotal * tax_rate
TotalCost= tax + subtotal
print("Price of the item:",price)
print("Quantity:",quantity)
print("Tax rate: %",tax_rate_For_Print)

print("Subtotal:$",subtotal)
print("Tax:$",tax)
print("Total:$",TotalCost)