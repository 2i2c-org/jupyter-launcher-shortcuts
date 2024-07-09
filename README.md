# Jupyter Launcher Shortcuts

Extension for JupyterLab (version 4+) and classic Jupyter Notebook (version 7+,
currently broken, see `Issue #25<https://github.com/2i2c-org/jupyter-launcher-shortcuts/issues/25>`_)
to add **user defined** 'launcher' shortcuts. Primarily useful in JupyterHub /
Binder situations.

For JupyterLab, they're added in the launcher interface.

![](labextension.png)

For classic Jupyter Notebook, they are added under the 'New' button

![](nbextension.png)

## Installation

The JupyterLab extension, the classic Jupyter Notebook extension, and a Jupyter
Server extension required behind the scenes can all be installed with ``pip``.

```bash
pip install jupyter-launcher-shortcuts
```

## Configuring

The extension can be configured in a ``jupyter_server_config.py``
file created in any of the directories under ``config`` in the 
output of ``jupyter --paths`` command.

```python
c.LauncherShortcuts.shortcuts = {
    'my-shiny-application': {
        'title': 'Human Readable Shortcut Title',
        'target': '{base_url}shiny/my-shiny-application-directory/',
        'icon_path': '/path/to/svg/file'
    }
}
```
