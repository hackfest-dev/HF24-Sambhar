from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, jsonify
from .models import User, Inventory, Category, Units
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import subprocess
import tempfile
from sqlalchemy import create_engine

auth = Blueprint('auth', __name__)

# Update SQLAlchemy database URI to connect to MySQL
# Replace 'username', 'password', 'database_name' with actual values
db_uri = 'mysql+mysqlconnector://username:password@localhost/database_name'

# Create SQLAlchemy engine
engine = create_engine(db_uri)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('myViews.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)

# Other routes remain the same

@auth.route('/run_current')
def run_current():
    subprocess.run(['python3', 'models/current_stock.py'])
    return send_file('../pie_chart.png', mimetype='image/png')

@auth.route('/budget_allocate')
def budget_allocate():
    try:
        with tempfile.TemporaryFile() as temp_output_file:
            subprocess.run(['python3', 'models/xg_boost.py'], stdout=temp_output_file)
            temp_output_file.seek(0)
            output = temp_output_file.read().decode('utf-8')

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
