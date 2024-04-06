from flask import Blueprint, render_template
from flask_login import login_required,current_user

myViews = Blueprint('myViews',__name__)

@myViews.route('/')
def landing():
    return render_template("landing.html")

@myViews.route('/home')
@login_required
def home():
    return render_template("home.html",user=current_user)