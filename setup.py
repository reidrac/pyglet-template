#!/usr/bin/env python
from setuptools import setup
from game.const import APP_NAME, VERSION, PROJECT_DESC, PROJECT_URL

def readme():
    try:
        return open('README.txt').read()
    except:
        return ""

setup(name=APP_NAME,
      version=VERSION,
      description=PROJECT_DESC,
      long_description=readme(),
      author='YOUR NAME',
      author_email='YOUR MAIL',
      url=PROJECT_URL,
      license='LICENSE',
      install_requires=['pyglet>=1.2.0'],
      include_package_data=True,
      zip_safe=False,
      scripts=['game.py'],
      packages=['game',],
      classifiers = [
        #'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        #'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment',
        'Intended Audience :: End Users/Desktop',
        ],
      )

