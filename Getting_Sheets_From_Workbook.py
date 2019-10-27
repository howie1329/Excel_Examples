import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

#* Get name of worksheets
print(wb.get_sheet_names())

#* Get Worksheet Object
sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
print(sheet.title)

#* See Active worksheet in excel
anothersheet = wb.active
print(anothersheet)