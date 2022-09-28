# Writing values to cell.

import openpyxl

wb = openpyxl.Workbook()        # New File
sheet = wb['Sheet']     # Adding new Sheet
sheet['A1'] = 'Hello, world!'       # Edit the cell values
print(sheet['A1'].values())     # Calling value from sheet