#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

storage_data = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel):
    """ A place to stay """

    __tablename__ = "places"
    if storage_data == "db":
        reviews = relationship('Review', cascade="all,delete",
                backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        ongitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of Review"""
        from models import storage
        rvwLst = []
        rvwLstAll = storage.all(Review)
        for review in rvwLstAll.values():
            if review.place_id in self.id:
                rvwLst.append(review)
        return rvwLst
    
