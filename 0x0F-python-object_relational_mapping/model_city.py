#!/usr/bin/python3
"""
Defines a City class using SQLAlchemy.
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class to represent a city in the database.
    """
    __tablename__ = "cities"

    id = Column(Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """
        Representation
        """
        return f"{self.state_id}: ({self.id}) {self.name}"
