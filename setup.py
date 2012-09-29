import os
from setuptools import setup

# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='picomongo',
      version='0.6',
      description='Ultimate MongoDB Object Document Mapper',
      author='Dailymotion IT Team',
      author_email='contact@dmcloud.net',
      packages=['picomongo'],
      install_requires=['pymongo'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Database',
      ],
      long_description=read('README.rst')
)
