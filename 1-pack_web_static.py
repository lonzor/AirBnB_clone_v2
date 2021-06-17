#!/usr/bin/python3
"""Module creates a .tgz file"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """packs up all files web_static"""
    try:
        now = datetime.now()
        ta_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        ta_path = "versions/" + ta_name
        local("mkdir -p versions")
        local("tar -czvf " + ta_path + " web_static")
        return ta_path
    except:
        return None
