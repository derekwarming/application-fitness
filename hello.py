from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

#shortcut icon located in bootstrap/base.html

@app.route("/")
def index():
    return render_template("index.html",
    current_time=datetime.utcnow())

@app.route("/user/<string:name>")
def user(name):
    return render_template("user.html", name=name,
    current_time=datetime.utcnow())

@app.route("/datetime-now")
def datetimenow():
    return render_template("datetime-now.html",
    current_time=datetime.utcnow())

@app.errorhandler(404) #404 error page
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) #500 error page
def internal_server_error(e):
    return render_template('500.html'), 500
