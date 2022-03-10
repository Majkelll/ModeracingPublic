from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required

views = Blueprint("views", __name__)


@views.route('/home')
@views.route('/')
def home():
    return render_template('./views/home.html', user=current_user)


@views.route('/lessons')
def lessons():
    return render_template('./views/lessons.html', user=current_user)


@views.route('/games')
def games():
    return render_template('./views/games.html', user=current_user)


@views.route('/special')
def special():
    return render_template('./views/special.html', user=current_user)


@views.route('/game')
def mainGame():
    return render_template('./views/maingame.html', user=current_user)
