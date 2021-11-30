from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from. import new_templates
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, Funcs, Api, Coin_Price, Total_Balance


sub = Blueprint('sub', __name__)


@sub.route('/sol', methods=['GET', 'POST'])
def sol():
    return render_template('sol.html', user=current_user, funcs=Funcs(), api=Api(), coin_price=Coin_Price(), tots=Total_Balance())