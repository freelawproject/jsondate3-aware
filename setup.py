import codecs
import os

import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setuptools.setup(
    name="jsondate3-aware",
    version="0.2.1",
    url="https://github.com/freelawproject/jsondate3-aware",
    license="BSD",
    author="Rick Harris, Maciej nitZ Krol, Free Law Project",
    author_email="rconradharris@gmail.com, nitz@o2.pl, info@free.law",
    description="JSON with tz-aware datetime support",
    long_description=read("README.rst"),
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["six", "iso8601"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
