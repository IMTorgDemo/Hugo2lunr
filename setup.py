# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="hugo2lunr",
    packages=['hugo2lunr'],
    version="0.1.0",
    description="Sample package for Python-Guide.org",
    long_description=readme,
    author="Jason Beach",
    author_email="information@mgmt-tech.org",
    url="",
    license=license,
    package_data={'': ['data/word_assocation_ref.json']},
    scripts=['bin/hugo2lunr'],
    include_package_data=True,
    zip_safe=False
)
