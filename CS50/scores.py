# Program to find
# average of three numbers

# Declaring empty list
scores = []

# Taking three inputs form user
for i in range(3):
    scores.append(int(input("Enter: ")))

# Finding Average
average = sum(scores) / len(scores)         # Using pre-defined functions sum() and len()
print(f"Average {average}")