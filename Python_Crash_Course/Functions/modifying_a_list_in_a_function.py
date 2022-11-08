# Moving data from one list to another using function's

def print_modules(unprinted_designs, completed_modules):
    """
    Simulate printing each design, until none are left.
    More each design to completed_modules after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printed model: {current_design}")
        completed_modules.append(current_design)

def show_completed_modules(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_modules(unprinted_designs, completed_models)
show_completed_modules(completed_models)
