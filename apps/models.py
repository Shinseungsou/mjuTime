from apps import db

class Mafia_room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roomNum = db.Column(db.Integer)
	manager = db.Column(db.Text())