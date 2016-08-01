from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/registry')
def wedding_registry():
  raise NotImplementedError

@app.route('/rsvp')
def repondez_sil_vous_plait():
  raise NotImplementedError

@app.route('/photos')
def photos():
  raise NotImplementedError

@app.route('/espresso')
def espresso_machine():
  raise NotImplementedError

if __name__ == '__main__':
  app.run(debug=True)

