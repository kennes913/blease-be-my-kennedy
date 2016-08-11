from flask import Flask, render_template, Blueprint

views = Blueprint('general', __name__)

@views.route('/')
def index():
  print 'hello!'
  return render_template('index.html')

@views.route('/registry')
def wedding_registry():
  raise NotImplementedError

@views.route('/RSVP')
def rsvp():
  raise NotImplementedError

@views.route('/photos')
def photos():
  raise NotImplementedError

@views.route('/espressos')
def espresso_machine():
  raise NotImplementedError

