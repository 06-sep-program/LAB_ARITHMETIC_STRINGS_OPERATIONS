

price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100:.1f}%")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

print("\n--------------------")
print("Bonus")
print("--------------------")

sentence = "Python is a powerful language and Python is easy to learn"
word = "Python"

print("Length of sentence:", len(sentence))
print("First index of word:", sentence.find(word))
print("Number of times word appears:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

new_sentence = sentence.replace(word, "Java")
print("After replacement:", new_sentence)

print("Last character:", sentence[-1])