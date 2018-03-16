from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FaskSskills.templates.test import A
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:123456@host:port/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'