<<<<<<< HEAD
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, jsonify
from .models import User
=======
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Inventory,Category,Units
>>>>>>> 469719455a558c44f57dbbf13ab1f8d268512af8
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import sqlite3
import subprocess
import tempfile
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
    inventory_items = db.session.query(Inventory, Category, Units).\
        join(Category, Inventory.category_id == Category.id).\
        join(Units, Inventory.units_id == Units.id).all()
    return render_template("inventory.html", inventory_items=inventory_items)

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
@auth.route('/run_current')
def run_current():
    subprocess.run(['python3', 'models/current_stock.py'])
    return send_file('../pie_chart.png', mimetype='image/png')
@auth.route('/budget_allocate')
def budget_allocate():
    try:
        # Execute xg_boost.py and capture its output to a temporary file
        with tempfile.TemporaryFile() as temp_output_file:
            subprocess.run(['python3', 'models/xg_boost.py'], stdout=temp_output_file)
            temp_output_file.seek(0)  # Move file pointer to the beginning
            output = temp_output_file.read().decode('utf-8')  # Read output from temporary file

        # Return the output as JSON
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)})
@auth.route('/product_status')
def product_status():
    subprocess.run(['python3', 'models/product_stock.py'])
    return send_file('../pie1_chart.png', mimetype='image/png')
@auth.route('/fore_cast')
def fore_cast():
    subprocess.run(['python3', 'models/forecast.py'])
    return send_file('../pie2_chart.png', mimetype='image/png')