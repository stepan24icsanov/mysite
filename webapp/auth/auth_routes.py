from flask import request, render_template, redirect, flash, url_for, jsonify
from flask_login import login_user, login_required, logout_user
import datetime

from webapp import app, db
from webapp.models import User


@app.route('/login', methods=['POST'])
def user_login_page():
    login = request.form['login']
    password = request.form['password']
    user = User.query.filter_by(user_name=login).first()

    if user is None:
        return jsonify({'status': 'not ok'})

    if password == user.user_password:
        login_user(user)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'wrong password'})




@app.route('/register', methods=['GET', 'POST'])
def user_register_page():
    if request.method == 'POST':
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']
        password2 = request.form['password2']
        user_registration_date = datetime.datetime.utcnow()
        if password != password2:
            flash('введенные пароли не совпадают')
            return redirect(url_for('user_register_page'))

        new_user = User(user_name=login,
                        user_password=password,
                        user_email=email,
                        user_registration_date=user_registration_date)
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
def user_logout_page():
    logout_user()
    next_page = request.args.get('next')
    return redirect(next_page)



