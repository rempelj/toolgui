from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toolgui",
    version="0.0.2",
    description="toolgui",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rempelj/toolgui",
    classifiers=["Development Status :: 1 - Planning"],
    install_requires=[
        "imgui[glfw]",
    ],
    extras_require={
        "dev": [
            "twine",
            "wheel",
        ],
    },
)
