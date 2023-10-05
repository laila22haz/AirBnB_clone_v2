#!/usr/bin/python3
"""Deploy archive"""

from fabric.api import *
from fabric.contrib import files
import os

env.hosts = ['ubuntu@54.226.32.212', '52.201.179.163']


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers"""
    if not files.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        archive_ext = os.path.splitext(archive_name)[0]
        new_folder = '/data/web_static/\
            releases/'.format(archive_ext)
        put(archive_name, '/temp')
        run('tar -xzf /tmp/{} -C /data/web_static\
        /releases/{}'.format(archive_name, archive_ext))
        run('rm -rf /temp/{}'.format(archive_name))
        run('rm -rf {}'.format('/data/web_static/current'))
        run('ln -s /data/web_static/releases\
            /{}/' '/data/web_static/current\
                '.format(archive_ext))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
