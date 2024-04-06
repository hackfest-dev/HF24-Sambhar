from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
DB_NAME = "inventory.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dskjhfkdjh dskjhkhsdf"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import myViews
    from .auth import auth

    app.register_blueprint(myViews, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists(path.join(path.dirname(__file__), '..', 'instance', 'inventory.db')):
        with app.app_context():
            db.create_all()
            print('Created database')
            from .models import User
            admin = User(email="admin@gmail.com",password = generate_password_hash("admin",method='pbkdf2:sha1', salt_length=8))
            db.session.add(admin)
            db.session.commit()
            print("Admin created successfully")
