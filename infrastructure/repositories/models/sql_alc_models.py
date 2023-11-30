from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()


class Calculation(db.Model):
    __tablename__ = 'calculations'

    results = db.Column(db.String(100), primary_key=True)
    date_calculated = db.Column(db.DateTime, default=datetime.date.today())
