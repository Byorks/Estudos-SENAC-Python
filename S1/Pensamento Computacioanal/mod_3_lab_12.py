# 3.4.11   LAB   The basics of lists ‒ the Beatles

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(0,2):
    beatles.append(input())
print("Step 3:", beatles)

# step 4
print("Step 4:", beatles)
for i in beatles:
    if beatles[i] == 'Stu Sutcliffe':
        del(beatles[1])
    elif beatles[i] == 'Pete Best':
        del(beatles[i])
# step 5
print("Step 5:", beatles)
beatles.insert(0, "Ringo Star")

# testing list length
print("The Fab", len(beatles))

