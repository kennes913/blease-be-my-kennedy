"""
Initialize App for bleasebemykennedy.com

"""
import utils 

from datetime import datetime
from flask import Flask, session, g, render_template

from flask_peewee.db import Database

app_config = utils.load_config()
app = Flask(__name__)
app.config.from_object(app_config)

# start and build database
if app_config.DEBUG:
	utils.build_database(app_config)

db = Database(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# user authentication and admin views and models
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin

# create admin user if it does not exist
auth = Auth(app, db)
if app_config.DEBUG:
	utils.create_admin_user(auth, 'admin', app_config.SECRET_KEY, app_config.email)

# initialize admin portion of site
admin = Admin(app, auth)
admin.setup()

# initialize general views and models 
from bbmk.views import views

app.register_blueprint(views)



