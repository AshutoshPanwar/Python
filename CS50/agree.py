# Program to input
# if user agree or not

# Prompt user for input
s = input("Do you agree? ").lower()     # Converting complete string to lowecase to reduce P&C

# Conditional
if s in ['y', 'yes']:
    print("Agreed!")
else:
    print("Don't Agree!")