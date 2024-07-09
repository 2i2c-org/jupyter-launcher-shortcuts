================================================
Jupyter Launcher Shortcuts development & release
================================================

Pre-build labextension
======================

In order to rebuild Jupyterlab extension

```
micromamba create -n jupyterlab-ext --override-channels --strict-channel-priority -c conda-forge -c nodefaults jupyterlab=4 nodejs=18 git hatch jinja2-time
micromamba activate jupyterlab-ext
```

Prebuild Jupyterlab extension
```
jlpm build
```

Create dist packages
====================

```
hatch build
```


Increase minor version
======================

```
hatch minor version
hatch build
```