import csv

outputFile = open('output.csv', 'w', newline='')        # Create a new file in write mode

print("Creating a file with name: output.csv")
outputWrite = csv.writer(outputFile)        # Write to file

# Append to file
outputWrite.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWrite.writerow(['Hello, World!', 'eggs', 'bacon', 'ham'])
outputWrite.writerow([1, 2, 3.145, 4])

# Close file
outputFile.close()