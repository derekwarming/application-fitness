from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask import session
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FieldList, FormField, RadioField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Nx_r9Uq/X)mZV,k;+6|WJQq5h^3<["'

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

@app.route("/sign_up1-2", methods=['GET', 'POST'])
def signup1():
    #username = None
    #email = None
    #password = None
    form = CreateAccountForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        #form.username.data = ''
        #form.email.data = ''
        #form.password.data = ''
        return redirect(url_for('signup2'))
    return render_template("sign_up1-2.html", form=form, username=session.get('username'), email=session.get('email'), password=session.get('password'))

@app.route("/sign_up2-2", methods=['GET', 'POST'])
def signup2():
    form2 = UserProfile1()
    if form2.validate_on_submit():
        session['gender'] = form2.gender.data
        return redirect(url_for('signup2'))
    return render_template("sign_up2-2.html", form2=form2, gender=session.get('gender'))

@app.errorhandler(404) #404 error page
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) #500 error page
def internal_server_error(e):
    return render_template('500.html'), 500

class CreateAccountForm(FlaskForm):
    username = StringField(render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    email = StringField(render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    password = PasswordField(render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField('NEXT')

class UserProfile1(FlaskForm):
    gender = RadioField('gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('NEXT')
