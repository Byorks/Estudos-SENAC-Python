# 3.2.11   LAB   The continue statement – the Pretty Vowel Eater

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Type a word: ").upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else: word_without_vowels += letter
    # Complete the body of the loop.

# Print the word assigned to word_without_vowels.
print(word_without_vowels)