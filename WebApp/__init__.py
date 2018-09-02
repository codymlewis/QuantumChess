import os
from flask import Flask, render_template
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # blueprint registration
    from . import Main
    app.register_blueprint(Main.bp)

    return app

RAS_APP = create_app()

@RAS_APP.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error=404), 404

@RAS_APP.errorhandler(500)
def internal_error(e):
    return render_template("error.html", error=500), 500
