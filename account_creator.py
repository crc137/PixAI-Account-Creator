#!/usr/bin/env python3
"""
PixAI Account Creator - Main Script
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.scripts.account_creator import main

if __name__ == "__main__":
    main()
