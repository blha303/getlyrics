from setuptools import setup

with open("README.rst", "rb") as f:
    long_descr = f.read().decode('utf-8')

setup(
    name = "getlyrics",
    packages = ["getlyrics"],
    install_requires = ["beautifulsoup4"],
    entry_points = {
        "console_scripts": ['getlyrics = getlyrics.getlyrics:main']
        },
    version = "1.0.0",
    description = "A Python program which gets the lyrics for a song and outputs them to stdout",
    long_description = long_descr,
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    url = "https://blha303.github.io/getlyrics/",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Multimedia :: Sound/Audio"
        ]
    )
