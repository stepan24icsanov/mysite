from flask_login import UserMixin

from webapp import db
from webapp.auth import login_manager


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    header = db.Column(db.String(150), nullable=False)
    text = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.post_id


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(64), nullable=False)
    user_password = db.Column(db.String(32), nullable=False)
    user_name = db.Column(db.String(32), nullable=False, unique=True)

    def get_id(self):
        return (self.user_id)

    def __repr__(self):
        return f'<User {self.user_id}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
