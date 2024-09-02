def print_pattern(size):
    # Upper half
    for i in range(size):
        for j in range(2*size):
            if j == size-i or j == size+i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half
    for i in range(size-2, -1, -1):
        for j in range(2*size):
            if j == size-i or j == size+i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Change the size as needed
print_pattern(4)
