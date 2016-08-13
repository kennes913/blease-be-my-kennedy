from flask import Flask, render_template, Blueprint

views = Blueprint('general', __name__)

@views.route('/')
def index():
  return render_template('index.html')

@views.route('/registry')
def wedding_registry():
  raise NotImplementedError

@views.route('/rsvp')
def rsvp():
  raise NotImplementedError

@views.route('/photos')
def photos():
  raise NotImplementedError

@views.route('/espresso')
def espresso_machine():
  raise NotImplementedError

