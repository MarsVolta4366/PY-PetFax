from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import pet
    from . import fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    @app.route("/")
    def hello():
        return "Hello, PetFax!"

    return app
