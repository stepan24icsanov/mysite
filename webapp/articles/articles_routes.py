from flask import request, render_template, redirect, url_for, jsonify
from flask_login import current_user
import datetime

from webapp import db
from webapp.models import Post, Comment
from webapp.articles import arti


@arti.route('/')
def articles():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    articles_list = Post.query
    pages = articles_list.paginate(page=page, per_page=4)
    return render_template('/articles/articles.html', pages=pages)


@arti.route('/<int:post_id>', methods=['POST', 'GET'])
def show_post(post_id):
    post = Post.query.get(post_id)
    if request.method == 'GET':
        comments = Comment.query.filter_by(post_id=post_id).all()
        return render_template('/articles/article.html', post=post, comments=comments)
    else:
        comment_text = request.form['text']
        comment_creation_date = datetime.datetime.utcnow()
        comment = Comment(post_id=post_id,
                          user_name=current_user.user_name,
                          text=comment_text,
                          comment_creation_date=comment_creation_date)
        try:
            db.session.add(comment)
            db.session.commit()
        except:
            return 'Error'
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('/articles/article.html', post=post, comments=comments)

