from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///builds.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from app import views

from app.builds import views
from app.builds import models

db.create_all()
