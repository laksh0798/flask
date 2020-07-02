from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_ssnId = db.Column(db.Integer, nullable=False)
    patient_name = db.Column(db.String(50), nullable=False)
    patient_age = db.Column(db.Integer)
    date_admission = db.Column(db.DateTime, default=datetime.now)
    bed_type = db.Column(db.String(50))
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    status = db.Column(db.String(50))

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_ssnId = db.Column(db.Integer, nullable=False)
    medicine_id=db.Column(db.Integer, nullable=False)
    qty=db.Column(db.Integer, nullable=False)
    
class MedicineStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_id=db.Column(db.Integer, nullable=False)
    medicine_name=db.Column(db.String(50))
    qty=db.Column(db.Integer, nullable=False)
    rate=db.Column(db.Integer, nullable=False)