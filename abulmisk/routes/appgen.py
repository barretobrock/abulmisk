from flask import Flask
from pukr import (
    InterceptHandler,
    get_logger,
)

# Internal packages
from abulmisk.configurations import BaseConfig
from abulmisk.flask_base import (
    bcrypt,
    db,
    log_mgr,
)
from abulmisk.routes.admin import admin
from abulmisk.routes.api import api
from abulmisk.routes.koned import koned
from abulmisk.routes.main import main
from abulmisk.routes.projects import projects
from abulmisk.routes.user import users


def create_app(*args, **kwargs) -> Flask:
    """Creates a Flask app instance"""
    # Config app
    config_class = kwargs.pop('config_class', BaseConfig)
    app = Flask(__name__, static_folder=config_class.STATIC_DIR_PATH,
                template_folder=config_class.TEMPLATE_DIR_PATH)
    app.config.from_object(config_class)
    # Initialize things that supports app
    db.init_app(app)
    bcrypt.init_app(app)
    log_mgr.init_app(app)

    # Register logger, bind handler into flask app
    logger = get_logger('abulmisk', app.config.get('LOG_DIR'), show_backtrace=True, base_level='DEBUG')
    logger.debug('Logger started. Binding to app handler.')
    app.logger.addHandler(InterceptHandler(logger=logger))
    app.extensions.setdefault('loguru', logger)

    # Register routes
    for rt in [admin, api, koned, main, projects, users]:
        app.register_blueprint(rt)

    return app
