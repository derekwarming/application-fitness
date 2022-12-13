from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<string:name>") #probably don't need this
def user(name):
    return render_template("user.html", name=name)

@app.route("/user/test/<id>") #probably don't need this
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return "Hello"
