#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
import os
from sqlalchemy import (create_engine)
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The mysql database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(os.getenv('HBNB_MYSQL_USER'),
                                                 os.getenv('HBNB_MYSQL_PWD'),
                                                 os.getenv('HBNB_MYSQL_HOST'),
                                                 os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True)

        Session = sessionmaker(bind=engine)

        self.__session = Session()

        if os.getenv('HBNB_ENV') == 'test':
            self.__session.drop_all()

    def all(self, cls=None):
        if cls:
            data = self.__session.query(cls)
        else:
            data = self.__session.query(User, State, City, Amenity, Place, Review)

