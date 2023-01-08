# Template: Python package

This is a `cookiecutter` template for quickly creating a new Python package.


## Getting started

To use this template, you will need to have `cookiecutter` installed. Once you
have it, you can create a new Python package using this template by running the
following command:

```cmd
cookiecutter 
```

## Features

The generated template comes with the following features:

* The template uses `poetry` for managing dependencies, creating virtual
environments, packaging, and publishing to PyPI.
* Testing is setup with `pytest`.
* Documentation is generated using `mkdocs`.
* The template includes GitHub Actions for:
    * Automatically releasing new versions to PyPI when you push a new tag to
    the master branch.
    * Deploying documentation to GitHub Pages.
