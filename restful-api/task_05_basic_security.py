"""Authenticated Flask website"""
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
      "user1": {
          "username": "user1",
          "password": generate_password_hash("belede"),
          "role": "user"
          },
      "admin1": {
          "username": "admin1",
          "password": generate_password_hash("adminemde"),
          "role": "admin"}
  }

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def index():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run(debug=True)
