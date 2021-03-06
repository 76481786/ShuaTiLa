from flask import Flask
from flask_moment import Moment
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown

moment = Moment()
pagedown = PageDown()
login_mamager = LoginManager()
login_mamager.session_protection = 'strong'
# login_mamager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    pagedown.init_app(app)
    login_mamager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .exam import exam as exam_blueprint
    app.register_blueprint(exam_blueprint, url_prefix='/exam')

    from .forum import forum as forum_blueprint
    app.register_blueprint(forum_blueprint, url_prefix='/forum')

    from .test import test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix='/test')

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app
