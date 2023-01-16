import os
from setuptools import setup, find_packages

PATH = os.path.abspath(os.path.dirname(__file__))

STARSALIGN_PATH = os.path.join(PATH, "starsalign/__init__.py")

with open(STARSALIGN_PATH, "r") as f:
    for line in f:
        if line.startswith("__version__"):
            _, _, VERSION = line.replace('"', "").split()
            break

setup(
    name="starsalign",
    version=VERSION,
    packages=find_packages(),

    author="Nicolas Antonio Gonzalez Figueroa",
    author_email="nagonzalezf@ing.ucsc.cl",
    description="A package for aligning and comparing astronomical images",
    keywords="alignment astronomical astro astronomy comparing difference image stars",
    url="https://github.com/nagonzalezf/starsalign",
    project_urls={
        "Source Code": "https://github.com/nagonzalezf/starsalign/starsalign",
        "Bug Tracker": "https://github.com/nagonzalezf/starsalign/issues",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Image Processing",
        
    ],
    install_requires=[
        "numpy",
        "opencv"
    ],
)
