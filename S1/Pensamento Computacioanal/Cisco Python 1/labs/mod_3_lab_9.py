# 3.2.14   LAB   Essentials of the while loop

total_blocks = blocks = int(input('Enter the number of blocks: '))

# Write your code here.
height = 0

# First I need to take one block and after two from the number os total blocks
# I need to remove the blocks I am pulling to the pyramid

for i in range(1, total_blocks + 1):
    print('Remaining blocks ->',blocks)
    if blocks >= i:
        blocks -= i
        height += 1
    else: 
        print('\nThere aren\'t insufficient blocks')
        break

print('The height of the pyramid:', height)
