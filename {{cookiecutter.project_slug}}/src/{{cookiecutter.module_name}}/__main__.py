import fire

from {{ cookiecutter.module_name }}.cli import CLI


def main():
    fire.Fire(CLI)


if __name__ == "__main__":
    main()
