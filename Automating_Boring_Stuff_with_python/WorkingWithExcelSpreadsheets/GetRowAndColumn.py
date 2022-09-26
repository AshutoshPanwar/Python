import openpyxl

wb = openpyxl.load_workbook('example.xlsx')     # Load File
sheet = wb['Sheet1']        # Specifit sheet in file

for rowOfCellObjects in sheet['A1' : 'C3']:     # Iterating to all columns
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- End of Row ---')