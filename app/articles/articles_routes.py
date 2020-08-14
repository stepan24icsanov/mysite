from flask import request, render_template
from app.models import Post
from app.articles import arti




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


@arti.route('/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    return render_template('/articles/article.html', post=post)