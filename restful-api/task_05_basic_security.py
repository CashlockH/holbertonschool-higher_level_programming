"""Authenticated Flask website"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secretkimisecret"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    return "Access Denied", 401

@app.route('/basic-protected', methods = ['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]['role']})
        return jsonify(access_token=access_token)
    return jsonify("Wrong username or password"), 401

@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return current_user
    return jsonify({"error": "Only admin"}), 403



if __name__ == '__main__':
    app.run()
