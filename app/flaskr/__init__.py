import os
from flask import Flask
from flaskr.database import db

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(app.instance_path, "flaskr.db")),
        # SQLALCHEMY_TRACK_MODIFICATIONS = False,
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    # from flaskr import db
    db.init_app(app)
  


    # apply the blueprints to the app
    from flaskr import home, translation
    app.register_blueprint(home.bp)
    app.register_blueprint(translation.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
