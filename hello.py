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
from wtforms import StringField, SubmitField, PasswordField, FieldList, FormField, RadioField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired

import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import column_property
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Nx_r9Uq/X)mZV,k;+6|WJQq5h^3<["'

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



#shortcut icon located in bootstrap/base.html


#Routes
#
#
#
#
#

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
        session['birthday'] = form2.birthday.data
        session['units'] = form2.units.data
        return redirect(url_for('signup3'))
    return render_template("sign_up2-2.html", form2=form2, gender=session.get('gender'), birthday=session.get('birthday'), units=session.get('units'))

@app.route("/sign_up3-1", methods=['GET', 'POST'])
def signup3():
    form3 = UserProfile2()
    if form3.validate_on_submit():
        session['height_inches'] = form3.height_inches.data
        session['weight_lbs'] = form3.weight_lbs.data
        session['goal_weight_lbs'] = form3.goal_weight_lbs.data
        return redirect(url_for('signup4'))
    return render_template("sign_up3-1.html", form3=form3, height_inches=session.get('height_inches'), weight_lbs=session.get('weight_lbs'), goal_weight_lbs=session.get('goal_weight_lbs'))

@app.route("/sign_up4-3", methods=['GET', 'POST'])
def signup4():
    form4 = UserProfile3()
    if form4.validate_on_submit():
        session['plan_daily_eat'] = form4.plan_daily_eat.data
        session['plan_daily_burn'] = form4.plan_daily_burn.data
        session['body_type'] = form4.body_type.data
        return redirect(url_for('signup5'))
    return render_template("sign_up4-3.html", form4=form4, plan_daily_eat=session.get('plan_daily_eat'), plan_daily_burn=session.get('plan_daily_burn'), body_type=session.get('body_type'))

@app.route("/sign_up5-1")
def signup5():
    return render_template("sign_up5-1.html")

#Error Pages
#
#
#
#
#

@app.errorhandler(404) #404 error page
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) #500 error page
def internal_server_error(e):
    return render_template('500.html'), 500

# Forms
#
#
#
#
#

