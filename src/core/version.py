#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core import config as cfg

GREEN = getattr(cfg, "GREEN", '\033[0;32m')
RED = getattr(cfg, "RED", '\033[0;31m')
BLUE = getattr(cfg, "BLUE", '\033[0;34m')
YELLOW = getattr(cfg, "YELLOW", '\033[0;33m')
CYAN = getattr(cfg, "CYAN", '\033[0;36m')
NC = getattr(cfg, "NC", '\033[0m')

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
    print(f"{GREEN}[+] {cfg.TITLE} {cfg.VERSION_STRING}{NC}")
    print(f"{GREEN}[+] Build Date: {cfg.BUILD_DATE}{NC}")
    print(f"{GREEN}[+] Release: {cfg.RELEASE_NAME}{NC}")
