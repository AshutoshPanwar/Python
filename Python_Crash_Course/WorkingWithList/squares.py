# List of Squared number from 1-10.

# Naive apperoch
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# Better approch
squares1 = [value**2 for value in range(1,11)]
print(squares1)