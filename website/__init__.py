from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import myViews
    from .auth import auth

    app.register_blueprint(myViews, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app