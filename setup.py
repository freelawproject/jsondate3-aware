import setuptools


setuptools.setup(
    name="jsondate3",
    version="0.1.4",
    url="https://github.com/nitz14/jsondate",
    license="MIT",
    author="Rick Harris, Maciej nitZ Krol",
    author_email="rconradharris@gmail.com, nitz@o2.pl",
    description="JSON with datetime support",
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["six"],
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
