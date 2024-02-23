"""
Traitlets based configuration for jupyter_server_proxy
"""
from jupyter_server.utils import url_path_join as ujoin
from .handlers import SuperviseAndProxyHandler, AddSlashHandler
import pkg_resources
from collections import namedtuple

