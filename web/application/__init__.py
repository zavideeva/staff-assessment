import os

from flask import Flask, redirect, url_for
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)
    # TODO Potential CSRF vulnerability
    # should be removed on production server
    # use for development only
    CORS(app)
    app.config.from_mapping(
        TEMPLATES_AUTO_RELOAD=True,
        # TODO replace with env variable
        SECRET_KEY='secretkey228',
    )

    # Register all blueprints to the app
    from application.views import auth

    app.register_blueprint(auth.bp)

    return app
