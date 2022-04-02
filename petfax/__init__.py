from flask import Flask
from flask_migrate import Migrate

from petfax.config import DATABASE_URI

def create_app():
    app = Flask(__name__)

    from . import pet
    from . import fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def hello():
        return "Hello, PetFax!"

    return app
