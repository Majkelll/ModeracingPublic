from flask import Blueprint, flash, render_template, request, redirect, url_for
from . import db, mail
from .models import User
from .scripts import authScripts
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Message
import time

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if request.form.get('data') == "login":
            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                if user.confirm_acc:
                    if check_password_hash(user.password, password):
                        flash("Login success", category='success')
                        login_user(user, remember=True)
                        return redirect(url_for('views.home'))
                    else:
                        flash('Password incorect', category='error')
                else:
                    flash('Email confrim', category='error')
            else:
                flash('Your email is not confirm', category='error')

        if request.form.get('data') == "signup":
            email = request.form.get("email")
            password = (request.form.get("password"),
                        request.form.get("password2"))
            email_exist = User.query.filter_by(email=email).first()
            if email_exist:
                flash("Email exists", category='error')
            elif not authScripts.emailValidation(email):
                flash("Invalid email", category='error')
            elif not authScripts.passwordValidation(password[0], password[1]):
                flash("Invalid password", category='error')
            else:
                new_user = User(email=email, username=authScripts.defaultNick(email),
                                password=generate_password_hash(password[0], method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('User created', category='success')
                # send confirm email
                email_send(email)
                # login_user(new_user, remember=True)
                # return redirect(url_for('views.home'))

    return render_template('./auth/login.html', user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/email/<email>")
def email_send(email):
    user = User.query.filter_by(email=email).first()
    msg = Message('Email confirmation', sender='michalwitkotestemail@gmail.com',
                  recipients=[email])
    try:
        msg.body = f"http://127.0.0.1:5000/confirm/{user.confirm_key}"
        mail.send(msg)
    except:
        return '0'
    return '1'


@auth.route("/confirm/<key>")
def confirm_email(key):
    user = User.query.filter_by(confirm_key=key).first()
    print(user)
    try:
        user.confirm_acc = True
        db.session.commit()
    except:
        return '0'
    return '1'


@auth.route('/account', methods=["GET", "POST"])
@login_required
def account():
    if request.method == 'POST':
        if request.form.get('data') == "changeUsername":
            newUsername = request.form.get('nick')
            if len(newUsername) > 2 and len(newUsername) < 15:
                current_user.username = newUsername
                db.session.commit()
                flash("Changed username", category='success')
            else:
                flash("Too shor or too long", category='error')

        if request.form.get('data') == 'changePassword':
            password_1 = request.form.get('password')
            password_2 = request.form.get('password2')
            if password_1 == password_2:
                current_user.password = generate_password_hash(
                    password_1, method='sha256')
                db.session.commit()
                flash("Changed Password")
            else:
                flash("Passwords dont match", category='error')
    return render_template('./views/account.html', user=current_user)
