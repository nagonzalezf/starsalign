import os
from setuptools import setup, find_packages

PATH = os.path.abspath(os.path.dirname(__file__))

STARSALIGN_PATH = os.path.join(PATH, "starsalign/starsalign.py")

with open(STARSALIGN_PATH, "r") as f:
    for line in f:
        if line.startswith("__version__"):
            _, _, AA_VERSION = line.replace('"', "").split()
            break

setup(
    name="starsalign",
    version=AA_VERSION,
    packages=find_packages(),

    author="Nicolas Antonio Gonzalez Figueroa",
    author_email="nagonzalezf@ing.ucsc.cl",
    description="A package for aligning and diffing astronomical images",
    keywords="astronomical image alignment difference",
    url="https://github.com/nagonzalezf/starsalign",
    project_urls={
        "Bug Tracker": "https://github.com/nagonzalezf/starsalign/issues",
        "Documentation": "https://github.com/nagonzalezf/starsalign/docs",
        "Source Code": "https://github.com/nagonzalezf/starsalign",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10.8",
    ],
    install_requires=[
        "numpy",
        "opencv-python==4.7.0"
    ],
)