from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, Funcs, Api


pages = Blueprint('pages', __name__)

@pages.route('/stocks', methods=['GET', 'POST'])
@login_required
def stocks():
    return render_template('stocks.html', user=current_user)

@pages.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin.html', user=current_user)

@pages.route('/chains', methods=['GET', 'POST'])
@login_required
def chains():
    return render_template('chains.html', user=current_user)

@pages.route('/tesla_charts', methods=['GET', 'POST'])
def tesla_charts():
    return render_template('tesla_charts.html', user=current_user)

@pages.route('/pltr_charts', methods=['GET', 'POST'])
def pltr_charts():
    return render_template('pltr_charts.html', user=current_user)

@pages.route('/photos', methods=['GET', 'POST'])
def photos():
    return render_template('photos.html', user=current_user)

@pages.route('/3d', methods=['GET', 'POST'])
def _3d_print():
    return render_template('3d_prints.html', user=current_user)

@pages.route('/rklb',methods=['GET', 'POST'])
def rklb():
    return render_template('rklb.html', user=current_user)