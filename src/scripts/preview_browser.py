#!/usr/bin/env python3

import asyncio
import argparse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from playwright.async_api import async_playwright
from src.ui.ui_enhancer import ui_enhancer
from src.core.version import get_version
from src.core import config as cfg

GREEN = cfg.GREEN
RED = cfg.RED
BLUE = cfg.BLUE
YELLOW = cfg.YELLOW
CYAN = cfg.CYAN
NC = cfg.NC
cprint = cfg.cprint
cprint_auto = cfg.cprint_auto

def parse_args():
    parser = argparse.ArgumentParser(description="Preview browser with UI enhancements")
    parser.add_argument("--headless", type=str, default="false", help="Run in headless mode (true/false)")
    parser.add_argument("--url", type=str, default="https://pixai.art/", help="URL to open")
    return parser.parse_args()

async def preview_browser():
    args = parse_args()
    headless = str(args.headless).strip().lower() in ("1", "true", "yes", "on")
    
    version = get_version()
    cprint_auto(f"[+] {cfg.TITLE} {version}")
    cprint_auto(f"[+] Starting browser preview...")
    cprint_auto(f"[+] URL: {args.url}")
    cprint_auto(f"[+] Headless: {headless}")
    cprint_auto(f"[+] Press Ctrl+C to close")
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=headless,
            args=cfg.BROWSER_ARGS
        )
        
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            cprint_auto(f"[+] Navigating to {args.url}...")
            await page.goto(args.url, timeout=30000)
            
            cprint_auto(f"[+] Applying UI enhancements...")
            await ui_enhancer.enhance_page(page)
            
            cprint_auto(f"[+] Browser ready! You can now see the enhanced interface.")
            cprint_auto(f"[+] Press Ctrl+C to close the browser.")
            
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                cprint_auto(f"\n[+] Closing browser...")
                
        except Exception as e:
            cprint_auto(f"[-] Error: {e}")
        finally:
            await context.close()
            await browser.close()
            cprint_auto(f"[+] Browser closed.")

if __name__ == "__main__":
    try:
        asyncio.run(preview_browser())
    except KeyboardInterrupt:
        print(f"\n{GREEN}[+] Exiting...{NC}")
    except Exception as e:
        print(f"{RED}[-] Fatal error: {e}{NC}")
