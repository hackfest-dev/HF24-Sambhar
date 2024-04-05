from flask import Blueprint, render_template

myViews = Blueprint('myViews',__name__)

@myViews.route('/')
def home():
    return render_template("login.html")