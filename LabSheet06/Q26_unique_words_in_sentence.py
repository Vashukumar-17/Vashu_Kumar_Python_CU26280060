# Find unique words, ignoring case and common punctuation
import string

sentence = input("Enter a sentence: ").casefold()
translator = str.maketrans("", "", string.punctuation)
words = sentence.translate(translator).split()
print("Unique words:", set(words))
