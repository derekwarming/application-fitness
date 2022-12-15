from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<string:name>") #probably don't need this
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404) #404 error page
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) #500 error page
def internal_server_error(e):
    return render_template('500.html'), 500
