import os

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    from project.api.list import list_bp
    app.register_blueprint(list_bp, url_prefix='/list')

    from project.api.item import item_bp
    app.register_blueprint(item_bp, url_prefix='/item')

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    @app.route('/')
    def index():
        return jsonify({'status': 'success'})

    return app
