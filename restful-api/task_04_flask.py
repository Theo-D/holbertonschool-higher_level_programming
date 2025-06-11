#!/usr/bin/python3
"""
task_04_flask.py -
"""
from flask import Flask, jsonify, request



app = Flask(__name__)
userDict = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def serializeUsernames():
    usernames = list(userDict.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def getUsers(username):
    for user in userDict.keys():
        if user == username:
            return jsonify(userDict[user])
        else:
            return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def addUSer():
    newUser = request.get_json()
    if 'username' not in newUser or not newUser:
        return jsonify({"error": "Username is required"}), 400
    userDict[newUser["username"]] = newUser
    return jsonify({"message": "User added", "user": newUser}), 201


if __name__ == "__main__":
    app.run()
