
price =5.60
quantity=2
tax_rate=0.15
subtotal= round(price*quantity,2)
tax=round(tax_rate*subtotal,2)
total=round(subtotal+ tax,2)

print(f"Price of item: $ {price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print()
print(f"Subtotal:${subtotal}")
print(f"tax:${tax}")
print(f"total:${total}")