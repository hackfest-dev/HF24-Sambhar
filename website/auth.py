from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print("Hello")
        email  = request.form.get('email')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged In Successfully',category='success')
                login_user(user,remember=True)
                return redirect(url_for('myViews.home'))
            else:
                flash('Incorrect password,try again.',category='error')  
        else:
            flash('Email does not exists,ask administrator to create a new user.',category='Error')
        
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 

@auth.route('/Home')
def home():
    return render_template("home.html")