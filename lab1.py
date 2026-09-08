price = 2.5
quantity = 5
tax_rate = 0.15

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax Rate: {tax_rate * 100}%\n")

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")