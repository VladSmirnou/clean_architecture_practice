from flask import Flask
from presentation.flask_app.routers.routers import calculator_bprint
from infrastructure.repositories.models.sql_alc_models import db
from flask_migrate import Migrate


def init_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/applicationdb'

    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(calculator_bprint)
    return app
