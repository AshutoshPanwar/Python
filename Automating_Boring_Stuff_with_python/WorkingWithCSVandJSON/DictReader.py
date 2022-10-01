# Accessing column items with heading name
import csv

exampleFile = open('SampleCSV.csv')     # Open File
exampleDictReader = csv.DictReader(exampleFile)     # DictReader store data in key-value format

for row in exampleDictReader:
    print(row['SampleCSV'])     # Print all items under SampleCSV