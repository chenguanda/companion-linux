# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name="companion-linux",
    version="0.0.1",
    description="Confluence Companion App for Linux",
    author="",
    author_email="",
    url="https://github.com/schorschii/companion-linux",
    packages=['companion_linux'],
    install_requires=[
        "websockets",
        "requests",
        "pyinotify",
    ],
    entry_points={
        "console_scripts": [
            "companion = companion_linux.companion:main"
        ]
    }
)


