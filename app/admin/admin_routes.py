from flask import (session,
                   render_template,
                   redirect,
                   url_for,
                   request)
from app.admin import admin
from app.models import Post
from app import db


def login_admin():
    session['admin_logged'] = 1


def isLogged():
    return True if session.get('admin_logged') else False


def logoutAdmin():
    session.pop('admin_logged', None)


@admin.route('/')
def index():
    if not isLogged():
        return redirect(url_for('.login'))

    return render_template('admin/admin-panel.html')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    if isLogged():
        return redirect(url_for('.index'))

    if request.method == 'POST':
        if request.form['login'] == 'stepan24' and request.form['password'] == 'stepank':
            login_admin()
            return redirect(url_for('.index'))
        else:
            return redirect(url_for('.login'))

    return render_template('admin/admin-login.html')


@admin.route('/logout', methods=['POST', 'GET'])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))
    logoutAdmin()
    return redirect(url_for('.login'))


@admin.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        header = request.form['header']
        text = request.form['text']
        post = Post(title=title, header=header, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/articles')
        except:
            return 'Error'
    else:
        return render_template('/admin/create-articles.html')