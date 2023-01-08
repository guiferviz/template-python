import os
import shutil
import pathlib


PROJECT_DIRECTORY = pathlib.Path(".").absolute()


def remove(path):
    full_path = PROJECT_DIRECTORY / path

    if full_path.is_dir():
        shutil.rmtree(full_path)
    else:
        full_path.unlink()


def main():
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove("AUTHORS.rst")
        remove("docs/authors.rst")

    if "{{ cookiecutter.create_docs }}" != "y":
        remove("docs")

    if "none" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.module_name }}", "cli.py")
        remove(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove("LICENSE")

    remove("_licenses/")


if __name__ == "__main__":
    main()
