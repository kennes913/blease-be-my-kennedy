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
		
from bbmk.views import views
app.register_blueprint(views)

app.run()
