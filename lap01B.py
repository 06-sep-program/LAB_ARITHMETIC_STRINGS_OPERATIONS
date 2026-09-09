
sentence = "I like to eat pizza with my family every single Friday"

word = "pizza"

print("Length of sentence:",len(sentence))

print("Index of first occurrence:",sentence.find(word))

print("Number of times word appears:",sentence.count(word))

print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

# Replace the word 
new_word = "burger"
print("Sentence after replacing word:", sentence.replace(word, new_word))

print("Last character:", sentence[-1])