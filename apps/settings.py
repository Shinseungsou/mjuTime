import os

# from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


class Config(object):
	# Set secret keys for CSRF protection
	SECRET_KEY = "likelion-flaskr-secret-key"
	# CSRF_SESSION_KEY = SESSION_KEY
	debug = False


class Production(Config):
	debug = True
	CSRF_ENABLED = False
	ADMIN = "wwwww43211@gmail.com"
	SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///mjutime?instance=mjutime:mjutt'
	migration_directory = 'migrations'