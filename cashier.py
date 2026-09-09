# Reema Alfaleh's Lab Submission (casier part)

price = 2.99 # the cost of the item the customer is purchasing
quantity = 3 # the number of items the customer is purchasing
tax_rate = 7.5/100 # the tax rate in your area 

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

pricePhrase = f"Price of item: {price} $ "
print(pricePhrase)

quantityPhrase = f"Quantity: {quantity} "
print(quantityPhrase)

tax_ratePhrase = f"Tax rate: {tax_rate * 100}%"
print(tax_ratePhrase)

print() # new line

subtotalPhrase = f"Subtotal: {subtotal}$ "
print(subtotalPhrase)

taxPhrase = f"Tax: {tax:.2f}$ "
print(taxPhrase)

totalPhrase = f"Total: {total:.2f}$"
print(totalPhrase)