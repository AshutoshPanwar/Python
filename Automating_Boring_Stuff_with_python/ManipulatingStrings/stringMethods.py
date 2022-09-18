spam = "Hello, World!"

print("spam.upper():")
print(spam.upper())

print("spam.lower():")
print(spam.lower())

print("spam.isupper():")
print(spam.isupper())

print("spam.islower():")
print(spam.islower())

print("hello.isalpha():")
print("hello".isalpha())

print("Hello123.isalnum():")
print("Hello123".isalnum())

print("123.isdecimal():")
print("123".isdecimal())

print(" .isspace():")
print(" ".isspace())

print("This Is Title Case.istitle():")
print("This Is Title Case".istitle())

print("Hello, World!.startswith('Hello'):")
print("Hello, World!".startswith('Hello'))

print("Hello, World!.endswith('Hello'):")
print("Hello, World!".endswith('Hello'))

print("Hello, World!.startswith('Hello, World!'):")
print("Hello, World!".startswith('Hello, World!'))

print("Hello, World!.endswith('Hello, World!'):")
print("Hello, World!".endswith('Hello, World!'))

# join() and split() Methods
spam = "My name is Simon".split(' ')
print("My name is Simon.split(' '):")
print(spam)

print('", ".join(spam):')
print(", ".join(spam))
print("###".join(spam))