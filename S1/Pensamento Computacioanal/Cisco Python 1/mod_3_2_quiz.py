# 3.2.17 SECTION QUIZ

# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
print("=== Question 1 ===")
for i in range(1, 11):
    if i % 2 != 0:  print(i)


# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
print("=== Question 2 ===")
x = 1
while x < 11:
    if x % 2 != 0: print(x)
    x +=1
    
# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
print("=== Question 3 ===")
email = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    email +=ch
print(email)

# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
print("=== Question 4 ===")
new_digits = ""
for digit in "0165031806510":
    if digit == "0":
        new_digits += "x"
    else:
        new_digits += digit
        
print(new_digits)

print("Second solution")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")