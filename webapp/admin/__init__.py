from flask import Blueprint


admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

from webapp.admin import admin_routes
