#!/usr/bin/python3
"""
Module to connect python backend to web server
Packs up web_static
Deploys archive
"""


from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['35.237.103.166', '3.88.182.73']


def do_deploy(archive_path):
    """ Deploys the archive """

    if not os.path.exists(archive_path):
        return False

    try:
        arch_name = archive_path[9:]
        name_no_ext = arch_name[:-4]

        tar_cmnd = "tar -xzvf /tmp/" + arch_name + " -C "
        rel_dir = "/data/web_static/releases/"
        cur_dir = "/data/web_static/current"

        put(archive_path, '/tmp/' + arch_name)

        run("mkdir -p " + rel_dir + name_no_ext)
        run(tar_cmnd + rel_dir + name_no_ext + " --strip-components=1")
        run("rm -f /tmp/" + arch_name)
        run("rm -f " + cur_dir)
        run("ln -sf " + rel_dir + name_no_ext + " " + cur_dir)
        return True
    except:
        return False


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
