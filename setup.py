#!/usr/bin/env python

from setuptools import setup
import os

dir = os.path.dirname(__file__)
path_to_main_file = os.path.join(dir, "zfsapi/__init__.py")
path_to_readme = os.path.join(dir, "README.md")
for line in open(path_to_main_file):
	if line.startswith('__version__'):
		version = line.split()[-1].strip("'").strip('"')
		break
else:
	raise ValueError, '"__version__" not found in "zfsapi/__init__.py"'
readme = open(path_to_readme).read(-1)

classifiers = [
]

setup(
    name='zfsapi',
    version=version,
    description='ZFS API for Python',
    long_description = readme,
    author='Sean Johnson',
    author_email='pirogoeth@maio.me',
    license="GPL",
    url='http://github.com/pirogoeth/zfsapi',
    package_dir=dict([
              ("zfsapi", "zfsapi"),
    ]),
    classifiers = [
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2 :: Only',
            'Programming Language :: Python :: 2.7',
            'Topic :: System :: Filesystems',
            'Topic :: Utilities',
    ],
    packages=["zfsapi"],
    keywords="ZFS filesystems API",
    zip_safe=False,
)
