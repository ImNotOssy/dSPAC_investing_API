from setuptools import setup, find_packages

setup(
    name="dspac_investing_API",
    version="0.1.0",
    packages=["dspac_api"],
    install_requires=[
        "pillow",
        "python-dotenv",
        "requests",
    ],
)
