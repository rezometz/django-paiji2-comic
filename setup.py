import os
import sys
from setuptools import setup, find_packages
from django.core import management

with open(os.path.join(os.path.dirname(__file__), 'README.markdown')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# compile django.po files (translations)
# curdir = os.getcwd()
# os.chdir('paiji2_comic')
# management.call_command('compilemessages', stdout=sys.stdout)
# os.chdir(curdir)

setup(
    name='django-paiji2-comic',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Show comic extracts',
    long_description=README,
    url='https://github.com/rezometz/django-paiji2-comic',
    author='Supelec Rezo Metz',
    author_email='paiji-dev@rezometz.org',
    license='Affero GPL v3+',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django-modular-blocks',
        'feedparser>=5',
    ]
)
