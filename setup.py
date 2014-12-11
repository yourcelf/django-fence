import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-fence',
    version = '0.0.3',
    packages = ['fence',],
    include_package_data=True,
    license = 'MIT',
    author = 'Charlie DeTar',
    author_email = 'cfd@fohn.org',
    description = 'Simple middleware to restrict access to "private beta" sites',
    long_description = README,
    url = 'http://github.com/yourcelf/django-fence',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
