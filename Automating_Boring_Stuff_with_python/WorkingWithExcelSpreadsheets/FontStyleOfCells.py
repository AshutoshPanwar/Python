import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']

italic24Font = Font(size=24, italic=True)       # Create a font
sheet['A1'].font = italic24Font     # Apply the font to A1
sheet['A1'] = 'Hello, world!'

italic24Font = Font(size=24, italic=True)       # Create a font
sheet['B3'].font = italic24Font     # Apply the font to A1
sheet['B3'] = '24 pt Italic'

print('New file is created with name: Styles.xlsx')
wb.save('Styles.xlsx')