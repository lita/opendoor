import logging
from os import getenv

from flask import Flask

from models import db
from routes import blueprint

LOG_FILENAME = 'app.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


def create_app():
    app = Flask(__name__)

    app.config["MONGODB_SETTINGS"] = {
        "host": getenv("MONGOLAB_URI", None),
    }
    app.config["SECRET_KEY"] = "KeepThisS3cr3t"

    app.register_blueprint(blueprint)

    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()