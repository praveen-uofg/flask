import os
from flask import Flask
from app.settings import config
from app.blueprints.ping.api import ping_blueprint
from app.blueprints.record.api import record_blueprint
from app.blueprints.error_handler.errors import errors


def setup_app():
    app = Flask(__name__)
    app.register_blueprint(ping_blueprint, url_prefix="/v1/ping")
    app.register_blueprint(errors)
    app.register_blueprint(record_blueprint, url_prefix="/v1/records")

    config_name = os.getenv('ENVIRONMENT')
    if not config_name:
        config_name = "development"
    app.config.from_object(config.app_config[config_name])
    return app
