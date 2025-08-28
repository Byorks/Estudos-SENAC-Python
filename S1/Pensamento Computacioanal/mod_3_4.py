# ------ Module 3 Section 4  ------

# Lists

# Changing element a chosen from the list
numbers = [10, 5, 7 ,2, 1]
print("Original list contents:", numbers)

numbers[0] = 111
print("New list contents:", numbers)

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

# printing one element
print(numbers[3]) # print -> 2

print("\nList length:", len(numbers))  # Printing the list's length.

# removing the second element from the list
del numbers[1]
print(len(numbers))
print(numbers)

# the last item from the list
numbers = [111, 7, 2, 1]
print(numbers[-1])


# the one before last in the list
numbers = [111, 7, 2, 1]
print(numbers[-2])
