# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

print(in_range(2, 5, 6))
print(in_range(6, 5, 8))