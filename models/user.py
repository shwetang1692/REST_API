import sqlite3
from db import db
class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) #maximum 80 characters
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod #Object is created using constructor
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod  #Object is created using constructor
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
