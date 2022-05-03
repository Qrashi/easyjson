import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="easyjson",
    version="0.0.1",
    author="Qrashi",
    author_email="fritz@vibe.ac",
    packages=["easyjson"],
    description="A simple package providing easy to use JSON utilities",
    long_description=long_description,
    url="https://github.com/Qrashi/easyjson",
    license="GPL3",
    install_requires=[]
)