import csv

exampleFile = open('SampleCSV.csv')     # Open file
exampleReader = csv.reader(exampleFile)     # Read file

# Accessing data with for loop in nested list
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))       # Accessing line number with .line_num()