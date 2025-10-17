#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图地点查询应用安装脚本
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="amap-location-query",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="基于高德地图API的智能地点查询应用",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/amap-location-query",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "amap-query=main:main",
        ],
    },
    keywords="amap, location, search, nlp, chinese, map, poi",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/amap-location-query/issues",
        "Source": "https://github.com/yourusername/amap-location-query",
        "Documentation": "https://github.com/yourusername/amap-location-query#readme",
    },
)
