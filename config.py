import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask_user:your_password@localhost/exchange_rates_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
