from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
# import flask migrate here
<<<<<<< HEAD
=======
from flask_migrate import Migrate
>>>>>>> 79519a6 (updated files)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
<<<<<<< HEAD
=======
migrate = Migrate(app, db)
>>>>>>> 79519a6 (updated files)
