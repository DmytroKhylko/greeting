from flask import Flask

def create_app(config_filename="greeting_app.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from greeting_app.app import bp
    app.register_blueprint(bp)

    return app