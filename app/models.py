#imports
from . import db
from uuid import uuid4
from datetime import datetime


class Emails(db.Model):
    id = db.Column(db.String(32), default=lambda: str(uuid4().hex), primary_key=True)
    email = db.Column(db.String(60), unique=True)
    signup_ip = db.Column(db.String(20))
    signup_browser = db.Column(db.String(120)) 
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.String(10), default="active") 

    