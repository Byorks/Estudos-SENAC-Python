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

# adding element to the end of the list
numbers.append(4)
print(numbers)

# adding element where I choose the location
numbers.insert(0, 232)
print(numbers)
print("The length increased by 1 =>", len(numbers))

# creating list and inserting numbers
empty_list = []

for i in range(6):
    empty_list.append(i + 1)
    
print(empty_list)

# using for to sum the elements from the list 
my_list = [10, 32, 34, 1, 9]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
    
print("Total =", my_list)
print(my_list)

my_list = [0, 1, 2, 3, 4]

total = 0

# the lens is not needed 
# for in list the i is the my_list content
# equal a foreach
for i in my_list:
    print(i)
    total += i
    
print(total)