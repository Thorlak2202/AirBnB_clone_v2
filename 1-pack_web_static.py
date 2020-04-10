#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')
        curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
        outpt = local('tar -czvf versions/web_static_{}.tgz web_static'.
                      format(curr_time))
        return outpt
    except:
        return None
