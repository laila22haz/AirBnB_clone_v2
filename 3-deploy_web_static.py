#!/usr/bin/python3
"""Script that creates and distributes an archive
to your web servers"""
from fabric.api import *
from datetime import datetime
from os.path import exists, splitext, basename

env.hosts = ['100.26.9.167', '52.201.179.163']


@task
def do_pack():
    """return the archive path if
    the archive has been correctly
    generated"""

    date_time = datetime.now()
    date = date_time.strftime('%Y%m%d%hM%S')
    file_name = "web_static_{}.tgz".format(date)
    mkdir = "mkdir -p versions"
    archive_path = "versions/{}".format(file_name)
    print("Packing web_static to {}".format(archive_path))
    if local("{} && tar -cvzf {} web_static"
             .format(mkdir, archive_path)).succeeded:
        return archive_path
        print("web_static packed: {} -> {}Bytes".format(path, size))
    return None


@task
def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_name = basename(archive_path)
        archive_ext = splitext(archive_name)[0]
        tmp_path = "/tmp/{}".format(archive_name)
        data_path = "/data/web_static/releases/{}".format(archive_ext)
        # Fabric commands
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(data_path))
        run('tar -xzf {}  -C {}'.format(tmp_path, data_path))
        run('rm {}'.format(tmp_path))
        run('mv {}/web_static/* {}/'.format(data_path, data_path))
        run('rm -rf {}/web_static'.format(data_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(data_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


@task
def deploy():
    """Function that creates and distributes an archive
    to your web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
