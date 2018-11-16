from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pySearch",
    version="1.0",
    author="jrkong",
    author_email="jrkong.hfd@gmail.com",
    description="cli tool for executing browser searches",
    license='BSD',
    url="https://github.com/jrkong/pySearch",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pySearch = pySearch:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ],
    include_package_data=True,
)