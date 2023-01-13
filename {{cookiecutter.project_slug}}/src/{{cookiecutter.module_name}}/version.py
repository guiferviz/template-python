import importlib.metadata

try:
    __version__ = importlib.metadata.version("{{ cookiecutter.module_name }}")
except ImportError:
    # When we run Python scripts from inside the package without installing it
    # an ImportError is raised. For example, running
    # `python src/{{ cookiecutter.module_name }}/__main__.py` in an environment
    # without the package installed causes this error.
    __version__ = "UnknownVersion"
