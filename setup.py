from setuptools import setup, find_packages

setup(
    name="interpret-clone",
    version="0.1.0",
    description="Un clon modificado de interpretml",
    author="Javier Pérez Vargas",
    author_email="javipv2003pv@gmail.com",
    url="https://github.com/bmihaljevic/tfg-interpretml",
    packages=find_packages(include=["interpret", "interpret.*"]),
    install_requires=[
        # dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
