#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
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
                                                 os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            drop_all(self.__session)

    def all(self, cls=None):
        cls_list = [State, City, Place, Review, User, Amenity]
        tmp_dic = {}
        if cls:
            data = self.__session.query(cls)
            for inst in data:
                tmp_dic[cls.__name__ + "." + inst.id] = inst
        else:
            i = 0
            while i < len(cls_list):
                for inst in self.__session.query(cls_list[i]):
                    tmp_dic[type(inst).__name__ + "." + inst.id] = inst
                i += 1
        return tmp_dic

    def new(self, obj):
            self.__session.add(obj)

    def save(self):
            self.__session.commit()

    def delete(self, obj=None):
            if obj:
                self.__session.delete(obj)

    def reload(self):
            Base.metadata.create_all(self.__engine)
            new_session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
            Session = scoped_session(new_session)
            self.__session = Session()
