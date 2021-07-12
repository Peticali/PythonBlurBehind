
from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.rst").read_text()

setup(
    name="BlurWindow",
    version="1.0.7",
    description="Blur PySide, Tkinter, etc windows.",
    url="https://github.com/Peticali/PythonBlurBehind",
    author="Peticali",
    long_description_content_type="text/x-rst",
    long_description=README,   
    author_email="pedropalmeira68@gmail.com",
    license="MIT",
    packages=['BlurWindow']

)