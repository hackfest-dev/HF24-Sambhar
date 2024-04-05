from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("./login.html")

@auth.route('/logout')
def logout():
    return "<h1>Hi</h1>"

@auth.route('/signup',methods=['POST','GET'])
def sign_up():
    return render_template("signup.html")