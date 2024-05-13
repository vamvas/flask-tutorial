import os
from flask import Flask

def create_app(test_config=None):
    # initialise Flask object
    app = Flask(__name__, instance_relative_config = True)

    # default configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # override default configuration when not testing
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load test config, when testing
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # create a simple page
    @app.route('/hello')
    def hello():
        return "Hello, world"
    
    from . import db
    db.init_app(app)

    return app
