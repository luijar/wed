from google.appengine.ext import db
from google.appengine.api import users

class Guest(db.Model):
	first_name = db.StringProperty(required=True)
	last_name = db.StringProperty(required=True)
	guests = db.StringProperty(required=True)   #, choices=set([1,2,3,4,5,6,7,8,10])
	country = db.StringProperty(required=True)
	message = db.StringProperty()
	email = db.StringProperty(required=True)