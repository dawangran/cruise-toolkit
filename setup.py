#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path
from setuptools import setup, find_packages

ROOT = Path(__file__).resolve().parent

def read_text(fname: str, default=""):
    p = ROOT / fname
    if not p.exists():
        return default
    return p.read_text(encoding="utf-8")

# 长描述（用于 PyPI 页面）
long_description = read_text("README.md")

setup(
    name="cruise-toolkit",
    version="1.0.0", 
    description="Unified CLI wrapper for barcode/UMI & CR/UR tools",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Dawn",
    author_email="605547565@qq.com",
    url="https://github.com/dawangran/cruise-toolkit",
    license="MIT",

    # 源码布局：src/
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # 会发现 src/cruise_toolkit/*
    py_modules=["common_utils"],          # 顶层兼容模块，确保 import common_utils 可用

    include_package_data=True,            # 结合 MANIFEST.in 一起生效
    license_files=("LICENSE",),           # 确保 LICENSE 被包含

    # 入口命令（安装后获得 `cruise-toolkit` 可执行）
    entry_points={
        "console_scripts": [
            "cruise-toolkit=cruise_toolkit.cli:main",
        ]
    },

    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["single-cell", "UMI", "barcode", "cyclone", "RNA"],
    project_urls={
        "Homepage": "https://github.com/dawangran/cruise-toolkit",
    },
)
