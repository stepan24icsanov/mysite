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


@admin.route('/edit_article/')
def edit_articles():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    articles_list = Post.query
    pages = articles_list.paginate(page=page, per_page=4)
    return render_template('/admin/edit-articles.html', pages=pages)



@admin.route('/edit_article/<int:post_id>', methods=['POST', 'GET'])
def edit_article(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST':
        try:
            post.title = request.form['title']
            post.header = request.form['header']
            post.text = request.form['text']
            db.session.commit()
            return redirect(url_for('.edit_articles'))
        except:
            return 'Error'
    else:
        return render_template('/admin/edit-article.html', post=post)