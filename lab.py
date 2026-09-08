price = 5.00
quantity = 6
tax_rate = 0.15

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"price of item : ${price}")
print(f"quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print()
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")   
print(f"Total: ${total}")
