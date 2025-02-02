from setuptools import setup, find_packages

with open("requirements.txt") as req:
    requirements = req.read().splitlines()

setup(
    name="pec4",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
)