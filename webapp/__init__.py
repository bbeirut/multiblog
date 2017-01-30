from config import DevConfig
from flask import Flask

from models import db
from controllers.blog import blog_blueprint
from controllers.main import main_blueprint
from webapp.extensions import bcrypt, oid

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    oid.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)
    
    return app