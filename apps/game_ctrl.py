#-*- coding:utf-8-*-

from flask import render_template, Flask, request, url_for, redirect
from sqlalchemy import desc
from apps import app, db
from xlrd import open_workbook,cellname
import sys
import pusher

from apps.models import (
    Mafia_room
)

# need to add session


def allowed_file(filename):
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

	return '.' in filename and \
	filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def getKey():
	return pusher.Pusher(
			app_id = '92355',
			key = '7a374a8c50c22eddd116',
			secret = '6921451435cbdefaad9e'
		)

@app.route('/')
@app.route('/mafia')
def mafia_index():
	session
	return render_template("game/mafia/index.html", activity='mafia', name='hello')

@app.route('/mafia_game')
def mafia_game():
	room = request.args.get('roomNum')
	return render_template("game/mafia/index.html", activity='mafia')

@app.route('/mkRoom', methods=['POST'])
def mafia_mkroom():
	room = request.form('mkRoom_name')
	return render_template("game/mafia/index.html", activity='mafia')

@app.route('/send')
def sendmsg():
	p = getKey()

	chat_name = request.args.get('name_data')
	chat_msg = request.args.get('msg_data')
	p['newchannel'].trigger('event_msg', {'name':chat_name, 'msg' :chat_msg})

	return ""

@app.route('/jobsend')
def jobsendmsg():
	p = getKey()

	chat_name = request.args.get('name_data')
	chat_msg = request.args.get('msg_data')
	p['newchannel'].trigger('job_msg', {'name':chat_name, 'msg' :chat_msg})

	return ""