# Order matters when passing Arguments.

def describe_pet(animal_type, pet_name):        # Here (animal_type, pet_name) are parameters.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# Order of arguments matters
# Here ('hamstar', 'harry') are the arguments.
describe_pet('hamstar', 'harry')
describe_pet(pet_name='harry', animal_type='hamstar')
describe_pet("dog", "willie")