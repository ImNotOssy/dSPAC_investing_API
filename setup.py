from setuptools import setup, find_packages

setup(
    name="dspac_invest_api",
    version="0.1.1",
    description="Unofficial dSPAC Invest API written in Python Requests",
    url="https://github.com/ImNotOssy/dSPAC_investing_API",
    author="Oswaldo Romero",
    packages=["dspac_invest_api"],
    install_requires=[
        "pillow",
        "python-dotenv",
        "requests",
    ],
)
