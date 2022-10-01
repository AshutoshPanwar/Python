# Observe order does not matter in tuples

import csv

outputFile = open('output.csv', 'w', newline='')
outputDictWrite = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWrite.writeheader()       # Add Header -> [Name', 'Pet', 'Phone']

# Add data under specific header
outputDictWrite.writerow({'Name' : 'Alias', 'Pet' : 'cat', 'Phone' : '555-555-555'})
outputDictWrite.writerow({'Name' : 'bob', 'Phone' : '555-000-555'})
outputDictWrite.writerow({ 'Phone' : '555-555-555', 'Name' : 'Carol', 'Pet' : 'Dog'})

# Close file
outputFile.close()
