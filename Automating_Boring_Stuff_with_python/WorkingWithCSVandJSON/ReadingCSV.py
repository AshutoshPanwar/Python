import csv

exampelFile = open('SampleCSV.csv')     # Open CSV
exampleRead = csv.reader(exampelFile)       # Read CSV
exampleData = list(exampleRead)         # Convert data to list format

print(exampleData)      # Print data