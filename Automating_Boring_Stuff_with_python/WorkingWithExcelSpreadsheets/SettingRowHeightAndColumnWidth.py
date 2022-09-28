
import openpyxl
wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'

sheet.row_dimensions[1].height = 70     # Height of first row
sheet.column_dimensions['B'].width = 20     # Width of second Column

wb.save('dimensions.xlsx')