"""Setup file, used for building a Python package."""
from setuptools import setup

with open("README.md", "r") as desc_file:
    long_description = desc_file.read()

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="modern-bencode",
    version="1.0.0",
    packages=["bencode"],
    python_requires='>=3.7',
)