# 3.5.3 The bubble sort – interactive version

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

del my_list

# Python can sort 
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# We can reverse the list
my_list.reverse()
print(my_list)

# Can arrange in alphabetic order
lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)