class CreateAccountForm(FlaskForm):
    username = StringField(render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    email = StringField(render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    password = PasswordField(render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField('NEXT')

class UserProfile1(FlaskForm):
    gender = RadioField('gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    birthday = DateField('birthday', format='%Y-%m-%d', validators=[DataRequired()])
    units = RadioField('units', choices=[('Imperial', 'Imperial'), ('Metric', 'Metric')], validators=[DataRequired()])
    submit = SubmitField('NEXT')

class UserProfile2(FlaskForm):
    # height = inches
    height_inches = SelectField('height_inches', choices=[
    ('36', '3 ft. 0 inch. / 91.44 cm'), ('37', '3 ft. 1 inch. / 93.98 cm'), ('38', '3 ft. 2 inch. / 96.52 cm'), ('39', '3 ft. 3 inch. / 99.06 cm'), ('40', '3 ft. 4 inch. / 101.6 cm'), ('41', '3 ft. 5 inch. / 104.14 cm'),
    ('42', '3 ft. 6 inch. / 106.68 cm'), ('43', '3 ft. 7 inch. / 109.22 cm'), ('44', '3 ft. 8 inch. / 111.76 cm'), ('45', '3 ft. 9 inch. / 114.3 cm'), ('46', '3 ft. 10 inch. / 116.84 cm'), ('47', '3 ft. 11 inch. / 119.38 cm'),
    ('48', '4 ft. 0 inch. / 121.92 cm'), ('49', '4 ft. 1 inch. / 124.46 cm'), ('50', '4 ft. 2 inch. / 127 cm'), ('51', '4 ft. 3 inch. / 129.54 cm'), ('52', '4 ft. 4 inch. / 132.08 cm'), ('53', '4 ft. 5 inch. / 134.62 cm'),
    ('54', '4 ft. 6 inch. / 137.16 cm'), ('55', '4 ft. 7 inch. / 139.7 cm'), ('56', '4 ft. 8 inch. / 142.24 cm'), ('57', '4 ft. 9 inch. / 144.78 cm'), ('58', '4 ft. 10 inch. / 147.32 cm'), ('59', '4 ft. 11 inch. / 149.86 cm'),
    ('60', '5 ft. 0 inch. / 152.4 cm'), ('61', '5 ft. 1 inch. / 154.94 cm'), ('62', '5 ft. 2 inch. / 157.48 cm'), ('63', '5 ft. 3 inch. / 160.02 cm'), ('64', '5 ft. 4 inch. / 162.56 cm'), ('65', '5 ft. 5 inch. / 165.1 cm'),
    ('66', '5 ft. 6 inch. / 167.64 cm'), ('67', '5 ft. 7 inch. / 170.18 cm'), ('68', '5 ft. 8 inch. / 172.72 cm'), ('69', '5 ft. 9 inch. / 175.26 cm'), ('70', '5 ft. 10 inch. / 177.8 cm'), ('71', '5 ft. 11 inch. / 180.34 cm'),
    ('72', '6 ft. 0 inch. / 182.88 cm'), ('73', '6 ft. 1 inch. / 185.42 cm'), ('74', '6 ft. 2 inch. / 187.96 cm'), ('75', '6 ft. 3 inch. / 190.5 cm'), ('76', '6 ft. 4 inch. / 193.04 cm'), ('77', '6 ft. 5 inch. / 195.58 cm'),
    ('78', '6 ft. 6 inch. / 198.12 cm'), ('79', '6 ft. 7 inch. / 200.66 cm'), ('80', '6 ft. 8 inch. / 203.2 cm'), ('81', '6 ft. 9 inch. / 205.74 cm'), ('82', '6 ft. 10 inch. / 208.28 cm'), ('83', '6 ft. 11 inch. / 210.82 cm'),
    ('84', '7 ft. 0 inch. / 213.36 cm'), ('85', '7 ft. 1 inch. / 215.9 cm'), ('86', '7 ft. 2 inch. / 218.44 cm'), ('87', '7 ft. 3 inch. / 220.98 cm'), ('88', '7 ft. 4 inch. / 223.52 cm'), ('89', '7 ft. 5 inch. / 226.06 cm'),
    ('90', '7 ft. 6 inch. / 228.6 cm')
    ])
    # current weight = lbs
    weight_lbs = SelectField('weight_lbs', choices=[
    ('30', '30 lbs. / 13.61 kg'), ('31', '31 lbs. / 14.06 kg'), ('32', '32 lbs. / 14.51 kg'), ('33', '33 lbs. / 14.97 kg'), ('34', '34 lbs. / 15.42 kg'), ('35', '35 lbs. / 15.88 kg'), ('36', '36 lbs. / 16.33 kg'), ('37', '37 lbs. / 16.78 kg'), ('38', '38 lbs. / 17.24 kg'), ('39', '39 lbs. / 17.69 kg'),
    ('40', '40 lbs. / 18.14 kg'), ('41', '41 lbs. / 18.60 kg'), ('42', '42 lbs. / 19.05 kg'), ('43', '43 lbs. / 19.50 kg'), ('44', '44 lbs. / 19.96 kg'), ('45', '45 lbs. / 20.41 kg'), ('46', '46 lbs. / 20.87 kg'), ('47', '47 lbs. / 21.32 kg'), ('48', '48 lbs. / 21.77 kg'), ('49', '49 lbs. / 22.23 kg'),
    ('50', '50 lbs. / 22.68 kg'), ('51', '51 lbs. / 23.13 kg'), ('52', '52 lbs. / 23.59 kg'), ('53', '53 lbs. / 24.04 kg'), ('54', '54 lbs. / 24.49 kg'), ('55', '55 lbs. / 24.95 kg'), ('56', '56 lbs. / 25.40 kg'), ('57', '57 lbs. / 25.85 kg'), ('58', '58 lbs. / 26.31 kg'), ('59', '59 lbs. / 26.76 kg'),
    ('60', '60 lbs. / 27.22 kg'), ('61', '61 lbs. / 27.67 kg'), ('62', '62 lbs. / 28.12 kg'), ('63', '63 lbs. / 28.58 kg'), ('64', '64 lbs. / 29.03 kg'), ('65', '65 lbs. / 29.48 kg'), ('66', '66 lbs. / 29.94 kg'), ('67', '67 lbs. / 30.39 kg'), ('68', '68 lbs. / 30.84 kg'), ('69', '69 lbs. / 31.30 kg'),
    ('70', '70 lbs. / 31.75 kg'), ('71', '71 lbs. / 32.21 kg'), ('72', '72 lbs. / 32.66 kg'), ('73', '73 lbs. / 33.11 kg'), ('74', '74 lbs. / 33.57 kg'), ('75', '75 lbs. / 34.02 kg'), ('76', '76 lbs. / 34.47 kg'), ('77', '77 lbs. / 34.93 kg'), ('78', '78 lbs. / 35.38 kg'), ('79', '79 lbs. / 35.83 kg'),
    ('80', '80 lbs. / 36.29 kg'), ('81', '81 lbs. / 36.74 kg'), ('82', '82 lbs. / 37.19 kg'), ('83', '83 lbs. / 37.65 kg'), ('84', '84 lbs. / 38.10 kg'), ('85', '85 lbs. / 38.56 kg'), ('86', '86 lbs. / 39.01 kg'), ('87', '87 lbs. / 39.46 kg'), ('88', '88 lbs. / 39.92 kg'), ('89', '89 lbs. / 40.37 kg'),
    ('90', '90 lbs. / 40.82 kg'), ('91', '91 lbs. / 41.28 kg'), ('92', '92 lbs. / 41.73 kg'), ('93', '93 lbs. / 42.18 kg'), ('94', '94 lbs. / 42.64 kg'), ('95', '95 lbs. / 43.09 kg'), ('96', '96 lbs. / 43.54 kg'), ('97', '97 lbs. / 44.00 kg'), ('98', '98 lbs. / 44.45 kg'), ('99', '99 lbs. / 44.91 kg'),
    ('100', '100 lbs. / 45.36 kg'), ('101', '101 lbs. / 45.81 kg'), ('102', '102 lbs. / 46.27 kg'), ('103', '103 lbs. / 46.72 kg'), ('104', '104 lbs. / 47.17 kg'), ('105', '105 lbs. / 47.63 kg'), ('106', '106 lbs. / 48.08 kg'), ('107', '107 lbs. / 48.53 kg'), ('108', '108 lbs. / 48.99 lg'), ('109', '109 lbs. / 49.44 kg'),
    ('110', '110 lbs. / 49.90 kg'), ('111', '111 lbs. / 50.35 kg'), ('112', '112 lbs. / 50.80 kg'), ('113', '113 lbs. / 51.26 kg'), ('114', '114 lbs. / 51.71 kg'), ('115', '115 lbs. / 52.16 kg'), ('116', '116 lbs. / 52.62 kg'), ('117', '117 lbs. / 53.07 kg'), ('118', '118 lbs. / 53.52 kg'), ('119', '119 lbs. / 53.98 kg'),
    ('120', '120 lbs. / 54.43 kg'), ('121', '121 lbs. / 54.88 kg'), ('122', '122 lbs. / 55.34 kg'), ('123', '123 lbs. / 55.79 kg'), ('124', '124 lbs. / 56.25 kg'), ('125', '125 lbs. / 56.70 kg'), ('126', '126 lbs. / 57.15 kg'), ('127', '127 lbs. / 57.61 kg'), ('128', '128 lbs. / 58.06 kg'), ('129', '129 lbs. / 58.51 kg'),
    ('130', '130 lbs. / 58.97 kg'), ('131', '131 lbs. / 59.42 kg'), ('132', '132 lbs. / 59.87 kg'), ('133', '133 lbs. / 60.33 kg'), ('134', '134 lbs. / 60.78 kg'), ('135', '135 lbs. / 61.23 kg'), ('136', '136 lbs. / 61.69 kg'), ('137', '137 lbs. / 62.14 kg'), ('138', '138 lbs. / 62.60 kg'), ('139', '139 lbs. / 63.05 kg'),
    ('140', '140 lbs. / 63.50 kg'), ('141', '141 lbs. / 63.96 kg'), ('142', '142 lbs. / 64.41 kg'), ('143', '143 lbs. / 64.86 kg'), ('144', '144 lbs. / 65.32 kg'), ('145', '145 lbs. / 65.77 kg'), ('146', '146 lbs. / 66.22 kg'), ('147', '147 lbs. / 66.68 kg'), ('148', '148 lbs. / 67.13 kg'), ('149', '149 lbs. / 67.59 kg'),
    ('150', '150 lbs. / 68.04 kg'), ('151', '151 lbs. / 68.49 kg'), ('152', '152 lbs. / 68.95 kg'), ('153', '153 lbs. / 69.40 kg'), ('154', '154 lbs. / 69.85 kg'), ('155', '155 lbs. / 70.31 kg'), ('156', '156 lbs. / 70.76 kg'), ('157', '157 lbs. / 71.21 kg'), ('158', '158 lbs. / 71.67 kg'), ('159', '159 lbs. / 72.12 kg'),
    ('160', '160 lbs. / 72.57 kg'), ('161', '161 lbs. / 73.03 kg'), ('162', '162 lbs. / 73.48 kg'), ('163', '163 lbs. / 73.94 kg'), ('164', '164 lbs. / 74.39 kg'), ('165', '165 lbs. / 74.84 kg'), ('166', '166 lbs. / 75.30 kg'), ('167', '167 lbs. / 75.75 kg'), ('168', '168 lbs. / 76.20 kg'), ('169', '169 lbs. / 76.66 kg'),
    ('170', '170 lbs. / 77.11 kg'), ('171', '171 lbs. / 77.56 kg'), ('172', '172 lbs. / 78.02 kg'), ('173', '173 lbs. / 78.47 kg'), ('174', '174 lbs. / 78.93 kg'), ('175', '175 lbs. / 79.38 kg'), ('176', '176 lbs. / 79.83 kg'), ('177', '177 lbs. / 80.29 kg'), ('178', '178 lbs. / 80.74 kg'), ('179', '179 lbs. / 81.19 kg'),
    ('180', '180 lbs. / 81.65 kg'), ('181', '181 lbs. / 82.10 kg'), ('182', '182 lbs. / 82.55 kg'), ('183', '183 lbs. / 83.01 kg'), ('184', '184 lbs. / 83.46 kg'), ('185', '185 lbs. / 83.91 kg'), ('186', '186 lbs. / 84.37 kg'), ('187', '187 lbs. / 84.82 kg'), ('188', '188 lbs. / 85.28 kg'), ('189', '189 lbs. / 85.73 kg'),
    ('190', '190 lbs. / 86.18 kg'), ('191', '191 lbs. / 86.64 kg'), ('192', '192 lbs. / 87.09 kg'), ('193', '193 lbs. / 87.54 kg'), ('194', '194 lbs. / 88.00 kg'), ('195', '195 lbs. / 88.45 kg'), ('196', '196 lbs. / 88.90 kg'), ('197', '197 lbs. / 89.36 kg'), ('198', '198 lbs. / 89.81 kg'), ('199', '199 lbs. / 90.26 kg'),
    ('200', '200 lbs. / 90.72 kg'), ('201', '201 lbs. / 91.17 kg'), ('202', '202 lbs. / 91.63 kg'), ('203', '203 lbs. / 92.08 kg'), ('204', '204 lbs. / 92.53 kg'), ('205', '205 lbs. / 92.99 kg'), ('206', '206 lbs. / 93.44 kg'), ('207', '207 lbs. / 93.89 kg'), ('208', '208 lbs. / 94.35 kg'), ('209', '209 lbs. / 94.80 kg'),
    ('210', '210 lbs. / 95.25 kg'), ('211', '211 lbs. / 95.71 kg'), ('212', '212 lbs. / 96.16 kg'), ('213', '213 lbs. / 96.62 kg'), ('214', '214 lbs. / 97.07 kg'), ('215', '215 lbs. / 97.52 kg'), ('216', '216 lbs. / 97.98 kg'), ('217', '217 lbs. / 98.43 kg'), ('218', '218 lbs. / 98.88 kg'), ('219', '219 lbs. / 99.34 kg'),
    ('220', '220 lbs. / 99.79 kg'), ('221', '221 lbs. / 100.24 kg'), ('222', '222 lbs. / 100.70 kg'), ('223', '223 lbs. / 101.15 kg'), ('224', '224 lbs. / 101.60 kg'), ('225', '225 lbs. / 102.06 kg'), ('226', '226 lbs. / 102.51 kg'), ('227', '227 lbs. / 102.97 kg'), ('228', '228 lbs. / 103.42 kg'), ('229', '229 lbs. / 103.87 kg'),
    ('230', '230 lbs. / 104.33 kg'), ('231', '231 lbs. / 104.78 kg'), ('232', '232 lbs. / 105.23 kg'), ('233', '233 lbs. / 105.69 kg'), ('234', '234 lbs. / 106.14 kg'), ('235', '235 lbs. / 106.59 kg'), ('236', '236 lbs. / 107.05 kg'), ('237', '237 lbs. / 107.50 kg'), ('238', '238 lbs. / 107.95 kg'), ('239', '239 lbs. / 108.41 kg'),
    ('240', '240 lbs. / 108.86 kg'), ('241', '241 lbs. / 109.32 kg'), ('242', '242 lbs. / 109.77 kg'), ('243', '243 lbs. / 110.22 kg'), ('244', '244 lbs. / 110.68 kg'), ('245', '245 lbs. / 111.13 kg'), ('246', '246 lbs. / 111.58 kg'), ('247', '247 lbs. / 112.04 kg'), ('248', '248 lbs. / 112.49 kg'), ('249', '249 lbs. / 112.94 kg'),
    ('250', '250 lbs. / 113.40 kg'), ('251', '251 lbs. / 113.85 kg'), ('252', '252 lbs. / 114.31 kg'), ('253', '253 lbs. / 114.76 kg'), ('254', '254 lbs. / 115.21 kg'), ('255', '255 lbs. / 115.67 kg'), ('256', '256 lbs. / 116.12 kg'), ('257', '257 lbs. / 116.57 kg'), ('258', '258 lbs. / 117.03 kg'), ('259', '259 lbs. / 117.48 kg'),
    ('260', '260 lbs. / 117.93 kg'), ('261', '261 lbs. / 118.39 kg'), ('262', '262 lbs. / 118.84 kg'), ('263', '263 lbs. / 119.29 kg'), ('264', '264 lbs. / 119.75 kg'), ('265', '265 lbs. / 120.20 kg'), ('266', '266 lbs. / 120.66 kg'), ('267', '267 lbs. / 121.11 kg'), ('268', '268 lbs. / 121.56 kg'), ('269', '269 lbs. / 122.02 kg'),
    ('270', '270 lbs. / 122.47 kg'), ('271', '271 lbs. / 122.92 kg'), ('272', '272 lbs. / 123.38 kg'), ('273', '273 lbs. / 123.83 kg'), ('274', '274 lbs. / 124.28 kg'), ('275', '275 lbs. / 124.74 kg'), ('276', '276 lbs. / 125.19 kg'), ('277', '277 lbs. / 125.64 kg'), ('278', '278 lbs. / 126.10 kg'), ('279', '279 lbs. / 126.55 kg'),
    ('280', '280 lbs. / 127.01 kg'), ('281', '281 lbs. / 127.46 kg'), ('282', '282 lbs. / 127.91 kg'), ('283', '283 lbs. / 128.37 kg'), ('284', '284 lbs. / 128.82 kg'), ('285', '285 lbs. / 129.27 kg'), ('286', '286 lbs. / 129.73 kg'), ('287', '287 lbs. / 130.18 kg'), ('288', '288 lbs. / 130.63 kg'), ('289', '289 lbs. / 131.09 kg'),
    ('290', '290 lbs. / 131.54 kg'), ('291', '291 lbs. / 132.00 kg'), ('292', '292 lbs. / 132.45 kg'), ('293', '293 lbs. / 132.90 kg'), ('294', '294 lbs. / 133.36 kg'), ('295', '295 lbs. / 133.81 kg'), ('296', '296 lbs. / 134.26 kg'), ('297', '297 lbs. / 134.72 kg'), ('298', '298 lbs. / 135.17 kg'), ('299', '299 lbs. / 135.62 kg'),
    ('300', '300 lbs. / 136.08 kg')
    ])
    goal_weight_lbs = SelectField('goal_weight_lbs', choices=[
    ('30', '30 lbs. / 13.61 kg'), ('31', '31 lbs. / 14.06 kg'), ('32', '32 lbs. / 14.51 kg'), ('33', '33 lbs. / 14.97 kg'), ('34', '34 lbs. / 15.42 kg'), ('35', '35 lbs. / 15.88 kg'), ('36', '36 lbs. / 16.33 kg'), ('37', '37 lbs. / 16.78 kg'), ('38', '38 lbs. / 17.24 kg'), ('39', '39 lbs. / 17.69 kg'),
    ('40', '40 lbs. / 18.14 kg'), ('41', '41 lbs. / 18.60 kg'), ('42', '42 lbs. / 19.05 kg'), ('43', '43 lbs. / 19.50 kg'), ('44', '44 lbs. / 19.96 kg'), ('45', '45 lbs. / 20.41 kg'), ('46', '46 lbs. / 20.87 kg'), ('47', '47 lbs. / 21.32 kg'), ('48', '48 lbs. / 21.77 kg'), ('49', '49 lbs. / 22.23 kg'),
    ('50', '50 lbs. / 22.68 kg'), ('51', '51 lbs. / 23.13 kg'), ('52', '52 lbs. / 23.59 kg'), ('53', '53 lbs. / 24.04 kg'), ('54', '54 lbs. / 24.49 kg'), ('55', '55 lbs. / 24.95 kg'), ('56', '56 lbs. / 25.40 kg'), ('57', '57 lbs. / 25.85 kg'), ('58', '58 lbs. / 26.31 kg'), ('59', '59 lbs. / 26.76 kg'),
    ('60', '60 lbs. / 27.22 kg'), ('61', '61 lbs. / 27.67 kg'), ('62', '62 lbs. / 28.12 kg'), ('63', '63 lbs. / 28.58 kg'), ('64', '64 lbs. / 29.03 kg'), ('65', '65 lbs. / 29.48 kg'), ('66', '66 lbs. / 29.94 kg'), ('67', '67 lbs. / 30.39 kg'), ('68', '68 lbs. / 30.84 kg'), ('69', '69 lbs. / 31.30 kg'),
    ('70', '70 lbs. / 31.75 kg'), ('71', '71 lbs. / 32.21 kg'), ('72', '72 lbs. / 32.66 kg'), ('73', '73 lbs. / 33.11 kg'), ('74', '74 lbs. / 33.57 kg'), ('75', '75 lbs. / 34.02 kg'), ('76', '76 lbs. / 34.47 kg'), ('77', '77 lbs. / 34.93 kg'), ('78', '78 lbs. / 35.38 kg'), ('79', '79 lbs. / 35.83 kg'),
    ('80', '80 lbs. / 36.29 kg'), ('81', '81 lbs. / 36.74 kg'), ('82', '82 lbs. / 37.19 kg'), ('83', '83 lbs. / 37.65 kg'), ('84', '84 lbs. / 38.10 kg'), ('85', '85 lbs. / 38.56 kg'), ('86', '86 lbs. / 39.01 kg'), ('87', '87 lbs. / 39.46 kg'), ('88', '88 lbs. / 39.92 kg'), ('89', '89 lbs. / 40.37 kg'),
    ('90', '90 lbs. / 40.82 kg'), ('91', '91 lbs. / 41.28 kg'), ('92', '92 lbs. / 41.73 kg'), ('93', '93 lbs. / 42.18 kg'), ('94', '94 lbs. / 42.64 kg'), ('95', '95 lbs. / 43.09 kg'), ('96', '96 lbs. / 43.54 kg'), ('97', '97 lbs. / 44.00 kg'), ('98', '98 lbs. / 44.45 kg'), ('99', '99 lbs. / 44.91 kg'),
    ('100', '100 lbs. / 45.36 kg'), ('101', '101 lbs. / 45.81 kg'), ('102', '102 lbs. / 46.27 kg'), ('103', '103 lbs. / 46.72 kg'), ('104', '104 lbs. / 47.17 kg'), ('105', '105 lbs. / 47.63 kg'), ('106', '106 lbs. / 48.08 kg'), ('107', '107 lbs. / 48.53 kg'), ('108', '108 lbs. / 48.99 lg'), ('109', '109 lbs. / 49.44 kg'),
    ('110', '110 lbs. / 49.90 kg'), ('111', '111 lbs. / 50.35 kg'), ('112', '112 lbs. / 50.80 kg'), ('113', '113 lbs. / 51.26 kg'), ('114', '114 lbs. / 51.71 kg'), ('115', '115 lbs. / 52.16 kg'), ('116', '116 lbs. / 52.62 kg'), ('117', '117 lbs. / 53.07 kg'), ('118', '118 lbs. / 53.52 kg'), ('119', '119 lbs. / 53.98 kg'),
    ('120', '120 lbs. / 54.43 kg'), ('121', '121 lbs. / 54.88 kg'), ('122', '122 lbs. / 55.34 kg'), ('123', '123 lbs. / 55.79 kg'), ('124', '124 lbs. / 56.25 kg'), ('125', '125 lbs. / 56.70 kg'), ('126', '126 lbs. / 57.15 kg'), ('127', '127 lbs. / 57.61 kg'), ('128', '128 lbs. / 58.06 kg'), ('129', '129 lbs. / 58.51 kg'),
    ('130', '130 lbs. / 58.97 kg'), ('131', '131 lbs. / 59.42 kg'), ('132', '132 lbs. / 59.87 kg'), ('133', '133 lbs. / 60.33 kg'), ('134', '134 lbs. / 60.78 kg'), ('135', '135 lbs. / 61.23 kg'), ('136', '136 lbs. / 61.69 kg'), ('137', '137 lbs. / 62.14 kg'), ('138', '138 lbs. / 62.60 kg'), ('139', '139 lbs. / 63.05 kg'),
    ('140', '140 lbs. / 63.50 kg'), ('141', '141 lbs. / 63.96 kg'), ('142', '142 lbs. / 64.41 kg'), ('143', '143 lbs. / 64.86 kg'), ('144', '144 lbs. / 65.32 kg'), ('145', '145 lbs. / 65.77 kg'), ('146', '146 lbs. / 66.22 kg'), ('147', '147 lbs. / 66.68 kg'), ('148', '148 lbs. / 67.13 kg'), ('149', '149 lbs. / 67.59 kg'),
    ('150', '150 lbs. / 68.04 kg'), ('151', '151 lbs. / 68.49 kg'), ('152', '152 lbs. / 68.95 kg'), ('153', '153 lbs. / 69.40 kg'), ('154', '154 lbs. / 69.85 kg'), ('155', '155 lbs. / 70.31 kg'), ('156', '156 lbs. / 70.76 kg'), ('157', '157 lbs. / 71.21 kg'), ('158', '158 lbs. / 71.67 kg'), ('159', '159 lbs. / 72.12 kg'),
    ('160', '160 lbs. / 72.57 kg'), ('161', '161 lbs. / 73.03 kg'), ('162', '162 lbs. / 73.48 kg'), ('163', '163 lbs. / 73.94 kg'), ('164', '164 lbs. / 74.39 kg'), ('165', '165 lbs. / 74.84 kg'), ('166', '166 lbs. / 75.30 kg'), ('167', '167 lbs. / 75.75 kg'), ('168', '168 lbs. / 76.20 kg'), ('169', '169 lbs. / 76.66 kg'),
    ('170', '170 lbs. / 77.11 kg'), ('171', '171 lbs. / 77.56 kg'), ('172', '172 lbs. / 78.02 kg'), ('173', '173 lbs. / 78.47 kg'), ('174', '174 lbs. / 78.93 kg'), ('175', '175 lbs. / 79.38 kg'), ('176', '176 lbs. / 79.83 kg'), ('177', '177 lbs. / 80.29 kg'), ('178', '178 lbs. / 80.74 kg'), ('179', '179 lbs. / 81.19 kg'),
    ('180', '180 lbs. / 81.65 kg'), ('181', '181 lbs. / 82.10 kg'), ('182', '182 lbs. / 82.55 kg'), ('183', '183 lbs. / 83.01 kg'), ('184', '184 lbs. / 83.46 kg'), ('185', '185 lbs. / 83.91 kg'), ('186', '186 lbs. / 84.37 kg'), ('187', '187 lbs. / 84.82 kg'), ('188', '188 lbs. / 85.28 kg'), ('189', '189 lbs. / 85.73 kg'),
    ('190', '190 lbs. / 86.18 kg'), ('191', '191 lbs. / 86.64 kg'), ('192', '192 lbs. / 87.09 kg'), ('193', '193 lbs. / 87.54 kg'), ('194', '194 lbs. / 88.00 kg'), ('195', '195 lbs. / 88.45 kg'), ('196', '196 lbs. / 88.90 kg'), ('197', '197 lbs. / 89.36 kg'), ('198', '198 lbs. / 89.81 kg'), ('199', '199 lbs. / 90.26 kg'),
    ('200', '200 lbs. / 90.72 kg'), ('201', '201 lbs. / 91.17 kg'), ('202', '202 lbs. / 91.63 kg'), ('203', '203 lbs. / 92.08 kg'), ('204', '204 lbs. / 92.53 kg'), ('205', '205 lbs. / 92.99 kg'), ('206', '206 lbs. / 93.44 kg'), ('207', '207 lbs. / 93.89 kg'), ('208', '208 lbs. / 94.35 kg'), ('209', '209 lbs. / 94.80 kg'),
    ('210', '210 lbs. / 95.25 kg'), ('211', '211 lbs. / 95.71 kg'), ('212', '212 lbs. / 96.16 kg'), ('213', '213 lbs. / 96.62 kg'), ('214', '214 lbs. / 97.07 kg'), ('215', '215 lbs. / 97.52 kg'), ('216', '216 lbs. / 97.98 kg'), ('217', '217 lbs. / 98.43 kg'), ('218', '218 lbs. / 98.88 kg'), ('219', '219 lbs. / 99.34 kg'),
    ('220', '220 lbs. / 99.79 kg'), ('221', '221 lbs. / 100.24 kg'), ('222', '222 lbs. / 100.70 kg'), ('223', '223 lbs. / 101.15 kg'), ('224', '224 lbs. / 101.60 kg'), ('225', '225 lbs. / 102.06 kg'), ('226', '226 lbs. / 102.51 kg'), ('227', '227 lbs. / 102.97 kg'), ('228', '228 lbs. / 103.42 kg'), ('229', '229 lbs. / 103.87 kg'),
    ('230', '230 lbs. / 104.33 kg'), ('231', '231 lbs. / 104.78 kg'), ('232', '232 lbs. / 105.23 kg'), ('233', '233 lbs. / 105.69 kg'), ('234', '234 lbs. / 106.14 kg'), ('235', '235 lbs. / 106.59 kg'), ('236', '236 lbs. / 107.05 kg'), ('237', '237 lbs. / 107.50 kg'), ('238', '238 lbs. / 107.95 kg'), ('239', '239 lbs. / 108.41 kg'),
    ('240', '240 lbs. / 108.86 kg'), ('241', '241 lbs. / 109.32 kg'), ('242', '242 lbs. / 109.77 kg'), ('243', '243 lbs. / 110.22 kg'), ('244', '244 lbs. / 110.68 kg'), ('245', '245 lbs. / 111.13 kg'), ('246', '246 lbs. / 111.58 kg'), ('247', '247 lbs. / 112.04 kg'), ('248', '248 lbs. / 112.49 kg'), ('249', '249 lbs. / 112.94 kg'),
    ('250', '250 lbs. / 113.40 kg'), ('251', '251 lbs. / 113.85 kg'), ('252', '252 lbs. / 114.31 kg'), ('253', '253 lbs. / 114.76 kg'), ('254', '254 lbs. / 115.21 kg'), ('255', '255 lbs. / 115.67 kg'), ('256', '256 lbs. / 116.12 kg'), ('257', '257 lbs. / 116.57 kg'), ('258', '258 lbs. / 117.03 kg'), ('259', '259 lbs. / 117.48 kg'),
    ('260', '260 lbs. / 117.93 kg'), ('261', '261 lbs. / 118.39 kg'), ('262', '262 lbs. / 118.84 kg'), ('263', '263 lbs. / 119.29 kg'), ('264', '264 lbs. / 119.75 kg'), ('265', '265 lbs. / 120.20 kg'), ('266', '266 lbs. / 120.66 kg'), ('267', '267 lbs. / 121.11 kg'), ('268', '268 lbs. / 121.56 kg'), ('269', '269 lbs. / 122.02 kg'),
    ('270', '270 lbs. / 122.47 kg'), ('271', '271 lbs. / 122.92 kg'), ('272', '272 lbs. / 123.38 kg'), ('273', '273 lbs. / 123.83 kg'), ('274', '274 lbs. / 124.28 kg'), ('275', '275 lbs. / 124.74 kg'), ('276', '276 lbs. / 125.19 kg'), ('277', '277 lbs. / 125.64 kg'), ('278', '278 lbs. / 126.10 kg'), ('279', '279 lbs. / 126.55 kg'),
    ('280', '280 lbs. / 127.01 kg'), ('281', '281 lbs. / 127.46 kg'), ('282', '282 lbs. / 127.91 kg'), ('283', '283 lbs. / 128.37 kg'), ('284', '284 lbs. / 128.82 kg'), ('285', '285 lbs. / 129.27 kg'), ('286', '286 lbs. / 129.73 kg'), ('287', '287 lbs. / 130.18 kg'), ('288', '288 lbs. / 130.63 kg'), ('289', '289 lbs. / 131.09 kg'),
    ('290', '290 lbs. / 131.54 kg'), ('291', '291 lbs. / 132.00 kg'), ('292', '292 lbs. / 132.45 kg'), ('293', '293 lbs. / 132.90 kg'), ('294', '294 lbs. / 133.36 kg'), ('295', '295 lbs. / 133.81 kg'), ('296', '296 lbs. / 134.26 kg'), ('297', '297 lbs. / 134.72 kg'), ('298', '298 lbs. / 135.17 kg'), ('299', '299 lbs. / 135.62 kg'),
    ('300', '300 lbs. / 136.08 kg')
    ])
    submit = SubmitField('NEXT')

class UserProfile3(FlaskForm):
    plan_daily_eat = IntegerField(render_kw={"placeholder": "Eat (Calories)"}, validators=[DataRequired()])
    plan_daily_burn = IntegerField(render_kw={"placeholder": "Burn (Calories)"}, validators=[DataRequired()])
    body_type = RadioField('body_type', choices=[('Round', 'Round'), ('Slender', 'Slender'), ('Athletic', 'Athletic')], validators=[DataRequired()])
    submit = SubmitField('NEXT')

#Models (Persistent Database Entities)
#
#
#
#
#

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True)
    units = db.Column(db.Enum('Imperial', 'Metric'), nullable=True)
    activation_status = db.Column(db.Enum('Active', 'Inactive'), nullable=True)
    activation_date = db.Column(db.Date(), nullable=True)
    last_login = db.Column(db.Date(), nullable=True)
    #Relationships
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #for debugging and testing purposes
    def __repr__(self):
        template = '<User "{0.username}">'
        return template.format(self)

def default_age(context):
    return context.get_current_parameters()['start_age']

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer, nullable=True)
    height_inches = db.Column(db.Integer, nullable=True)
    weight_lbs = db.Column(db.Float, nullable=True)
    body_type = db.Column(db.Enum('Round', 'Slender', 'Athletic'))
    birthday = db.Column(db.Date(), nullable=True)
    start_date = db.Column(db.Date(), nullable=True)
    start_age = column_property('birthday - start_date') # use " " if problems
    updated_aged = db.Column(db.Float, default=default_age)
    goal_weight_lbs = db.Column(db.Integer, nullable=True)
    rest_meta_rate = db.Column(db.Integer, nullable=True)
    plan_daily_eat = db.Column(db.Integer, nullable=True)
    plan_daily_burn = db.Column(db.Integer, nullable=True)
    plan_daily_change_lbs = column_property('-((rest_meta_rate - plan_daily_eat + plan_daily_burn)/3500)') # use " " if problems
    #relationships
    logs = db.relationship('Log', backref='profile')
    forecasts = db.relationship('Forecast', backref='profile')
    users = db.relationship('User', uselist=False, backref='profile')

    #for debugging and testing purposes
    def __repr__(self):
        template = '<Gender "{0.gender}"> <Height "{0.height_inches}">'
        return template.format(self)

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    log_datetime = db.Column(db.DateTime(), nullable=True)
    log_burn = db.Column(db.Integer, nullable=True)
    log_eat = db.Column(db.Integer, nullable=True)
    log_energy_remaining = db.Column(db.Integer, nullable=True)
    log_body_change_lbs = db.Column(db.Float, nullable=True)
    log_updated_weight_lbs = db.Column(db.Float, nullable=True)
    distance_from_goal_lbs = db.Column(db.Float, nullable=True)
    new_rest_meta_rate = db.Column(db.Integer, nullable=True)
    #relationships
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    #for debugging and testing purposes
    def __repr__(self):
        template = '<DateTime "{0.log_datetime}"> <Burn "{0.log_burn}">'
        return template.format(self)

class Forecast(db.Model):
    __tablename__ = 'forecasts'
    id = db.Column(db.Integer, primary_key=True)
    forecast_current_date = db.Column(db.DateTime(timezone=True), default=func.now())
    forecast_projected_date = db.Column(db.Date(), nullable=True)
    forecast_total_days = column_property('forecast_projected_date - forecast_current_date') # use " " if problems
    forecast_body_change_lbs = db.Column(db.Float, nullable=True)
    forecast_projected_weight_lbs = db.Column(db.Float, nullable=True)
    #relationships
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    #for debugging and testing purposes
    def __repr__(self):
        template = '<Current Date "{0.forecast_current_date}"> <Projected Date "{0.forecast_projected_date}">'
        return template.format(self)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    #relationships
    users = db.relationship('User', backref='role', lazy='dynamic')

    #for debugging and testing purposes
    def __repr__(self):
        template = '<Role "{0.name}">'
        return template.format(self)
