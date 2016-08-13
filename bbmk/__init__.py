"""
"""

import config

from datetime import datetime
from flask import Flask, session, g, render_template

app = Flask(__name__)

try:
	if config.develop:
		app.config.from_object(config.develop)
	else:
		app.config.from_object(config.production)
except ImportError:
	 app.config.from_object(config.default)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
		
from bbmk.views import views

app.register_blueprint(views)
