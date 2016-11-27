"""
TODO: add docstring
"""

import utils

import flask_peewee.db

from datetime import datetime
from flask import Flask, session, g, render_template
from flask_basicauth import BasicAuth

app_config = utils.load_config('develop')

app = Flask(__name__)
app.config.from_object(app_config)
utils.build_database(app_config)

@app.teardown_request
def close_db(exception):
	if not db.database.is_closed():
		db.close_db()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

basic_auth = BasicAuth(app)

db = flask_peewee.db.Database(app)

from bbmk.views import views
app.register_blueprint(views)



