# Always prefer setuptools over distutils
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="sqlite_server",
    version=open("VERSION").read().strip(),
    description="Server for sqlite",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/cjrh/sqlite-server",
    author="Caleb Hattingh",
    author_email="caleb.hattingh@gmail.com",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="sqlite",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["aiosqlite", "aiohttp"],
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ["pytest", "pytest-cov"],
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={"console_scripts": ["sqlite_server=sqlite_server:main"]},  # Optional
)
