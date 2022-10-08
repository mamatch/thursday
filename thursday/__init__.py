from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config

db = SQLAlchemy()
boots = Bootstrap()


def create_app(config_name: str):
    """
    A function to create an instance of flask app
    :param config_name: the run mode ["dev", "test", "prod"]
    :return: A flask application instance
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # initialisation of modules
    db.init_app(app)
    boots.init_app(app)

    # insert routes, blueprints, etc....
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
