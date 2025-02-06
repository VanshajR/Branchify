from setuptools import setup, find_packages

setup(
    name="branchify",
    version="1.0.1",
    description="Generate an ASCII folder structure of a directory",
    long_description=open("DOCUMENTATION.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Vanshaj Raghuvanshi",
    author_email="vanshajraghuvanshi@gmail.com",
    url="https://github.com/VanshajR/branchify",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "branchify = branchify.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
)
