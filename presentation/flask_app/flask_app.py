from flask import Flask
from presentation.flask_app.routers.routers import calculator_bprint
from infrastructure.flask_app.interfaces.controller_interface import \
    IFlaskController
from infrastructure.repository.models.sql_alc_models import db
from flask_migrate import Migrate


def init_app(controller: IFlaskController):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:JkdsL%26%252dS%5E%40%232@localhost:5432/applicationdb'
    # I set this controller into the app object
    # for now just to make it more aligned with the Cli
    # app creation process, but in general it is forbidden
    # to do so.
    db.init_app(app)
    migrate = Migrate(app, db)

    setattr(calculator_bprint, 'controller', controller)
    app.register_blueprint(calculator_bprint)
    return app
