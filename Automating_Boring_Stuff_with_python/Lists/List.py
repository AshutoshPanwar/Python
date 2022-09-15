# Declearing list
spam = ['cat', 'bat', 'rat', 'elephant']

# Accessing each elements of list with index
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

# spam[0] is evaluated as 'cat'
print('Hello, ' + spam[0])

# List index only except int
print(spam[int(1.0)])

# Negative index
print(spam[-1])
print(spam[-3])

# Slicing in python
print(spam[:4])
print(spam[:])

# No of items in a list
print(len(spam))

# List are mutable
print(spam[0])
spam[0] = 'mutuable'
print(spam[0])

# Concatenating list
print([1,2,3] + spam)
print([1,2,3] * 3)

# Delete item form list
del spam[2]
print(spam)