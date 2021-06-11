#!/usr/bin/python3
""" A module that connects web server to python backend """


from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['3.84.179.220', '54.226.50.222']

def deploy():
    archive = do_pack()
    if not archive:
        return False

    status = do_deploy(archive)

    return status


def do_deploy(archive_path):
    """ Deploy an archive """

    if not os.path.exists(archive_path):
            return False
    try:
        archiveName = archive_path[9:]
        archNameNoExt = archiveName[:-4]

        put(arhive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archNameNoExt)
        run("tar -xzvf /tmp/" + archiveName + " -C " +
            "/data/web_static/releases/" + archNameNoExt +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archNameNoExt + "/data/web_static/current")
        return True
    except:
        return False


def do_pack():
    """ Pack up our web_static """

    try:
        now = datetime.now()

        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")
        local("tar -czvf " + tarArchivePath + " web_static")

        return tarArchivePath
    except:
        return None
