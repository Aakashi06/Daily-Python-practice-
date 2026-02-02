n = 5  # number of rows

for i in range(n):
    # print leading spaces
    print(" " * (n - i - 1), end="")
    
    # print stars
    print("*" * (2 * i + 1))
