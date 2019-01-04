import setuptools
from glob import glob

setuptools.setup(
    name="jupyter-launcher-shortcuts",
    version='1.0dev',
    url="https://github.com/yuvipanda/jupyter-launcher-shortcuts",
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    license="BSD 3-Clause",
    description="Easily place shortcuts",
    packages=setuptools.find_packages(),
    install_requires=['notebook', 'simpervisor', 'aiohttp'],
    python_requires='>=3.5',
    classifiers=[
        'Framework :: Jupyter',
    ],
    data_files=[
        ('share/jupyter/nbextensions/jupyter_launcher_shortcuts', glob('jupyter_launcher_shortcuts/static/*')),
        ('etc/jupyter/jupyter_notebook_config.d', ['jupyter_launcher_shortcuts/etc/serverextension.json']),
        ('etc/jupyter/nbconfig/tree.d', ['jupyter_launcher_shortcuts/etc/nbextension.json'])
    ],
    include_package_data=True,
    zip_safe=False
)
