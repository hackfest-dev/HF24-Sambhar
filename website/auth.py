from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, jsonify
from .models import User,Inventory,Category,Units
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
#db_uri = 'mysql+mysqlconnector://username:password@localhost/database_name'

# Create SQLAlchemy engine
#engine = create_engine(db_uri)

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
        join(Category, Inventory.item_category == Category.category_id).\
        join(Units, Inventory.units == Units.unit_id).all()
    return render_template("inventory.html", inventory_items=inventory_items)

@auth.route('/addtoinventory',methods=['GET','POST'])
def addtoinventory():
    if request.method=='POST':
        id = request.form.get('item_id')
        category = request.form.get('item_category')
        name = request.form.get('item-name')
        curr_stock = request.form.get('current-stock')
        units = request.form.get('units')
        d_price = request.form.get('default-price')
        r_s_price = request.form.get('r-selling-price')
        r_b_price = request.form.get('r-buying-price')
        mrp = request.form.get('mrp')
        dealer_price = request.form.get('dealer-price')
        dis_price = request.form.get('dis-price')
        tax = request.form.get('tax')
        item_type = request.form.get('item-type')
        hsn_code = request.form.get('hsn-code')
        min_stock = request.form.get('min-stock')
        max_stock = request.form.get('max-stock')

        item = Inventory.query.filter_by(item_id=id).first()

        if item:
            flash("Item already exists in the Inventory.",category='error')
        else:
            it = Category.query.filter_by(category_name=category).first()
            print(it)
            cat_id = it.category_id
            bt = Units.query.filter_by(unit_name=units).first()
            uni_id = bt.unit_id
            new_item = Inventory(item_id=id,item_category=cat_id,item_name=name,current_stock=curr_stock,units=uni_id,default_price=d_price,regular_selling_price=r_s_price,regular_buying_price=r_b_price,mrp=mrp,dealer_price=dealer_price,distributor_price=dis_price,tax=tax,item_type=item_type,hsn_code=hsn_code,min_stock_level=min_stock,max_stock_level=max_stock)
            db.session.add(new_item)
            db.session.commit()

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
