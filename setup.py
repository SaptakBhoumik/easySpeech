from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="easySpeech",
    version="0.0.1",
    description="A python wrapper for google speech to text api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SaptakBhoumik/easySpeech",
    author="Saptak Bhoumik",
    author_email="saptakbhoumik@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["easySpeech"],
    include_package_data=True,
    install_requires=["numpy","sounddevice","librosa","transformers"]
)