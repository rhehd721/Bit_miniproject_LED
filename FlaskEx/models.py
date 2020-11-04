from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Myuser(db.Model):
    __tablename__='myuser'
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username=db.Column(db.String(8))

# LED 관련 DB
class LED(db.Model):
    __tablename__='LED'
    id = db.Column(db.Integer,primary_key=True)
    red = db.Column(db.String(2))
    green = db.Column(db.String(2))
    yellow = db.Column(db.String(2))
    time = db.Column(db.String(30))
    
    

