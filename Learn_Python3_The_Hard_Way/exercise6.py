# String and text

# intiger calling in string format()
types_of_people = 10
x = f"There are {types_of_people} types of people."

# String calling in format() string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Checking output
print(x)
print(y)

# Calling strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Keywork calling in string format()
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

# Joining two strings
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
