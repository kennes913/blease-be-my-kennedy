"""
Main App for bleasemekennedy.com
"""
import utils

import flask_peewee.db

from datetime import datetime
from flask import Flask, session, g, render_template
from flask_basicauth  import BasicAuth

app_config = utils.load_config()
app = Flask(__name__)
app.config.from_object(app_config)

# start and build database
utils.build_database(app_config)

@app.teardown_request
def close_db(exception):
	if not db.database.is_closed():
		db.close_db()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# Basic Auth for protected pages
basic_auth = BasicAuth(app)

# Flask Peewee ORM dependency
# http://docs.peewee-orm.com/projects/flask-peewee/en/latest/database.html
db = flask_peewee.db.Database(app)

# initialize general views and models 
from bbmk.views import views

app.register_blueprint(views)



