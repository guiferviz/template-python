# Template: Python package

This is a [`cookiecutter`
template](https://cookiecutter.readthedocs.io/en/stable/) for quickly creating
a new Python package.


## Getting started

To use this template, you will need to have `cookiecutter` installed. Once you
have it, you can create a new Python package using this template by running the
following command:

```cmd
cookiecutter gh:guiferviz/template-python
```

Alternatively you can use `cruft` for creating your project. The advantage of
using `cruft` over `cookiecutter` is that you can update your generated project
if the template is also updated. To create the Python project files for the
first time you can use:

```cmd
cruft create https://github.com/guiferviz/template-python/
```

Once you have a new version of your template you can update your existing
projects with:

```cmd
cruft update
```

See [the cruft docs](https://cruft.github.io/cruft/) for more info.


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
