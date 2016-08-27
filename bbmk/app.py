"""
Initialize App for bleasebemykennedy.com

"""
import utils

from datetime import datetime
from flask import Flask, session, g, render_template

app_config = utils.load_config()
app = Flask(__name__)
app.config.from_object(app_config)

# start and build database
if app_config.DEBUG:
	utils.build_database(app_config)

@app.teardown_request
def close_db(exception):
	if not db.database.is_closed():
		db.close_db()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# flask peewee ORM dependencies
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin

db = Database(app)
auth = Auth(app, db)

if app_config.DEBUG:
	utils.create_admin_user(auth, 'admin', app_config.SECRET_KEY, app_config.email)

# initialize admin portion of site
admin = Admin(app, auth)
admin.setup()

# initialize general views and models 
from bbmk.views import views

app.register_blueprint(views)



