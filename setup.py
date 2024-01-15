import os
import pathlib
import pkg_resources
from setuptools import setup, find_packages


PKG_NAME = "CraftyAI"
VERSION = "1.0.0"
EXTRAS = {}


def _read_file(fname):
    with pathlib.Path(fname).open(encoding="utf-8") as fp:
        return fp.read()


def _read_install_requires():
    with pathlib.Path("requirements.txt").open() as fp:
        return [
            str(requirement) for requirement in pkg_resources.parse_requirements(fp)
        ]


def _fill_extras(extras):
    if extras:
        extras["all"] = list(set([item for group in extras.values() for item in group]))
    return extras


setup(
    name=PKG_NAME,
    version=VERSION,
    author=f"TheUnrealZaka",
    author_email="info@theunrealzaka.me",
    url="https://github.com/TheUnrealZaka/CraftyAI",
    description="CraftyAI is an intelligent agent for Minecraft with LLM (Large Language Models).",
    long_description_content_type="text/markdown",
    keywords=[
        "Minecraft",
        "AI",
        "Intelligent Agent",
        "CraftyAI",
        "Large Language Models",
        "Crafty",
        "Embodied Agents",
    ],
    packages=find_packages(include=f"{PKG_NAME}.*"),
    include_package_data=True,
    zip_safe=False,
    install_requires=_read_install_requires(),
    extras_require=_fill_extras(EXTRAS),
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Engineering :: Artificial Intelligence",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
    ],
)