import {{ cookiecutter.module_name }}


class CLI:
    def __init__(self, version: bool = False):
        if version:
            self._greet()
            raise SystemExit()

    def _greet(self):
        print({{ cookiecutter.module_name }}.__version__)

    def hi(self, name: str = "{{ cookiecutter.full_name }}"):
        """Say hello.

        Args:
            name (str): Your name.
        """
        print(f"Hi {name}")

    def bye(self, name: str = "{{ cookiecutter.full_name }}"):
        """Say good bye.

        Args:
            name (str): Your name.
        """
        print(f"Bye {name}")
