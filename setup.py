#!/usr/bin/env python3
"""
Setup script for byonoy-luminescence-reader
"""

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="byonoy-luminescence-reader",
        version="0.1.0",
        description="MCP server for Byonoy Luminescence Reader",
        author="Luis Villa",
        author_email="luis.villa@example.com",
        packages=find_packages(),
        install_requires=[
            "byonoy_devices",
            "mcp[cli]>=1.0.0",
        ],
        extras_require={
            "dev": [
                "pytest>=7.0.0",
                "black>=23.0.0",
                "flake8>=6.0.0",
                "mypy>=1.0.0",
            ],
        },
        entry_points={
            "console_scripts": [
                "byonoy-mcp=byonoy_luminescence_reader.server:main",
            ],
        },
        python_requires=">=3.10",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Topic :: Scientific/Engineering",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    ) 