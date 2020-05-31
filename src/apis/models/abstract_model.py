from flask_sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, MetaData
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
BaseModel = db.Model

def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return db