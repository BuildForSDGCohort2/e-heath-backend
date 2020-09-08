from flask import Flask


from api.extentions import db
from api.extentions import migrate
from api.extentions import mail
from api.extentions import login_manager
from api.blueprints.auth import user
from api.blueprints.user.models import User



def create_app(settings_override=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(user)
    extensions(app)

    return app


def extensions(app):
    """ Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return None