#!/usr/bin/python3
""" Module connecting web server to python """


from fabric.ap import local, env, put, run
from datetime import datetime
import os


env.hosts = ['35.237.103.166', '3.88.182.73']


def deploy():
    """ Runs the deploy """

    archive = do_pack()
    if archive is None:
        return False

    status = do_deploy(archive)
    return status

def do_deploy():
    """ Deploys the archive """

    if not os.path.exists(archive_path):
        return False
    try:
        archName = archive_path[9:]
        archNameNoExt = archName[:-4]
        tarCmnd = "sudo tar -xzvf /tmp/" + archName + " -C "
        rel_dir = "/data/web_static/releases/"
        cur_dir = "/data/web_static/current/"
        put(archive_path, '/tmp/' + archName)
        run("sudo mkdir -p " + rel_dir + archNameNoExt)
        run(tarCmnd + rel_dir + archNameNoExt + " --strip-components=1")
        run("sudo rm -f /tmp/" + archName)
        run("sudo rm -f " + cur_dir)
        run("sudo ln -sf " + rel_dir + archNameNoExt + " " + cur_dir)
        return True
    except:
        return False

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
