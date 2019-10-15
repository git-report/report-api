import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.gitlab_data import gitlab_data_blueprint
    from project.api.metrics import metrics_blueprint
    from project.api.requirements import requirements_blueprint
    app.register_blueprint(gitlab_data_blueprint)
    app.register_blueprint(metrics_blueprint)
    app.register_blueprint(requirements_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
