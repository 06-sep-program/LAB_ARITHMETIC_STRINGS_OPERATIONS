# <!-- Bonus, create a new python file and do the following:
# Define a string variable containing a sentence with at least 10 words.
# Define a string variable containing a word that appears in the sentence.
# Print the length of the sentence.
# Print the index of the first occurrence of the word in the sentence.
# Print the number of times the word appears in the sentence.
# Print the sentence in all uppercase letters.
# Print the sentence in all lowercase letters.
# Replace the word in the sentence with a new word of your choice.
# Print the last character of the sentence. -->



sentence: str = "Saudi Arabia is a very beautiful country with rich culture"
word: str = "beautiful"

print(len(sentence))
print(sentence.find(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(word ,  "amazing"))
print(sentence[-1])
