# Jupyter Launcher Shortcuts development

## Pre-build labextension

In order to rebuild Jupyterlab extension

```
micromamba create -n jupyterlab-ext --override-channels --strict-channel-priority -c conda-forge -c nodefaults jupyterlab=4 nodejs=18 git hatch jinja2-time
micromamba activate jupyterlab-ext
```

Prebuild Jupyterlab extension
```
jlpm build
```
