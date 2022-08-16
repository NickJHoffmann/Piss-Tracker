import sqlalchemy.dialects.postgresql
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import relationship

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(sqlalchemy.dialects.postgresql.UUID, primary_key=True, server_default=text("uuid_generate_v4()")) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(100))

    entries = relationship("Entry", cascade="all, delete", passive_deletes=True)



class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(sqlalchemy.dialects.postgresql.UUID, ForeignKey("users.id"), primary_key=True)
    timestamp = db.Column(sqlalchemy.dialects.postgresql.TIMESTAMP, primary_key=True, server_default=text("NOW()"))
    duration = db.Column(db.Float, nullable=False)
