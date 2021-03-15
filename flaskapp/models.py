from flaskapp import db
from flask import redirect, url_for, current_app
from datetime import datetime
try:
	import simplejson as json
except:
	import json

class Record(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	num1 = db.Column(db.Integer, nullable=False)
	num2 = db.Column(db.Integer, nullable=False)
	date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

