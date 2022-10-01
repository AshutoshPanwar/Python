import csv

csvFile = open('example.tsv', 'w', newline='')
csvWrite = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')       # delimiter-> tab after every value; lineterminator-> After every row

# Adding values
csvWrite.writerow(['apple', 'orange', 'grapes'])
csvWrite.writerow(['eggs', 'bacon', 'ham'])
csvWrite.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

# Close file
csvFile.close()