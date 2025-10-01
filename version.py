#!/usr/bin/env python3
"""
PixAI Account Creator - Version Script
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.version import get_version, get_build_info

if __name__ == "__main__":
    build_info = get_build_info()
    print(f"PixAI Account Creator {build_info['version_string']}")
    print(f"Build Date: {build_info['build_date']}")
    print(f"Release: {build_info['release_name']}")
