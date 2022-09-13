def spam():
    eggs = 'spam local'     # spam() local variable
    print(eggs)

def bacon():
    eggs = 'bacon local'        # bacon() local variable
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'     # Global variable
bacon()
print(eggs)