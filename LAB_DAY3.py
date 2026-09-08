Price:float =2.99
Quantity:int = 3
Tax_rate:float = 7.5

print(f"Price of item: ${Price}")
print(f"Quantity: {Quantity}")
print(f"Tax rate: {Tax_rate} %")


print()

subtotal:float = ((Price )* float(Quantity) ) 
Tax : float = (subtotal* Tax_rate) /100
Total : float = subtotal + Tax 

print(f"subTotal: ${subtotal: .2f}")
print(f"Tax: ${Tax: .2f}")
print(f"Total: ${Total: .2f}")
 