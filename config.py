from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aleks1604@localhost:1604/rpp'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
