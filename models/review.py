#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from os import getenv

storage_data = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"
    if storage_data == "db":
        text = Column(Text:wq(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
