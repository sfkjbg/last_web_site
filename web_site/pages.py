from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


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