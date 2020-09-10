#imports
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template, flash
from flask_sqlalchemy  import SQLAlchemy
from uuid import uuid4
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import click
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from .config import Config
from flask_bootstrap import Bootstrap
from .flask_celery import make_celery


#app initialization
app = Flask(__name__)

#config app
app.config.from_object(Config)


#setting up db, migrations and authentication
db = SQLAlchemy(app)

#import models here because of the circular dependency
from .models import *


migrate = Migrate(app,db)

#celery
celery = make_celery(app)

#context processor for dates
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

#close connections to avoid queue pool overflow
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()



# blueprint imports --- always below db creation
from app.site.routes import site

# register blueprints
app.register_blueprint(site)
