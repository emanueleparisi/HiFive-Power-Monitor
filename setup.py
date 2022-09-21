import pathlib
import re

from setuptools import setup


def parse_package_version():
    package_init_path = pathlib.Path.cwd() / "hifivepm" / "__init__.py"
    version_pattern = r"__version__\s*=\s*\"([0-9\.]+)\""

    with package_init_path.open(mode='r') as fp:
        version = None
        for line in fp:
            line = line.strip()
            if line and version is None:
                match = re.search(
                    version_pattern,
                    line
                )
                if match is not None:
                    version = match.group(1)

    if version is None:
        raise RuntimeError(
            f"Cannot parse package version from {package_init_path}."
        )

    return version


setup(
    # Package description.
    name="hifivepm",
    version=parse_package_version(),
    description="Some utilities to read and analyze HiFive power measurements",
    packages=["hifivepm"],

    # Package requirements.
    install_requires=[
        "jupyter",
        "matplotlib",
        "nptdms",
        "pandas"
    ]
)
