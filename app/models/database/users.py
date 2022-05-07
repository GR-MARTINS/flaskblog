from app.ext.database import db
from app.ext.flask_login import login_manager
from flask_login import UserMixin
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(20),
        nullable=False,
        default='default.jpg'
    )
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self):
        return create_access_token(identity=self.id)

    @staticmethod
    @jwt_required()
    def verify_reset_token():
        try:
            user_id = get_jwt_identity()
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
