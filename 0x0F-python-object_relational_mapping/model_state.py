#!/usr/bin/python3
"""
Defines a State class using SQLAlchemy.
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state entity in a database.

    Attributes:
        __tablename__ (str): The name of the corresponding database table.
        id (Column): An auto-incrementing integer primary key for the state.
        name (Column): A string column representing the name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
