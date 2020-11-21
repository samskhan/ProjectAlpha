from flask import Flask

#Adding flask app instance.

alpha = Flask(__name__)

#Using app instance to create base route, should return simple message
@alpha.route("/")
def index():
    return "Welcome to Project Alpha"

#Second route for shits and giggles
@alpha.route("/second-route")
def second():
    return("This is the second route")

#Use this to check out using the parameter "username"
@alpha.route("/second-route/<username>")
def name(username):
    return f"Yo waddup {username}."
