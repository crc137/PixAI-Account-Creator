#!/usr/bin/env python3
"""
PixAI Account Creator - Browser Preview Script
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.scripts.preview_browser import preview_browser
import asyncio

if __name__ == "__main__":
    try:
        asyncio.run(preview_browser())
    except KeyboardInterrupt:
        print(f"\n[+] Exiting...")
    except Exception as e:
        print(f"[-] Fatal error: {e}")
