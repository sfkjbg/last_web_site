from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text='"from" test_text_ (auth.py) (login.html)')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash("Name must be at least 3 characters", category='error')
        elif len(password1) < 7:
            flash('Password is too short', category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        else:
            flash("Account Created", category='success')

    return render_template('sign_up.html')

@auth.route('/stocks', methods=['GET', 'POST'])
def stocks():
    return render_template('stocks.html')