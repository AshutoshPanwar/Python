# Accessing column items with heading name
import csv

exampleFile = open('SampleCSV.csv')     # Open File
exampleDictReader = csv.DictReader(exampleFile, ['Loop-Down'])     # [AnyThing] Create alias of header value

for row in exampleDictReader:
    print(row['Loop'])     # Access value with alias value