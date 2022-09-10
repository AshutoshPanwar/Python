# Dictionary in python

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    "CA" : 'San Francisco',
    "MI" : 'Detroit',
    "FL" : 'Jacksonville'
}

# Adding new items to list
cities[ 'NY' ] = "New York"
cities[ 'OR' ] = "Portland"

# Accessing value of keys
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print("*" * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# Accessing all elements of Dict
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbrrviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Taxas')

if not states:
    print("Sorry, no Taxes.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")