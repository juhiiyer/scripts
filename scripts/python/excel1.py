#!/usr/bin/python3.5
import xlrd
loc = ("/500gb1/juhiPython/scripts/python/employee.xlsx")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
print(sheet.nrows,sheet.ncols)

for i in range(sheet.nrows):
	print()
	for j in range(sheet.ncols):
		print(sheet.cell_value(i,j),end='')
		# print ()
#people send thingi in json files
