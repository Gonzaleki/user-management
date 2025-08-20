from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return "This would return the method that creates the user"

@auth.route("/login")
def signin():
    return "This would return the method that logs the user in"

@auth.route("/logout")
def signin():
    return "This would return the method that logs the user out"