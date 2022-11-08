# Default values are used when user forget or don’t enter the arguments then function will take default values from parameters.
# Default values helps program to run smoothely.

def describe_pet(animal_type='elephant', pet_name='willie'):        # Here (animal_type, pet_name) are parameters.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamstar', 'harry')
describe_pet(pet_name='harry', animal_type='hamstar')
describe_pet("Lion")
describe_pet("dog", "willie")
describe_pet()