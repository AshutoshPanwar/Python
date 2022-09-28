# Get all values of a column.

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')     # Load Sheet
sheet = wb.active

for cellObj in list(sheet.columns)[1]:      # Iterating and printing each column values.
    print(cellObj.value)