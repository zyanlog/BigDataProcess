#!/usr/bin/python3
from openpyxl import load_workbook

wb = load_workbook(filename = 'student.xlsx')
ws = wb['Sheet1']

totalList = []
for row in ws.iter_rows(min_row=2):
	midterm = row[2].value
	final = row[3].value
	homework = row[4].value
	attendance = row[5].value

	sum = midterm * 0.3 + final * 0.35 + homework * 0.34 + attendance

	row[6].value = sum
	totalList.append(sum)

totalList.sort(reverse=True)

ap = totalList[int(len(totalList) * 0.15) - 1]
a = totalList[int(len(totalList) * 0.3) - 1]
bp = totalList[int(len(totalList) * 0.5) - 1]
b = totalList[int(len(totalList) * 0.7) - 1]

count = 0
for row in ws.iter_rows(min_row=2):
	if row[6].value < 40:
		row[7].value = 'F'
	elif row[6].value >= ap:
		row[7].value = 'A+'
	elif row[6].value >= a:
		row[7].value = 'A0'
	elif row[6].value >= bp:
		row[7].value = 'B+'
	elif row[6].value >= b:
		row[7].value = 'B0'
	else:
		count += 1

cp = totalList[int(len(totalList) * 0.7) - 1 + int(count * 0.5)]

for row in ws.iter_rows(min_row=2):
	if row[6].value < b and row[6].value > cp:
		row[7].value = 'C+'
	elif row[6].value == '':
		row[7].value = 'C0'

wb.save('student.xlsx')
