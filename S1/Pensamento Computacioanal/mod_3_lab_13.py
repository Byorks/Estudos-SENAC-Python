# 3.6.6 LAB Operating with lists ‒ basics

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in range(len(my_list) -1):
    for num in range(len(my_list) -1):
        if my_list[i] != my_list[-1]:
            if num == my_list[i + 1]:
                del my_list[i]
print("The list with unique elements only:")
print(my_list)

