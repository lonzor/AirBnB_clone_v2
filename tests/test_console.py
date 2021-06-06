#!/usr/bin/python3
"""Module for unittesting the console"""


from io import StringIO
import sys
import unittest
from unittest.mock import patch
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand


fs = FileStorage()


class TestConsole(unittest.TestCase):
    """A class to test console"""

    def test_state(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='California'")
            st_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(st_id[:-1]))
            st = f.getvalue()
        self.assertIn(st_id[:-1], st)

if __name__ == '__main__':
    unittest.main()
