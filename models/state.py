#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        cities_list = []
        tmp_dic = models.storage.all(City)
        for key in tmp_dic:
            if tmp_dic[key].state_id == self.id:
                cities_list.append(tmp_dic[key])
        return cities_list
