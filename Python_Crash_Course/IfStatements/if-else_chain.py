# if-elif-else chain for single value

print("Enter you age: ")
age = int(input())

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")