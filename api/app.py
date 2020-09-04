from flask import Flask
from flask_migrate import Migrate


from api.extentions import db
from api.extentions import mail
from api.extentions import login_manager


def create_app(settings_override=None):

    app = Flask(__name__, instance_relative_config=True)

    migrate = Migrate(app, db)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override:
        app.config.update(settings_override)

    
    # with app.app_context():
    #     from cli import commands

    extensions(app)


    return app

def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    return None