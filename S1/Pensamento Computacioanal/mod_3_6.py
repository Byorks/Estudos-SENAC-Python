list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# The output -> 2
# because in the case of a list, it stores the location in memory, as if pointing to a place
# to effectively copy
list_2 = list_1.copy()
# or
list_2 = list_1[:]

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[0:6]
print(new_list)

# if the first parameter is omitted, it is as if the start number were 0my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# del can delete a slice too
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# deleting all elements from the list
del my_list[:]
print(my_list)

#deleting the list itself 
del my_list
