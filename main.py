price = 2.99
quantity = 3
tax_rate = 0.075  # 7.5%


subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax


print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%\n")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
