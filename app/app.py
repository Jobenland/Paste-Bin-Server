from flask import (Blueprint, render_template, request, session,
                   redirect, flash, url_for, g, current_app)
from flask_login import (login_user, logout_user, current_user, login_required)

from . import db
from .models import User
from .utils import validate_captcha

import json

main = Blueprint('main', __name__)


@main.before_app_request
def before_request():
    g.user = current_user


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    try:
        my_var = session.get('status', None)
    except:
        my_var = ' '
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if current_app.config.get('SHOW_CAPTCHA'):
        captcha_response = request.form.get('g-recaptcha-response')
        if not validate_captcha(captcha_response):
            flash('Bad Captcha')
            return redirect(url_for('main.register'))

    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if password != password_confirm:
        flash('Passwords must match!')
        return redirect(url_for('main.register'))

    user = User.create(email, password)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        flash('User already exists!')
        return redirect(url_for('main.register'))

    return redirect(url_for('main.login'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['email']
    password = request.form['password']

    if current_app.config.get('SHOW_CAPTCHA'):
        captcha_response = request.form.get('g-recaptcha-response')
        if not validate_captcha(captcha_response):
            flash('Bad Captcha')
            return redirect(url_for('main.login'))

    registered_user = User.get_user(username, password)

    if registered_user is None:
        flash('Username or Password is invalid')
        return redirect(url_for('main.login'))
    else:
        login_user(registered_user)

    return redirect(url_for('main.index'))

@main.route('/add', methods=['POST'])
def add():
    text = request.form['paste']
    key = request.form['key']
    print(text)
    print(key)
    if key == '' or text == '':
        flash("Both feilds must be filled")
        return redirect(url_for('main.index'))
    else:
        unique = findkey(key)
        if unique == True:
            elem = {'text': text, 'key': key}
            addtext(elem)
            data = "Your message has been saved. Your retreval code is " + key
            session['status'] = "Your message has been saved. Your retreval code is " + key
            return render_template("index.html", data=data)
        else:
            flash("Key has already been used. Use a different key")
            return redirect(url_for('main.index'))
    
@main.route('/retreive', methods=['GET', 'POST'])
def retreive():
    return render_template('findtext.html')

@main.route('/get', methods=['GET', 'POST'])
def get():
    key = request.form['key']
    if key == '':
        flash("Key feild must be filled")
        return redirect(url_for('main.retreive'))
    else:
        repeat = findkey(key)
        if repeat:
            flash("Key does not exist")
            return render_template("findtext.html")
        else:
            data = findtext(key)
            return render_template("findtext.html", data=data)

@main.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))

def addtext(elem):
    try:
        with open ("text.json") as f:
            data = json.load(f)
        if type(elem) is dict:
            data.append(elem)
        with open ("text.json","w") as f:
            json.dump(data, f)

    except FileNotFoundError:
        if type(elem) is dict:
            data = [elem]
        with open ("text.json",'w') as f:
            json.dump(data, f)

def findkey(key):

    with open('text.json',"r",encoding="utf8") as json_file:
        data = json_file.read() 
    obj = json.loads(data)

    for elem in range(len(obj)):
        if obj[elem]['key'] == key:
            return False
    return True

def findtext(key):
    with open('text.json',"r",encoding="utf8") as json_file:
        data = json_file.read() 
    obj = json.loads(data)

    for elem in range(len(obj)):
        if obj[elem]['key'] == key:
            return obj[elem]['text']
    return ''