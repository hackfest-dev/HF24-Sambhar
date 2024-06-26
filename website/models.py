from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Category(db.Model):
    category_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    category_name=db.Column(db.String(20),unique=True)

class Companies(db.Model):
    company_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    company_name=db.Column(db.String(50))
    company_address_line1=db.Column(db.String(50))
    company_address_line2=db.Column(db.String(50))
    company_pin=db.Column(db.Integer)
    company_city=db.Column(db.String(50))
    company_state=db.Column(db.String(50))
    company_country=db.Column(db.String(50))
    
    
class Units(db.Model):
    unit_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    unit_name=db.Column(db.String(5),unique=True)

class Store(db.Model):
    store_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    store_name=db.Column(db.String(50))
    
class Inventory(db.Model):
    item_id=db.Column(db.String(10),primary_key=True)
    item_category=db.Column(db.Integer,db.ForeignKey('category.category_id'))
    item_name=db.Column(db.String(20))
    current_stock=db.Column(db.Integer)
    units=db.Column(db.Integer,db.ForeignKey('units.unit_id'))
    default_price=db.Column(db.Integer)
    regular_selling_price=db.Column(db.Integer)
    regular_buying_price=db.Column(db.Integer)
    mrp=db.Column(db.Integer)
    dealer_price=db.Column(db.Integer)
    distributor_price=db.Column(db.Integer)
    tax=db.Column(db.Float)
    item_type=db.Column(db.String(50))
    hsn_code=db.Column(db.String(50),unique=True)
    min_stock_level=db.Column(db.Integer)
    max_stock_level=db.Column(db.Integer)
    
class Stock_movement(db.Model):
    sales_id=db.Column(db.Integer,primary_key=True)
    from_store=db.Column(db.Integer,db.ForeignKey('store.store_id'))
    to_store=db.Column(db.Integer,db.ForeignKey('store.store_id'))
    mov_type=db.Column(db.String(20))
    mov_date=db.Column(db.Date)
    
    
class Transaction(db.Model):   
    tran_id = db.Column(db.Integer,primary_key=True,autoincrement=True) 
    sales_id=db.Column(db.Integer,db.ForeignKey('stock_movement.sales_id'))
    item_id=db.Column(db.String(10),db.ForeignKey('inventory.item_id'))
    price_per_unit=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    
class Produces(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    finished_prod_id=db.Column(db.String(10),db.ForeignKey('inventory.item_id'))
    raw_material_id=db.Column(db.String(10),db.ForeignKey('inventory.item_id'))
    quantity=db.Column(db.Integer)

class Sales_purchases(db.Column):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    sales_id=db.Column(db.Integer,db.ForeignKey('stock_movement.sales_id'))
    company=db.Column(db.Integer,db.ForeignKey('companies.company_id'))

