from distutils.core import setup

setup(
    name = 'django-fence',
    version = '0.0.1',
    packages = ['fence',],
    platforms = ['any'],
    license = 'MIT',
    author = 'Charlie DeTar',
    author_email = 'cfd@media.mit.edu',
    description = 'Simple middleware to restrict access to "beta only" sites',
    long_description = open('README.rst').read(),
    url = 'http://github.com/yourcelf/django-authproxy',
)
