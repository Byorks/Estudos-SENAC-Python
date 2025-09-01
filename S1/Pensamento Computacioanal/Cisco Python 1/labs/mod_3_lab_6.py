# 3.2.7  LAB   The break statement – Stuck in a loop

# First attempt
words = None

while words != "chupacabra":
    words = input("Enter words: ")
    
print("You`ve successfully left the loop.")

# Secondly attempt
while True:
    more_words = input("Type more words; ")
    if more_words == "chupacabra": break
    
print("You`ve successfully left the loop.")