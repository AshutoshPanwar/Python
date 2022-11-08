# (*) is one parameter that tell python to create empty tuple that collects as many arguments.

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza of the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, "mushroom", 'green peppers', 'extra cheese')
