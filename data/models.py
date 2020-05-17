import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Hero(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'Hero'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    build = relationship("Build", back_populates='Hero')
    spell = relationship("Spell", back_populates='Hero')


class Spell(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'Spell'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    leveling = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Build(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'Build'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    early = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    midgame = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lategame = sqlalchemy.Column(sqlalchemy.String, nullable=True)
