from decimal import Decimal

price= Decimal("2.99")
quantity= 3
tax_rate= Decimal("7.5")
subtotal = (price * quantity).quantize(Decimal("0.01"))
tax = (subtotal * tax_rate / Decimal("100")).quantize(Decimal("0.01"))
total = (subtotal + tax).quantize(Decimal("0.01"))

print("###########  FIRST LAB  ###########")
print("Price of item", price, "$")
print("Quantity", quantity, "$")
print("Tax rate", tax_rate, "%")
print("Subtotal", subtotal, "$")
print("Tax", tax, "$")
print("Total costs", total, "$")


## Bonus, create a new python file and do the following:
favorite_anime: str = "My favorite anime is Gintama"
Hobby: str = "Gintama"

print("###########  BONUS LAB  ###########")
print("Length of sentence:", len(favorite_anime))
print("Number of words:", len(favorite_anime.split()))
print("Index of first occurrence:", favorite_anime.index(Hobby))
print("Number of times the word appears:", favorite_anime.count(Hobby))
print("Uppercase:", favorite_anime.upper())
print("Lowercase:", favorite_anime.lower())

new_sentence = favorite_anime.replace(Hobby, "Attack on Titan")
print("New sentence:", new_sentence)
print("Last character:", favorite_anime[-1])
