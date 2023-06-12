from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
import uuid

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(100))

    entries = relationship("Entry", cascade="all, delete", passive_deletes=True)


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(UUID, ForeignKey("users.id"), primary_key=True)
    timestamp = db.Column(TIMESTAMP, primary_key=True, server_default=text("NOW()"))
    duration = db.Column(db.Float, nullable=False)
