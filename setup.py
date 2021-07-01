import os
import sys
from distutils.core import setup
from setuptools import find_packages

PROJECT = "ecashaddress"

def get_readme():
    """Returns content of README.rst file"""
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, "README.rst")
    with open(filename, "r", encoding="utf-8") as fp:
        long_description = fp.read()
    return long_description


def get_version():
    """Returns current version number from _version.py file"""
    dirname = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), PROJECT)
    sys.path.insert(0, dirname)
    import _version
    sys.path = sys.path[1:]
    return _version.version


setup(name=PROJECT,
      version=get_version(),
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'ecashconvert=ecashaddress.__main__:convert',
              'ecashaddress=ecashaddress.__main__:main'
          ]

      },
      description='Python library and command line tool for converting cashaddr',
      url='https://github.com/PiRK/ecashaddress/',
      python_requires='>=3.7',
      keywords=['ecash', 'bcha', 'bitcoincash', 'bch', 'address', 'cashaddress', 'legacy', 'convert'],
      classifiers=[
          'Programming Language :: Python :: 3',
      ],
    long_description=get_readme()
)
