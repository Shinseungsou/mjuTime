#-*- coding:utf-8-*-
from xlrd import open_workbook,cellname
import sys

book = open_workbook('example1.xls')
sheet = book.sheet_by_index(0)

print sheet.name

print sheet.nrows
print sheet.ncols

print sys.stdin.encoding
print sys.stdout.encoding

'''
room : room for class
froom : flag for room for and if
'''


froom = False
room_and_time = 11
col = 5
allClassList = []




for row_index in range(sheet.nrows):
	classList = []
	if sheet.cell(row_index,room_and_time).value == '' :
		continue
	elif sheet.cell(row_index,1).value == u'학년' :
		continue

	if sheet.cell(row_index,1).value != '':
		grade = sheet.cell(row_index,1).value
	if sheet.cell(row_index,2).value != '':
		lecture = sheet.cell(row_index,2).value
	if sheet.cell(row_index,5).value != '':
		lecturePoint = sheet.cell(row_index,5).value
	if sheet.cell(row_index,6).value != '':
		classTime = sheet.cell(row_index,6).value
	if sheet.cell(row_index,7).value != '':
		prof = sheet.cell(row_index,7).value
	if sheet.cell(row_index,9).value != '':
		lectureNum = sheet.cell(row_index,9).value
	if sheet.cell(row_index,10).value != '':
		limit = sheet.cell(row_index,10).value


	if sheet.cell(row_index,room_and_time).value != '' :
		week = sheet.cell(row_index,room_and_time).value[0]
		fclass = int(sheet.cell(row_index,room_and_time).value[1] + sheet.cell(row_index,room_and_time).value[2])
		lclass = int(sheet.cell(row_index,room_and_time).value[7] + sheet.cell(row_index,room_and_time).value[8])
		room = ''
		for i in range(len(sheet.cell(row_index,room_and_time).value)):
			if sheet.cell(row_index,room_and_time).value[i] == ')':
				froom = False
				break
			elif sheet.cell(row_index,room_and_time).value[i] == '(':
				froom = True
			elif froom :
				room += sheet.cell(row_index,room_and_time).value[i]

	classList.append(grade)
	classList.append(lecture)
	classList.append(lecturePoint)
	classList.append(classTime)
	classList.append(prof)
	classList.append(lectureNum)
	classList.append(limit)
	classList.append(week)
	classList.append(fclass)
	classList.append(lclass)
	classList.append(room)
	allClassList.append(classList)
	# for col_index in range(sheet.ncols) :
	# 	if sheet.cell(row_index,col_index).value != '' :
	# 		print cellname(row_index,col_index),'(',row_index,',',col_index,')-',
	# 		print sheet.cell(row_index,col_index).value
print allClassList