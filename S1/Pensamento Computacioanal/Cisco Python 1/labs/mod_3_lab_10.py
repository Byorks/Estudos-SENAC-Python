# 3.2.15   LAB   Collatz's hypothesis
user_input = int(input("Type a number: "))
c0 = user_input
counter = 0

while True: 
    counter +=1    
    if c0 % 2 == 0:
        c0 //= 2
    else: 
        c0 = 3 * c0 + 1
    if c0 == 1:
        print(c0) 
        break
    print(c0)

print("steps =", counter)
        