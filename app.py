from flask import Flask, render_template, jsonify
from model import db, app, User
from sqlalchemy import func

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/login')
def login():
  return render_template()


@app.route('/map', methods=["POST","GET"])
def map():
  return render_template('map.html')


@app.route('/users')
def users():
  users = User.query.all()
  results = []

  for user in users:
    results.append(user.email)

  print results
  return jsonify({"results": results})


@app.route('/request')
def request():
  return render_template('request.html');

if __name__ == '__main__':
    app.debug = True
    app.run()
