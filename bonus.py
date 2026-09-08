sentence = "Learning Python with VS Code is very fun and Python helps me code"
target_word = "Python"
new_word = "Java"

print("Sentence Length:", len(sentence))
print("First Index of word:", sentence.find(target_word))
print("Word Count:", sentence.count(target_word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

replaced_sentence = sentence.replace(target_word, new_word)
print("Replaced Sentence:", replaced_sentence)
print("Last Character:", sentence[-1])
