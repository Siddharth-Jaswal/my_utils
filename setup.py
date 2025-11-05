
from setuptools import setup, find_packages

setup(
    name="my_utils",                # package name
    version="1.0.0",                # version
    author="Siddharth Jaswal",
    description="A collection of utility",
    packages=find_packages(),       # automatically include all subpackages
    install_requires=[],            # add dependencies here if any
    python_requires=">=3.7",
)
