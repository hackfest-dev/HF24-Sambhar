from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import sqlite3

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
            flash('Email does not exists',category='error')
        
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/inventory')
def inventory():
    return render_template("inventory.html")

@auth.route('/addtoinventory')
def addtoinventory():
    return render_template("addtoinventory.html")

@auth.route('/updateinventory')
def updateinventory():
    return render_template("updateinventory.html")

@auth.route('/salesPurchases')
def salesPurchases():
    return render_template("sales.html")

@auth.route('/setting')
def setting():
    return render_template("setting.html")

@auth.route('/reports')
def reports():
    return render_template("report.html")