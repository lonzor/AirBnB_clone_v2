#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True,),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref="place_amenities")
    amenity_ids = []

    @property
    def reviews(self):
        """getter for reviews"""
        from models.review import Review
        from models import storage
        review_list = []
        tmp_dic = storage.all(Review)
        for key in tmp_dic:
            if tmp_dic[key].place_id == self.id:
                review_list.append(tmp_dic[key])
        return review_list

    @property
    def amenities(self):
        """ getter for amenities """
        from models.amenity import Amenity
        from models import storage
        tmp_dic = storage.all(Amenity)
        for key in tmp_dic:
            if tmp_dic[key].place_amenity == self.id:
                self.amenity_ids.append(tmp_dic[key])
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """setter for amenities"""
        if obj == Amenity:
            self.amenity_ids.append(obj.id)
