from flask import request, render_template, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user

from webapp import app, db
from webapp.models import User


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(user_name=login).first()

        if password == user.user_password:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(url_for('index'))
        else:
            flash('Неверный логин или пароль')
            return redirect(url_for('login_page'))
    else:
        return render_template('auth/login_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # email = request.form['email']
        login = request.form['login']
        password = request.form['password']
        password2 = request.form['password2']
        if password != password2:
            flash('введенные пароли не совпадают')
            return redirect(url_for('register_page'))

        new_user = User(user_name=login, user_password=password, user_email='123321')
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return 'error'

        return redirect('/login')
    else:
        return render_template('auth/register_page.html')


@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect(url_for('index'))



