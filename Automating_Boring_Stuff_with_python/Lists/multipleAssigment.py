from sys import displayhook


cat = ['fat', 'gray', 'loud']

# Naive method of assigning list items
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size)
print(color)
print(disposition)

# Python style of assigning list items
size1, color1, disposition1 = cat
print(size1)
print(color1)
print(disposition1)