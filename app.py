from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html');

@app.route('/login')
def login():
  return render_template();

@app.route('/map', methods=['POST'])
def map():
  return render_template('map.html');

if __name__ == '__main__':
    app.debug = True
    app.run()
