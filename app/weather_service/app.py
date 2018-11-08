from flask import Flask
from .config import config_by_name
from weather_service.info import info_bp
import weather_service.info.views


def create_app(config_name='dev'):
    app = Flask(__name__)
    app.register_blueprint(info_bp)
    app.config.from_object(config_by_name[config_name])
    return app
