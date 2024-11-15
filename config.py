import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = os.getenv('FLASK_DB_USER')
db_password = os.getenv('FLASK_DB_PASSWORD')
db_name = os.getenv('FLASK_DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}'

db = SQLAlchemy(app)
