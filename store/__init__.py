from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_login import LoginManager
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_store.db'
app.config['SECRET_KEY'] = 'dhgjshavfjakskah'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate()
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'loginClient'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = 'Favor, fazer o login primeiro!'

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

from store.shopping_cart import carts
from store.products import routes
from store.admin import routes
from store.clients import routes