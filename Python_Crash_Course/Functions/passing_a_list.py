# Passing a list an argument.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}."
        print(msg)

username = ['hannah', 'khana', 'yash']
greet_users(username)