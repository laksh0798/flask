from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User,Patient
from . import db
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/create-patient', methods=['POST'])
@login_required
def create_patient():
    if request.method == 'POST':
        c_patient = Patient(patient_ssnId = request.form.get('patient_id'),
                        patient_name = request.form.get('patient_name'), 
                        patient_age = request.form.get('patient_age'),
                        bed_type = request.form.get('type_of_bed'),
                        address = request.form.get('address'),
                        city = request.form.get('city'),
                        state= request.form.get('stt'),
                        status = "Active" ) 
        db.session.add(c_patient)
        db.session.commit()

    return '<h1>Added New User!<h1>'
