#!/usr/bin/python3
"""tests for db storage"""
import unittest
import sys
import os
from io import StringIO
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from unittest.mock import patch
from console import HBNBCommand


class test_db_storage(unittest.TestCase):

    """Class for testing db_storage"""

    def test_storage(self):
        """test the entirity of db_storage"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='California'")
            state = f.getvalue()
            state = state[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City state_id='" + state +
                                 "' name='San_Francisco_is_super_cool'")
            city = f.getvalue()
            city = city[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User email='my@me.com' " +
                                 "password='pwd' first_name='FN' " +
                                 "last_name='LN'")
            user = f.getvalue()
            user = user[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place city_id='" + city +
                                 "' user_id='" + user +
                                 "' name='My_mansion' " +
                                 "description='no_description_yet' " +
                                 "number_rooms=4 number_bathrooms=1 " +
                                 "max_guest=3 price_by_night=100 " +
                                 "latitude=120.12 longitude=101.4")
            place = f.getvalue()
            place = place[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(place))
            show = f.getvalue()

        self.assertIn(place, show)
        self.assertIn(city, show)
        self.assertIn(user, show)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(state))
            st_show = f.getvalue()

        self.assertIn(state, st_show)

if __name__ == '__main__':
    unittest.main()
