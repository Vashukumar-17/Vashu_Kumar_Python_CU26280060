# Q20: Find the length of the longest word in a tuple

words = tuple(input("Enter words separated by spaces: ").split())

if len(words) == 0:
    print("The tuple is empty!")
else:
    longest_word = words[0]
    for word in words:
        # Keep the word that is longer than the current longest
        if len(word) > len(longest_word):
            longest_word = word

    print("Tuple               :", words)
    print("Longest word        :", longest_word)
    print("Length of that word :", len(longest_word))
