size = 25
gap = 3

for x in range(10):
    for i in range(size):
        spaces_on = [(i+k) % size for k in range(gap)]
        for j in range(size):
            if j in spaces_on:
                print(end="  ")
            else:
                print("*", end=" ")

        print()
