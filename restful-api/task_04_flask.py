from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


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
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['GET', 'POST'])
def parser():
    try:
        usera = request.json
        if not usera:
            return jsonify({"error": "No JSON data provided"}), 400
        if 'username' not in usera:
            return jsonify({"error": "Username is required"}), 400
        users[usera['username']] = usera
        new = {
                "message": "User added",
                "user": {
                    "username": usera['username'],
                    "name": usera['name'],
                    "age": usera['age'],
                    "city": usera['city']
                    }
                }
        return jsonify(new), 201
    except Exception as err:
        return jsonify({"error": str(err)}), 404


if __name__ == "__main__":
    app.run()
