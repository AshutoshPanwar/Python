# Excel File operations.

import openpyxl

wb = openpyxl.Workbook()        # New file
sheet = wb.active       # Load Sheet

sheet['A1'] = 200       # Adding data
sheet['A2'] = 300       # Adding data

sheet['A3'] = 'SUM(A1:A2)'      # Set the Formula.

print("New file is created with name: writeFormula.xlsx")
wb.save('writeFormula.xlsx')
