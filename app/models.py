from app import db




class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    header = db.Column(db.String(150), nullable=False)
    text = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.post_id