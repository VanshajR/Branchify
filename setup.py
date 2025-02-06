from setuptools import setup, find_packages
from pathlib import Path
here = Path(__file__).parent
long_description = (here / "DOCUMENTATION.md").read_text(encoding="utf-8")
setup(
    name="branchify",
    version="1.0.1",
    description="Generate an ASCII folder structure of a directory",
    long_description=long_description,
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
    python_requires=">=3.8",
)
