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

GREEN = getattr(cfg, "GREEN", '\033[0;32m')
RED = getattr(cfg, "RED", '\033[0;31m')
BLUE = getattr(cfg, "BLUE", '\033[0;34m')
YELLOW = getattr(cfg, "YELLOW", '\033[0;33m')
CYAN = getattr(cfg, "CYAN", '\033[0;36m')
NC = getattr(cfg, "NC", '\033[0m')

def parse_args():
    parser = argparse.ArgumentParser(description="Preview browser with UI enhancements")
    parser.add_argument("--headless", type=str, default="false", help="Run in headless mode (true/false)")
    parser.add_argument("--url", type=str, default="https://pixai.art/", help="URL to open")
    return parser.parse_args()

async def preview_browser():
    args = parse_args()
    headless = str(args.headless).strip().lower() in ("1", "true", "yes", "on")
    
    version = get_version()
    print(f"{GREEN}[+] {cfg.TITLE} {version}{NC}")
    print(f"{GREEN}[+] Starting browser preview...{NC}")
    print(f"{GREEN}[+] URL: {args.url}{NC}")
    print(f"{GREEN}[+] Headless: {headless}{NC}")
    print(f"{GREEN}[+] Press Ctrl+C to close{NC}")
    
    async with async_playwright() as pw:
        # Launch browser
        browser = await pw.chromium.launch(
            headless=headless,
            args=cfg.BROWSER_ARGS
        )
        
        # Create context and page
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            # Navigate to URL
            print(f"{GREEN}[+] Navigating to {args.url}...{NC}")
            await page.goto(args.url, timeout=30000)
            
            # Apply UI enhancements
            print(f"{GREEN}[+] Applying UI enhancements...{NC}")
            await ui_enhancer.enhance_page(page)
            
            print(f"{GREEN}[+] Browser ready! You can now see the enhanced interface.{NC}")
            print(f"{GREEN}[+] Press Ctrl+C to close the browser.{NC}")
            
            # Keep browser open until user closes it
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{GREEN}[+] Closing browser...{NC}")
                
        except Exception as e:
            print(f"{RED}[-] Error: {e}{NC}")
        finally:
            await context.close()
            await browser.close()
            print(f"{GREEN}[+] Browser closed.{NC}")

if __name__ == "__main__":
    try:
        asyncio.run(preview_browser())
    except KeyboardInterrupt:
        print(f"\n{GREEN}[+] Exiting...{NC}")
    except Exception as e:
        print(f"{RED}[-] Fatal error: {e}{NC}")
