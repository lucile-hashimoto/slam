#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages

BASE_REQUIREMENTS = ["numpy", "scipy", "trimesh", "nibabel>=2.1", "networkx"]
TEST_REQUIREMENTS = ["flake8", "autopep8", "pytest", "pytest-cov", "coveralls"]
DIST = ["tvb-gdist"]

# grab version
verstr = "unknown"
try:
    verstrline = open('slam/_version.py', "rt").read()
except EnvironmentError:
    pass  # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in yourpackage/_version.py")

setup(
    name="brain-slam",
    version=verstr,
    packages=find_packages(),
    author="Guillaume Auzias",
    description="Surface anaLysis And Modeling",
    url="https://github.com/brain-slam/slam",
    license="MIT",
    python_requires=">=3.6",  # enforce Python 3.6 as minimum
    install_requires=BASE_REQUIREMENTS,
    extras_require={
        "full": DIST,
        "dev": DIST + TEST_REQUIREMENTS,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],
)
