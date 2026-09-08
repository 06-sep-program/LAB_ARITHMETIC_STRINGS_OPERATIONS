price = 2.99
quantity = 3
taxRate = 0.075
subtotal = price * quantity
tax = subtotal * taxRate
total = subtotal + tax
print(f"Price of item: $ {price}")
print(f"Quantity: {quantity}")
print(f"tax rate: 7.5%")
print (f"subtotal: {subtotal}")
print(f"tax: {tax:.2f}")
print(f"total: {total:.2f}")