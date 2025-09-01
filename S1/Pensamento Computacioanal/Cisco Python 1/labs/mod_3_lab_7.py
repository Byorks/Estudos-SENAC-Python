# 3.2.10   LAB   The continue statement – the Ugly Vowel Eater

# continue can be used both with while and for loops
# It skips the actual block code and passes to the next loop

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    else:
        print(letter)
    # Complete the body of the for loop.

