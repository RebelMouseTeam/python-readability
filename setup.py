#!/usr/bin/env python
import os
from distribute_setup import use_setuptools; use_setuptools()
from setuptools import setup, find_packages

rel_file = lambda *args: os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)
cleanup = lambda lines: filter(None, map(lambda s: s.strip(), lines))

def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()

def get_requirements():
    return cleanup(read_from(rel_file('REQUIREMENTS')).splitlines())

setup(
    name="readability-lxml",
    version="0.2.6.2",
    author="Roberto Alamos",
    author_email="roberto@rebelmouse.com",
    description="modification of buriy's readability tool",
    test_suite = "tests.test_article_only",
    long_description= "Given a html, it pulls out the main body text",
    license="Apache License 2.0",
    url="http://github.com/ralamosm/python-readability",
    packages=find_packages(),
    install_requires = get_requirements(),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ]
)
