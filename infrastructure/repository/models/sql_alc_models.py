from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Calculation(db.Model):
    __tablename__ = 'calculations'

    results = db.Column(db.String(100), primary_key=True)
