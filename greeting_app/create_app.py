from flask import Flask
from flask_migrate import Migrate

def create_app(config_filename="greeting_app.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from greeting_app.models.db import db 
    from greeting_app.models.db import migrate
    from greeting_app.app import bp

    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)

    return app