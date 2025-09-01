# Mod 3 Section 1
# Conditions 
# Simple condition
if true_or_false_condition:
	perform_if_condition_true
else:
	perform_if_condition_false
 
# Condition with elif
if the_weather_is_good:
	go_for_a_walk()
elif tickets_are_available:
	go_to_the_theater()
elif table_is_available:
	go_for_lunch()
else:
	play_chess_at_home()
 
 
 # Analyzing two examples - both do the same thing analyse a number and tells the bigger 
 # Example 1
 # Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)

# Example 2
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2
# in resume a shorter version, if we have a one line instruction we can do this 