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
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove("LICENSE")

    remove("_licenses/")


if __name__ == "__main__":
    main()
