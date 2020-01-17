Julie's Python Template

This is a cookiecutter template for a typical Python library following modern packaging conventions. It utilizes popular libraries alongside Make and Graphviz to fully automate all development and deployment tasks. Check out the live demo: jacebrowning/template-python-demo

Build Status

Features

Preconfigured setup for Travis CI, Coveralls, and Scrutinizer
pyproject.toml for managing dependencies and package metadata
Makefile for automating common development tasks:
Installing dependencies with poetry
Automatic formatting with isort and black
Static analysis with pylint
Type checking with mypy
Docstring styling with pydocstyle
Running tests with pytest
Building documentation with mkdocs
Publishing to PyPI using poetry
If you are instead looking for a Python application template, check out one of the sibling projects:

jacebrowning/template-django
jacebrowning/template-flask
Examples

Here are a few sample projects based on this template:

jacebrowning/minilog
theovoss/Chess
sprout42/StarStruct
MichiganLabs/flask-gcm
flask-restful/flask-restful
Usage

Install cookiecutter and generate a project:

$ pip install cookiecutter
$ cookiecutter gh:jacebrowning/template-python -f
Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

If you still need to use legacy Python or nose as the test runner, older versions of this template are available on branches:

$ cookiecutter gh:jacebrowning/template-python -f --checkout=python2

$ cookiecutter gh:jacebrowning/template-python -f --checkout=nose
Updates

Checkout the appropriate branch of template-python-demo and manually merge changes into your project.