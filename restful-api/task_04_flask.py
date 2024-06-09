"""Simple Flask request handler"""
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def data():
    return jsonify([keys for keys in users.keys()])


@app.route("/status")
def status():
    return "OK"


@app.route('/users/<username>')
def user(username):
    for key in users.keys():
        if key == username:
            return jsonify(users[key])
    return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['GET', 'POST'])
def parser():
    if request.method == "POST":
        user = request.form.get('user')
        users[user['username']] = user


if __name__ == "__main__":
    app.run()
