secret_number = 777

# Multi-line printing
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_input = None

while secret_number != user_input:
   user_input = int(input("Type the possible secret number: "))
   
   if secret_number != user_input:
       print("Ha ha! You're stuck in my loop!")
   else:
       print("Well done, muggle! You are free now")
   


