sentence = "Python is a powerful programming language that is easy to learn and use"
word = "Python"

print("Length of sentence:", len(sentence))
print("Index of first occurrence:", sentence.index(word))
print("Number of times word appears:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

new_sentence = sentence.replace("Python", "Java")
print("After replacement:", new_sentence)

print("Last character:", sentence[-1])
