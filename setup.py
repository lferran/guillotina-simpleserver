# -*- coding: utf-8 -*-
from os import path

from setuptools import find_packages, setup


def get_requirements(rfile):
    with open(rfile, "r") as f:
        requirements = []
        for line in f.readlines():
            if len(line) == 0 or line[0] == "#" or "://" in line:
                continue
            requirements.append(line.strip())
    return requirements


setup(
    name="guillotina-simpleserver",
    version="1.0.0",
    description="Really simple server on top of guillotina",
    long_description=" ",
    keywords=[],
    author="Ferran Llamas",
    author_email="llamas.arroniz@gmail.com",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="http://github.com/lferran/guillotina-simpleserver.git",
    license="BSD",
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    extras_require={
        "test": get_requirements("test-requirements.txt"),
        "dev": get_requirements("dev-requirements.txt")
    },
)
