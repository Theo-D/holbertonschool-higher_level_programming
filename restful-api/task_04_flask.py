#!/usr/bin/python3
"""
task_04_flask.py -
"""
from flask import Flask, jsonify, request


userDict = {}
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def serializeUsernames(userDict):
    return jsonify({'username': userDict})


@app.route("/status")
def status():
    return "Ok"


@app.route("/users/<str:username>")
def getUsers(username):
    for user in userDict:
        if user == username:
            return jsonify(userDict[user])
        else:
            return jsonify({"error": "User not found"}), 404


@app.route("/add_user", method="POST")
def addUSer():
    newUser = request.get_json()
    if "username" not in newUser:
        return jsonify({"error": "Username is required"}), 400
    else:
        userDict[newUser["username"]]
        return jsonify({"message": "User added", "user": newUser})


if __name__ == "__main__":
    app.run()
