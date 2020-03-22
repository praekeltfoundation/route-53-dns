import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name="route53",
    version="0.0.1.dev0",
    license="MIT",
    description="Package for Managing Route53 Records",
    author="Praekelt.org SRE team",
    author_email="sre@praekelt.org",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "route53=route53.cli:main",
        ],
    },
    python_requires=">=3.7",
    install_requires=[
        "python-route53",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "hypothesis",
            "isort",
            "mypy",
            "pep517",
            "pytest>=5.0.1",
            "pytest-cov",
            "pytest-trio",
            "trio-typing",
        ]
    },
    classifiers=[
        "Private :: Do Not Upload",
    ],
)
