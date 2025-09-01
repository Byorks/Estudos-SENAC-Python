# ------ Module 3 Section 2 ------

# Loops

# for loop with range function
for i in range(10):
    print("The value of i is currently", i)

# Range with two arguments, the first is the initial point, the second is the end but not self included
for i in range(3, 6):
    print("The value of i is currently", i)
    
# Range with three arguments, the third is incremental value, de default is 1
for i in range(2, 8, 3):
    print("The value of i is currently", i)
    
    
# ----- Break and Continue Examples ------

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

