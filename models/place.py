#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import os
from sqlalchemy.orm import relationship
from models.amenity import Amenity

storage_data = os.getenv("HBNB_TYPE_STORAGE")

place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False
            ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False
            ),
        )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_data == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', cascade="all,delete", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, back_populates="place_amenities")
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
            """getter attribute reviews"""
            from models import storage
            rvwlst = []
            rvwlstAll = storage.all(Review)
            for review in rvwlstAll.values():
                if review.place_id==self.id:
                    rvwlst.append(review)
            return rvwlst

        @property
        def amenities(self):
            """Getter amenities"""
            from models import storage
            amenlist = []
            amenAll = storage.all(Amenity)
            for amenity in amenAll.values():
                if amenity.ids in self.amenity_ids:
                    amenlist.append(amenity)
            return amenlist

        @amenities.setter
        def amenities(self, amenity):
            """Setter amenities"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
