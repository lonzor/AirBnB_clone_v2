#!/usr/bin/python3
"""Module creates a .tgz file"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """packs up all files web_static"""
    try:
        now = datetime.now()
        taName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        taPath = "versions/" + taName
        local("mkdir -p versions")
        local("tar -czvf " + taPath + "web_static")
        return taPath
    except:
        return None
