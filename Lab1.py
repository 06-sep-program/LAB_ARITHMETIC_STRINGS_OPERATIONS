price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Price of item:" , price)
print("Quantity:" , quantity)
print("Tax rate:" , tax_rate * 100)

print(" ")

print("Subtotal:" , "$" + str(round(subtotal,2)))
print("Tax:" , "$" + str(round(tax,2)))
print("Total:" , "$" + str(round(total,2)))