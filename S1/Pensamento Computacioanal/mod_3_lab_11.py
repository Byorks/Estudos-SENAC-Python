# 3.4.6   LAB   The basics of lists

# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
hat_list = [1, 2, 3, 4, 5]
print("Content of the hat ->", hat_list)

hat_list[2] = int(input("Enter a integer number to replace the  middle number of the hat: "))
print("New content of the hat ->", hat_list)

# write a line of code that removes the last element from the list (Step 2)
# Using instruction del
del hat_list[-1]
print("\nDeleted the last item from the hat->", hat_list)

# write a line of code that prints the length of the existing list (Step 3).
print("\nThe actual length of the hat list->", len(hat_list))