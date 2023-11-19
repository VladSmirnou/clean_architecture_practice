from flask import Flask
from presentation.flask_app.routers.routers import calculator_bprint
from infrastructure.flask_app.interfaces.controller_interface import \
    IFlaskController


def init_app(controller: IFlaskController):
    app = Flask(__name__)
    # I set this controller into the app object
    # for now just to make it more aligned with the Cli
    # app creation process, but in general it is forbidden
    # to do so.
    setattr(calculator_bprint, 'controller', controller)
    app.register_blueprint(calculator_bprint)
    return app