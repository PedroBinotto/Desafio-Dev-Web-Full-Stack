import os
import pymysql

class Config:
	# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senha@localhost/app'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

