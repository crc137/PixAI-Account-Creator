#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core import config as cfg

GREEN = cfg.GREEN
RED = cfg.RED
BLUE = cfg.BLUE
YELLOW = cfg.YELLOW
CYAN = cfg.CYAN
NC = cfg.NC
cprint = cfg.cprint
cprint_auto = cfg.cprint_auto

__version__ = cfg.VERSION
__version_info__ = (cfg.VERSION_MAJOR, cfg.VERSION_MINOR, cfg.VERSION_PATCH)
__version_string__ = cfg.VERSION_STRING
__build_date__ = cfg.BUILD_DATE
__release_name__ = cfg.RELEASE_NAME

def get_version():
    return __version__

def get_version_info():
    return __version_info__

def get_version_string():
    return __version_string__

def get_build_info():
    return {
        "version": __version__,
        "version_string": __version_string__,
        "version_info": __version_info__,
        "build_date": __build_date__,
        "release_name": __release_name__
    }

if __name__ == "__main__":
    cprint_auto(f"[+] {cfg.TITLE} {cfg.VERSION_STRING}")
    cprint_auto(f"[+] Build Date: {cfg.BUILD_DATE}")
    cprint_auto(f"[+] Release: {cfg.RELEASE_NAME}")
