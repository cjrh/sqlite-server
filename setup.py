# Always prefer setuptools over distutils
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

extras_require = {"dev": ["check-manifest", "wheel"], "test": ["pytest", "pytest-cov"]}
extras_require["all"] = list({d for k, deps in extras_require.items() for d in deps})

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
    extras_require=extras_require,
    keywords="sqlite",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["aiosqlite", "aiohttp", "cchardet", "aiodns", "pyzmq", "biodome"],
    entry_points={"console_scripts": ["sqlite_server=sqlite_server:main"]},
)
