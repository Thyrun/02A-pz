from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Currencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(100), nullable=False)
    currency_code = db.Column(db.String(10), nullable=False, unique=True)
    exchange_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Waluta {self.code}>'
