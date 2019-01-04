from notebook.utils import url_path_join as ujoin
from .api import ShortcutsHandler, IconHandler
from traitlets import Dict
from traitlets.config import Configurable
from collections import namedtuple

Shortcut = namedtuple('Shortcut', ['name', 'title', 'icon_path', 'target'])

class LauncherShortcuts(Configurable):
    shortcuts = Dict(
        {},
        help="""
        Dictionary of shortcuts to put in launchers.

        Key should be the name of the shortcut.

        Value should be a dictionary with the following keys:

          title
            Human readable title for the shortcut. Defaults to the name.

          target
            URL to open when shortcut is clicked. {base_url} is replaced with
            the notebook server's base_url

          icon_path
            Full path to an svg icon that could be used with a launcher. Currently only used by the
            JupyterLab launcher
        """,
        config=True
    )

def shortcut_from_dict(name, shortcut_dict):
    return Shortcut(
        name,
        title=shortcut_dict.get('title', name),
        icon_path=shortcut_dict.get('icon_path'),
        target=shortcut_dict['target']
    )

def load_jupyter_server_extension(nbapp):
    # Set up handlers picked up via config
    base_url = nbapp.web_app.settings['base_url']
    shortcuts = [
        shortcut_from_dict(k, v) 
        for k, v in LauncherShortcuts(parent=nbapp).shortcuts.items()
    ]

    icons = {}
    for ls in shortcuts:
        if ls.icon_path:
            icons[ls.name] = ls.icon_path

    nbapp.web_app.add_handlers('.*', [
        (ujoin(base_url, 'launcher-shortcuts/shortcuts'), ShortcutsHandler, {'shortcuts': shortcuts}),
        (ujoin(base_url, 'launcher-shortcuts/icon/(.*)'), IconHandler, {'icons': icons})
    ])


# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'jupyter_launcher_shortcuts',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "jupyter_launcher_shortcuts",
        'src': 'static',
        "require": "jupyter_launcher_shortcuts/tree"
    }]
