# Q3. Count word frequency after converting the sentence to lowercase.

sentence = input("Enter a sentence: ").lower()
frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(f"{word}: {count}")
