from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.settings import DB_CON_STRING

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CON_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from src import models
from src import views
db.create_all()
