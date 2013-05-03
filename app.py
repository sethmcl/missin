from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', name='bryan');

@app.route('/goodbye')
def goodbye():
    return 'goodbye'

if __name__ == '__main__':
    app.debug = True
    app.run()
