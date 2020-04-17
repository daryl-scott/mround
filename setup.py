"""build script for setuptools"""
from __future__ import absolute_import
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mround",
    version="1.0",
    author="Daryl Scott",
    author_email="daryl_scott@live.com",
    description="Rounding functions compatible with Python 2 and 3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daryl-scott/mround",
    packages=["mround"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4"
)
