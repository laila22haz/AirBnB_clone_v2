#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""
from fabric.api import local
import datetime


def do_pack():
    """return the archive path if
    the archive has been correctly
    generated"""

    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y%m%d%hM%S')
    file_name = "web_static_{}.tgz".format(date)
    mkdir = "mkdir -p versions"
    archive_path = "versions/{}".format(file_name)
    print("Packing web_static to {}".format(archive_path))
    local("{}&& tar -cvzf {} web_static".format(mkdir, archive_path))
