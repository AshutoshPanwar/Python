# Iterating through List in python.
# No need to pass no of items in the list.
# Naming convention ( list->Plural, iterator->Singular)

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician},That was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show.")