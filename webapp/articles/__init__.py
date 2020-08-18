from flask import Blueprint


arti = Blueprint('articles', __name__, template_folder='templates', url_prefix='/articles')


from webapp.articles import articles_routes