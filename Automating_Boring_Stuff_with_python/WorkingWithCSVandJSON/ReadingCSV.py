import csv

exampelFile = open('SampleCSV.csv')     # Open CSV
exampleRead = csv.reader(exampelFile)       # Read CSV
exampleData = list(exampleRead)         # Convert data to list format

print(exampleData)      # Print data

print("Accessing specific data:")
print(exampleData[0][0])
print(exampleData[1][1])
print(exampleData[1][2])
print(exampleData[2][1])
print(exampleData[6][1])