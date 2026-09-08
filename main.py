# 1. Define variables
price = 2.99
quantity = 3
tax_rate = 0.075

# 2. Perform calculations
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# 3. Print output formatted as currency
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%\n")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")