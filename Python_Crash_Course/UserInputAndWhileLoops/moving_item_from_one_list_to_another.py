# Moving items from one list to another.

unconformed_users = ['alice', 'brian', 'candace']
conformed_users = []

while unconformed_users:
    current_user = unconformed_users.pop()
    print(f"Verified user: {current_user.title()}")
    conformed_users.append(current_user)

print("\nThe following user have been conformed:")
for conformed_user in conformed_users:
    print(conformed_user.title())