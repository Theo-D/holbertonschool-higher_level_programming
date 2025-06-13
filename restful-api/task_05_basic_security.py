#!/usr/bin/python3
"""
task_05_basic_security.py
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "It-is-indeed-super-secret!"  # Change this!
jwt = JWTManager(app)
auth = HTTPBasicAuth()
users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    else:
        return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Access with:
# curl -X POST http://localhost:5000/login
# -H "Content-Type: application/json"
# -d '{"username": "username", "password": "password"}'
@app.route("/login", methods=["GET", "POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username,
                                           additional_claims={"role":
                                           user["role"]})
        return jsonify(access_token)
    else:
        return ({"msg": "Bad username or password"}), 401


# Access with: curl -H "Authorization: Bearer access_token"
# http://127.0.0.1:5000/jwt-protected
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@jwt.user_identity_loader
def user_id_tostr(user):
    return str(user)


# Access with: curl -H "Authorization: Bearer access_token"
# http://127.0.0.1:5000/jwt-protected
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin():
    current_user = get_jwt()
    if current_user.get('role') != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


""" @jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401 """


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
