#-*- coding:utf-8-*-

from flask import render_template, Flask, request, url_for, redirect
from sqlalchemy import desc
from apps import app, db
from xlrd import open_workbook,cellname
import sys

from apps.models import (
    Mafia_room
)




def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", activity='index')

@app.route('/index2')
def index2():
	return render_template("index2.html", activity='index2')

@app.route('/index3')
def index3():
	return render_template("index3.html", activity='index3')
	
@app.route('/ttable')
def upload():
	return redirect(url_for('uplodexls'))

#file upload
@app.route('/uplodexls')
def uplodexls():
	return render_template("uploadxls.html")

#find and make TT
@app.route('/uploading', methods=['POST'])
def uploading():
	excel = request.files['xlsFlie']
	subject = request.form['subject']
	year = request.form['year']
	semester = request.form['semester']
	text = request.form['text']

	if not excel : 
		messages = "please select excel file"

	elif not subject : 
		messages = "please type subject"
	elif not year : 
		messages = "please type year"
	elif not semester : 
		messages = "please type semester"
	else : 
		upload_data = ClassTTxls(
			xlsfile = excel,
			subject = subject,
			year = year,
			semester = semester,
			text = text
		)
		db.session.add(upload_data)
		db.session.commit()


		messages = "upload success"

	return render_template("uploadxls.html", messages=messages)


def xlsParsing(book):
	sheet = book.sheet_by_index(0)

	'''
	room : room for class
	froom : flag for room for and if
	'''


	froom = False
	room_and_time = 11
	col = 5
	allClassList = []



	line = 0
	num = 0
	for row_index in range(sheet.nrows):
		classList = []
		if sheet.cell(row_index,room_and_time).value == '' :
			continue
		elif sheet.cell(row_index,1).value == u'학년' :
			continue
		else:
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
				fclass = 10
				lclass = 10
				fclass = ((sheet.cell(row_index,room_and_time).value[1:3]))
				lclass = ((sheet.cell(row_index,room_and_time).value[7:9]))
				room = ''
				for i in range(len(sheet.cell(row_index,room_and_time).value)):
					if sheet.cell(row_index,room_and_time).value[i] == ')':
						froom = False
						break
					elif sheet.cell(row_index,room_and_time).value[i] == '(':
						froom = True
					elif froom :
						room += sheet.cell(row_index,room_and_time).value[i]
			nowcode = 0
			beforecode = 0

			if isinstance(sheet.cell(row_index, 9).value, float):
				nowcode = int(sheet.cell(row_index, 9).value)
			elif isinstance(sheet.cell(row_index, 9).value, int):
				newcode = sheet.cell(row_index, 9)
			elif len(sheet.cell(row_index, 9).value) > 0:
				if isinstance(sheet.cell(row_index, 9).value, str):
					nowcode = int(float(unicode(sheet.cell(row_index, 9).value)))
				elif isinstance(sheet.cell(row_index, 9).value, unicode):
					nowcode = int(float(sheet.cell(row_index, 9).value))

			if sheet.cell(row_index - 1, 9).value == "강좌번호":
				if isinstance(sheet.cell(row_index - 1, 9).value, float):
					nowcode = int(sheet.cell(row_index - 1, 9).value)
				elif isinstance(sheet.cell(row_index - 1, 9).value, int):
					newcode = sheet.cell(row_index - 1, 9)
				elif len(sheet.cell(row_index - 1, 9).value) > 0:
					if isinstance(sheet.cell(row_index - 1, 9).value, str):
						nowcode = int(float(unicode(sheet.cell(row_index - 1, 9).value)))
					elif isinstance(sheet.cell(row_index - 1, 9).value, unicode):
						nowcode = int(float(sheet.cell(row_index - 1, 9).value))

			if nowcode != beforecode : 
				num += 1
			line += 1
			classList.append(line)
			classList.append(num)
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

	#end for
	return allClassList

@app.route('/static')
def updateStatic():

	#excel = open_workbook()

	# book = open_workbook(excel.filename, sys.stdout,0,1)
	book = open_workbook('/static/xls/example.xls')
	allClassList = xlsParsing(book)

	print allClassList
	return render_template("checkTT.html", classList=allClassList)


@app.route('/update', methods=['POST', 'GET'])
def update():
	if request.method == 'POST':
		excel = request.files['xlsFlie']

	# book = open_workbook(excel.filename, sys.stdout,0,1)
		book = open_workbook(file_contents=excel.read())
		allClassList = xlsParsing(book)

		print allClassList
		return render_template("checkTT.html", classList=allClassList)
	else :
		return render_template("checkTT.html")



#bug report

@app.route('/bug', methods=['GET'])
def bugreport():
	result = Report.query.all()
	return render_template("bug.html", all_list=result)

@app.route('/upload', methods=['POST'])
def upload_db():
	post_photo = request.files['photo']
	post_text = request.form['text']

	messages = []


	if post_text: # 텍스트는 무조건 입력해야한다.
		if len(post_text) > 200: # 코멘트가 너무 길면 
			messages.append( "text are too long" )

		elif post_photo: # 코멘트가 길지도 않고, 이미지가 있으면
			filestream = post_photo.read()

			if not allowed_file(post_photo.filename): # 이미지 형식이 아니면
				messages.append( "please upload valid image file" )

			elif len(filestream) > 1024 * 1024: # 파일 크기가 크면
				messages.append( "please upload image size under 1M" )

			else:# 제대로 된 이미지 형식이고 파일 크기가 1M 이하이면
				upload_data = Report(
					photo = filestream,
					text = post_text
				)
				
				db.session.add(upload_data)
				db.session.commit()

				messages.append( "image and text are uploaded!" )

		else: # 이미지가 없으면
			upload_data = Report(
				photo = 0,
				text = post_text
			)

			db.session.add(upload_data)
			db.session.commit()

			messages.append( "text are uploaded" )

	else: # 텍스트가 없으면
		messages.append( "please enter text" )
	result = Report.query.all()
	return render_template("bug.html", messages=messages, all_list=result)



@app.route('/show/<key>')
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.photo)

