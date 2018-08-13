import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_params = dict(
    name="example_pkg",
    version="0.0.1",
    author="Nullbyte",
    author_email="me@nullbyte.be",
    description="A dynamic inventory builder for ansible",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lion24/flask-dynamic-inventory",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

setuptools.setup(**setup_params)
