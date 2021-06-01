import os
import stat

from setuptools import setup
from setuptools.command.install import install
from distutils import log


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

FILES_TO_MARK_EXECUTABLE = ["./easySpeech/flac-linux-x86", "./easySpeech/flac-linux-x86_64", "./easySpeech/flac-mac", "./easySpeech/flac-win32.exe"]


class InstallWithExtraSteps(install):
    def run(self):
        install.run(self)  # do the original install steps

        # mark the FLAC executables as executable by all users (this fixes occasional issues when file permissions get messed up)
        for output_path in self.get_outputs():
            if os.path.basename(output_path) in FILES_TO_MARK_EXECUTABLE:
                log.info("setting executable permissions on {}".format(output_path))
                stat_info = os.stat(output_path)
                os.chmod(
                    output_path,
                    stat_info.st_mode |
                    stat.S_IRUSR | stat.S_IXUSR |  # owner can read/execute
                    stat.S_IRGRP | stat.S_IXGRP |  # group can read/execute
                    stat.S_IROTH | stat.S_IXOTH  # everyone else can read/execute
                )

# This call to setup() does all the work
setup(
    name="easySpeech",
    version="1.0.1",
    cmdclass={"install": InstallWithExtraSteps},
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