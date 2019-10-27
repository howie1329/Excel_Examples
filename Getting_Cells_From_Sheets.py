import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')
print(sheet['A1'])

print(sheet['A1'].value)

c = sheet['B1']
a = ["a","b","c","d","e"]
print(c.value)
print(c.column)

print('Row ' + str(c.row) + ', Column ' + a[c.column - 1].capitalize() + ' is ' + c.value)

print("Cell " + c.coordinate + " is " + c.value)

print(sheet['C1'].value)