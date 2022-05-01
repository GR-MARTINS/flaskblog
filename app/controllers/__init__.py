from app.controllers.main import main
from app.controllers.handlers import errors
from app.controllers.posts import posts
from app.controllers.users import users


def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(posts)
    app.register_blueprint(users)
