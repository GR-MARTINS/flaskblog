from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def init_app(app):
    login_manager.init_app(app)
