#!/usr/bin/env python3

import os
import sys
import time
import random
import string
import asyncio
import argparse
import json
import csv
import requests
from typing import List, Dict, Optional, Tuple
from playwright.async_api import async_playwright
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core import config as cfg
from src.ui.ui_enhancer import ui_enhancer
from src.core.version import get_version

GREEN = cfg.GREEN
RED = cfg.RED
BLUE = cfg.BLUE
YELLOW = cfg.YELLOW
CYAN = cfg.CYAN
NC = cfg.NC
cprint = cfg.cprint
cprint_auto = cfg.cprint_auto

API_URL = getattr(cfg, "API_URL", "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add")
HEADLESS = getattr(cfg, "HEADLESS", True)
BROWSER_ARGS = list(getattr(cfg, "BROWSER_ARGS", ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]))
EMAIL_DOMAIN = getattr(cfg, "EMAIL_DOMAIN", "coonlink.com")
DEFAULT_PROXIES_FILE = getattr(cfg, "PROXIES_FILE", "")
URL_USERNAME = getattr(cfg, "URL_USERNAME", "crc137")
ACCOUNT_CREATION_DELAY = getattr(cfg, "ACCOUNT_CREATION_DELAY", 2.0)
FORM_FIELD_DELAY = getattr(cfg, "FORM_FIELD_DELAY", 300)
FORM_SUBMISSION_DELAY = getattr(cfg, "FORM_SUBMISSION_DELAY", 1000)
PAGE_LOAD_DELAY = getattr(cfg, "PAGE_LOAD_DELAY", 500)
RETRY_DELAY = getattr(cfg, "RETRY_DELAY", 5.0)
RATE_LIMIT_DELAY = getattr(cfg, "RATE_LIMIT_DELAY", 15.0)
MAX_RETRY_ATTEMPTS = getattr(cfg, "MAX_RETRY_ATTEMPTS", 3)

def get_env_bool(name: str, default: str = "false") -> bool:
    value = os.getenv(name, default).strip().lower()
    return value in ("1", "true", "yes", "on")

def send_account_to_api(email: str, password: str) -> bool:
    try:
        response = requests.post(API_URL, json={
            "email": email,
            "password": password
        }, timeout=30)
        
        if response.status_code == 200:
            print(f"[+] Account {email} sent to API successfully")
            return True
        else:
            print(f"[-] Failed to send {email} to API: {response.status_code}")
            return False
    except Exception as e:
        print(f"[-] Error sending {email} to API: {e}")
        return False

def generate_email(domain: str) -> str:
    local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{local}@{domain}"

def generate_password() -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=12))

async def create_account_once_async(pw, context, page, email: str, password: str) -> Tuple[bool, bool]:
    try:
        await page.goto("https://pixai.art/", timeout=60000)
        await ui_enhancer.enhance_page(page)
        
        max_attempts = MAX_RETRY_ATTEMPTS
        
        for attempt in range(max_attempts):
            cprint_auto(f"[+] Account creation attempt {attempt + 1}/{max_attempts}")
            
            try:
                try:
                    await page.get_by_role("button", name="Sign in").click()
                    await page.wait_for_timeout(FORM_FIELD_DELAY)
                except Exception as e:
                    cprint_auto(f"[-] Could not find Sign in button: {e}")
                    cprint_auto("[+] Refreshing page and trying again...")
                    await page.reload()
                    await page.wait_for_timeout(FORM_SUBMISSION_DELAY)
                    await page.get_by_role("button", name="Sign in").click()
                    await page.wait_for_timeout(FORM_FIELD_DELAY)

                try:
                    await page.get_by_role("button", name="Continue with Email", exact=False).click()
                except Exception:
                    if await page.locator("text=Continue with Email").count():
                        await page.locator("text=Continue with Email").click()
                    else:
                        cprint_auto("[-] Could not find 'Continue with Email' button — continue anyway")

                await page.wait_for_timeout(300)
                
                if await page.locator("text=Register").count():
                    await page.locator("text=Register").click()

                cprint_auto("[+] Filling email field for registration...")
                if await page.get_by_role("textbox", name="Email").count():
                    await page.get_by_role("textbox", name="Email").click()
                    await page.wait_for_timeout(FORM_FIELD_DELAY)
                    await page.get_by_role("textbox", name="Email").press("ControlOrMeta+a")
                    await page.wait_for_timeout(100)
                    await page.get_by_role("textbox", name="Email").fill(email)
                    await page.wait_for_timeout(PAGE_LOAD_DELAY)
                    cprint_auto(f"[+] Email filled: {email}")
                else:
                    await page.fill("input[type='email']", email)
                    await page.wait_for_timeout(PAGE_LOAD_DELAY)

                cprint_auto("[+] Filling password field for registration...")
                if await page.get_by_role("textbox", name="Password").count():
                    await page.get_by_role("textbox", name="Password").click()
                    await page.wait_for_timeout(FORM_FIELD_DELAY)
                    await page.get_by_role("textbox", name="Password").press("ControlOrMeta+a")
                    await page.wait_for_timeout(100)
                    await page.get_by_role("textbox", name="Password").fill(password)
                    await page.wait_for_timeout(PAGE_LOAD_DELAY)
                    cprint_auto("[+] Password filled")
                else:
                    await page.fill("input[type='password']", password)
                    await page.wait_for_timeout(PAGE_LOAD_DELAY)

                cprint_auto("[+] Verifying registration fields are filled...")
                try:
                    email_value = await page.get_by_role("textbox", name="Email").input_value()
                    password_value = await page.get_by_role("textbox", name="Password").input_value()
                    cprint_auto(f"[+] Email field value: {email_value[:10]}...")
                    cprint_auto(f"[+] Password field value: {'*' * len(password_value)}")
                    
                    if not email_value or not password_value:
                        cprint_auto("[-] Registration fields are empty, retrying...")
                        await page.wait_for_timeout(FORM_SUBMISSION_DELAY)
                        continue
                except Exception as e:
                    cprint_auto(f"[-] Could not verify registration fields: {e}")
                
                cprint_auto("[+] Waiting before registration submission...")
                await page.wait_for_timeout(FORM_SUBMISSION_DELAY)

                cprint_auto("[+] Submitting registration...")
                if await page.get_by_role("button", name="Sign Up").count():
                    try:
                        await page.get_by_role("button", name="Sign Up").click()
                    except Exception:
                        pass
                elif await page.locator("button:has-text('Sign up')").count():
                    await page.locator("button:has-text('Sign up')").click()
                elif await page.locator("button:has-text('Sign Up')").count():
                    await page.locator("button:has-text('Sign Up')").click()
                else:
                    await page.locator("form").first.evaluate("form => form.submit()")

                cprint_auto("[+] Submitted registration. Monitoring login button for successful authentication...")
                
                login_success = await monitor_login_button_changes(page, timeout=30000)
                
                if login_success:
                    cprint_auto("[+] Login button monitoring indicates successful authentication!")
                else:
                    cprint_auto("[-] Login button monitoring did not detect successful authentication")
                
                await page.wait_for_timeout(2000)
                
                try:
                    error_selectors = [
                        "div:has-text('Too many requests')"
                    ]
                    
                    rate_limit_found = False
                    for selector in error_selectors:
                        if await page.locator(selector).count() > 0:
                            error_text = await page.locator(selector).first.inner_text()
                            cprint_auto(f"[-] Rate limit detected after registration: '{error_text}'")
                            rate_limit_found = True
                            break
                    
                    if rate_limit_found:
                        return False, True
                        
                except Exception as e:
                    print(f"[-] Error checking for rate limit: {e}")

                cprint_auto("[+] Waiting for account creation to complete...")
                await page.wait_for_timeout(1500)
                
                try:
                    if await page.locator("button:has-text('Close')").count():
                        await page.locator("button:has-text('Close')").first.click()
                except Exception:
                    pass
                
                cprint_auto("[+] Waiting for account creation confirmation...")
                
                if login_success:
                    cprint_auto("[+] Account creation confirmed by successful login monitoring!")
                    return True, False
                
                try:
                    await page.wait_for_selector("button:has-text('Generate')", timeout=5000)
                    cprint_auto("[+] Account creation confirmed by Generate button!")
                    return True, False
                except Exception:
                    current_url = page.url
                    if "/artworks" in current_url or "/@" in current_url:
                        cprint_auto("[+] Account creation confirmed by profile page navigation!")
                        return True, False
                    else:
                        print("[-] Account creation failed - no confirmation found")
                        return False, False
                    
            except Exception as e:
                print(f"[-] Account creation attempt {attempt + 1} failed: {e}")
                if attempt < max_attempts - 1:
                    cprint_auto(f"[+] Waiting 5 seconds before retry...")
                    await asyncio.sleep(RETRY_DELAY)
                else:
                    cprint_auto("[-] All account creation attempts failed")
                    return False, False
        return False, False
        
    except Exception as e:
        print(f"[-] Create account failed: {e}")
        return False, False

async def monitor_login_button_changes(page, timeout: int = 30000) -> bool:
    try:
        cprint_auto("[+] Monitoring login button for changes...")
        
        login_button_selector = "button[type='submit']:has-text('Login')"
        
        try:
            await page.wait_for_selector(login_button_selector, timeout=10000)
            cprint_auto("[+] Login button found, monitoring for changes...")
        except Exception:
            cprint_auto("[-] Login button not found, checking if already logged in...")
            if await page.locator("button[aria-haspopup='true']").count() > 0:
                cprint_auto("[+] Already logged in (profile menu found)")
                return True
            return False
        
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                button_element = await page.locator(login_button_selector).first
                
                if await button_element.count() == 0:
                    cprint_auto("[+] Login button disappeared - successful login!")
                    return True
                
                is_disabled = await button_element.get_attribute("disabled")
                is_invisible = await button_element.locator("span:has-text('Login')").get_attribute("class")
                spinner_visible = await button_element.locator("svg.animate-spin").get_attribute("class")
                
                if is_disabled and "invisible" in (is_invisible or ""):
                    cprint_auto("[+] Login button is in loading state (disabled + invisible text + spinner)")
                    await page.wait_for_timeout(1000)
                    continue
                
                if not is_disabled and "invisible" not in (is_invisible or ""):
                    if spinner_visible and "hidden" in spinner_visible:
                        cprint_auto("[+] Login button returned to normal state - checking if login was successful...")
                        await page.wait_for_timeout(2000)
                        
                        if await button_element.count() == 0:
                            cprint_auto("[+] Login button disappeared after state change - successful login!")
                            return True
                        
                        if await page.locator("button[aria-haspopup='true']").count() > 0:
                            cprint_auto("[+] Profile menu found - successful login!")
                            return True
                        
                        if await page.locator("text=Generate").count() > 0:
                            cprint_auto("[+] Generate button found - successful login!")
                            return True
                        
                        if await page.locator("a[href*='/artworks']").count() > 0:
                            cprint_auto("[+] Artworks link found - successful login!")
                            return True
                
                await page.wait_for_timeout(500)
                
            except Exception as e:
                cprint_auto(f"[-] Error monitoring button: {e}")
                await page.wait_for_timeout(1000)
        
        cprint_auto("[-] Login button monitoring timeout")
        
        try:
            if await page.locator("button[aria-haspopup='true']").count() > 0:
                cprint_auto("[+] Final check: Profile menu found - successful login!")
                return True
            
            if await page.locator("text=Generate").count() > 0:
                cprint_auto("[+] Final check: Generate button found - successful login!")
                return True
                
            if await page.locator("a[href*='/artworks']").count() > 0:
                cprint_auto("[+] Final check: Artworks link found - successful login!")
                return True
        except Exception as e:
            cprint_auto(f"[-] Error in final check: {e}")
        
        return False
        
    except Exception as e:
        cprint_auto(f"[-] Error in button monitoring: {e}")
        return False

async def logout_if_possible_async(page) -> None:
    try:
        cprint_auto("[+] Logging out...")
        cprint_auto("[+] Navigating to profile to clear popups...")
        await page.goto(f"https://pixai.art/@{URL_USERNAME}/artworks", timeout=30000)
        await page.wait_for_timeout(1000)
        await page.locator("button[aria-haspopup='true']").first.click()
        await page.wait_for_timeout(300)
        await page.get_by_role("menuitem", name="Log out").click()
        cprint_auto("[+] Logged out successfully")
        await page.wait_for_timeout(500)
        return True
        
    except Exception as e:
        cprint_auto(f"[-] Logout failed: {e}")
        return False

async def create_accounts_multi_browser_async(accounts_count: int, browsers_count: int):
    headless = HEADLESS
    accounts_per_browser = accounts_count // browsers_count
    remainder = accounts_count % browsers_count
    
    cprint_auto(f"[+] Starting multi-browser account creation")
    cprint_auto(f"[+] Total accounts: {accounts_count}")
    cprint_auto(f"[+] Browsers: {browsers_count}")
    cprint_auto(f"[+] Accounts per browser: {accounts_per_browser}")
    cprint_auto(f"[+] Remainder: {remainder}")
    
    created_accounts = []
    failed_accounts = []
    
    async def browser_worker(browser_index: int, accounts_to_create: int, proxy: Optional[str] = None):
        nonlocal created_accounts, failed_accounts
        
        cprint_auto(f"[+] Browser {browser_index + 1}: Starting with {accounts_to_create} accounts")
        
        async with async_playwright() as pw:
            proxies_cycle: List[str] = []
            if proxy:
                proxies_cycle = [proxy]
                cprint_auto(f"[DEBUG] Browser {browser_index + 1}: Using single proxy: {proxy}")
            elif PROXIES:
                proxies_cycle = PROXIES[:]
                cprint_auto(f"[DEBUG] Browser {browser_index + 1}: Using {len(proxies_cycle)} proxies from global list")

            current_proxy_index = browser_index % len(proxies_cycle) if proxies_cycle else 0
            if proxies_cycle:
                initial_proxy = proxies_cycle[current_proxy_index]
                cprint_auto(f"[DEBUG] Browser {browser_index + 1}: Starting with proxy {current_proxy_index + 1}/{len(proxies_cycle)}: {initial_proxy.split(':')[0]}:{initial_proxy.split(':')[1]}")

            async def launch_with_proxy(proxy_url: Optional[str]):
                launch_kwargs = {"headless": headless, "args": BROWSER_ARGS}
                br = await pw.chromium.launch(**launch_kwargs)
                
                context_kwargs = {}
                if proxy_url:
                    parts = proxy_url.split(':')
                    if len(parts) == 4:
                        host, port, user, password = parts
                        context_kwargs["proxy"] = {
                            "server": f"http://{host}:{port}",
                            "username": user,
                            "password": password
                        }
                        cprint_auto(f"[>] Browser {browser_index + 1}: Using proxy {host}:{port} with auth")
                    else:
                        context_kwargs["proxy"] = {"server": f"http://{proxy_url}"}
                        cprint_auto(f"[>] Browser {browser_index + 1}: Using proxy {proxy_url}")
                
                ctx = await br.new_context(**context_kwargs)
                pg = await ctx.new_page()
                return br, ctx, pg

            current_proxy = proxies_cycle[current_proxy_index] if proxies_cycle else None
            browser, context, page = await launch_with_proxy(current_proxy)
            
            try:
                i = 0
                while i < accounts_to_create:
                    email = generate_email(EMAIL_DOMAIN)
                    password = generate_password()
                    
                    current_proxy = proxies_cycle[current_proxy_index] if proxies_cycle else None
                    proxy_info = f" (proxy {current_proxy_index + 1}/{len(proxies_cycle)})" if proxies_cycle else ""
                    cprint_auto(f"[+] Browser {browser_index + 1}: Creating account {i+1}/{accounts_to_create}: {email}{proxy_info}")
                    
                    try:
                        success, rate_limited = await create_account_once_async(pw, context, page, email, password)
                        
                        if success:
                            if send_account_to_api(email, password):
                                created_accounts.append({"email": email, "password": password})
                                cprint_auto(f"[+] Browser {browser_index + 1}: Account {email} created and sent to API")
                                
                                try:
                                    await logout_if_possible_async(page)
                                except Exception:
                                    cprint_auto(f"[!] Browser {browser_index + 1}: Logout failed, continuing...")
                                
                                i += 1
                            else:
                                cprint_auto(f"[-] Browser {browser_index + 1}: Failed to send {email} to API")
                                failed_accounts.append({"email": email, "password": password})
                                i += 1
                        elif rate_limited:
                            cprint_auto("[!] Rate limited. Rotating proxy and retrying this account...")
                            try:
                                await context.close()
                                await browser.close()
                            except Exception:
                                pass
                            if proxies_cycle:
                                cprint_auto(f"[DEBUG] Browser {browser_index + 1}: Available proxies: {len(proxies_cycle)}")
                                if len(proxies_cycle) > 1:
                                    current_proxy_index = (current_proxy_index + 1) % len(proxies_cycle)
                                    current_proxy = proxies_cycle[current_proxy_index]
                                    cprint_auto(f"[>] Browser {browser_index + 1}: Switched to proxy {current_proxy.split(':')[0]}:{current_proxy.split(':')[1]} (proxy {current_proxy_index + 1}/{len(proxies_cycle)})")
                                else:
                                    current_proxy = proxies_cycle[0]
                                    cprint_auto(f"[>] Browser {browser_index + 1}: Only one proxy available, using with delay")
                            else:
                                current_proxy = None
                                cprint_auto(f"[>] Browser {browser_index + 1}: No proxy available, using direct connection")
                            browser, context, page = await launch_with_proxy(current_proxy)
                            if len(proxies_cycle) == 1:
                                await asyncio.sleep(10)  
                            else:
                                await asyncio.sleep(5)
                            continue
                        else:
                            cprint_auto(f"[-] Browser {browser_index + 1}: Failed to create {email}")
                            if proxies_cycle and len(proxies_cycle) > 1:
                                cprint_auto(f"[!] Rotating proxy after failed account creation...")
                                try:
                                    await context.close()
                                    await browser.close()
                                except Exception:
                                    pass
                                current_proxy_index = (current_proxy_index + 1) % len(proxies_cycle)
                                current_proxy = proxies_cycle[current_proxy_index]
                                cprint_auto(f"[>] Browser {browser_index + 1}: Switched to proxy {current_proxy.split(':')[0]}:{current_proxy.split(':')[1]} (proxy {current_proxy_index + 1}/{len(proxies_cycle)})")
                                browser, context, page = await launch_with_proxy(current_proxy)
                                await asyncio.sleep(2)
                            failed_accounts.append({"email": email, "password": password})
                            i += 1
                            
                    except Exception as e:
                        cprint_auto(f"[-] Browser {browser_index + 1}: Error creating account: {e}")
                        failed_accounts.append({"email": email, "password": password})
                        i += 1
                    
                    await asyncio.sleep(ACCOUNT_CREATION_DELAY)
                    
            except Exception as e:
                cprint_auto(f"[-] Browser {browser_index + 1}: Fatal error: {e}")
            finally:
                await context.close()
                await browser.close()
                cprint_auto(f"[+] Browser {browser_index + 1}: Completed")
    
    tasks = []

    for browser_index in range(browsers_count):
        accounts_for_this_browser = accounts_per_browser + (1 if browser_index < remainder else 0)
        if accounts_for_this_browser > 0:
            task = asyncio.create_task(browser_worker(browser_index, accounts_for_this_browser, None))
            tasks.append(task)
    
    cprint_auto(f"[+] Starting {len(tasks)} browsers in parallel...")
    await asyncio.gather(*tasks, return_exceptions=True)
    cprint_auto(f"\n[+] Multi-browser creation completed!")
    cprint_auto(f"[+] Successfully created: {len(created_accounts)}")
    cprint_auto(f"[+] Failed: {len(failed_accounts)}")
    cprint_auto(f"[+] Success rate: {(len(created_accounts)/accounts_count)*100:.1f}%")
    
    return {
        "created_count": len(created_accounts),
        "failed_count": len(failed_accounts),
        "created": created_accounts,
        "failed": failed_accounts,
    }

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PixAI account creator (multi-browser)")
    parser.add_argument("--accounts", type=int, required=True, help="Total number of accounts to create")
    parser.add_argument("--browsers", type=int, default=None, help="Number of parallel browser instances (auto-detected from proxies if not specified)")
    parser.add_argument("--headless", type=str, default=os.getenv("HEADLESS", str(HEADLESS).lower()), help="true/false to run headless")
    parser.add_argument("--api-url", type=str, default=os.getenv("API_URL", API_URL), help="API URL to send created accounts")
    parser.add_argument("--email-domain", type=str, default=os.getenv("EMAIL_DOMAIN", EMAIL_DOMAIN), help="Email domain for generated accounts")
    parser.add_argument("--json", action="store_true", help="Print JSON summary at the end")
    parser.add_argument("--csv", type=str, default=None, help="Optional CSV path to save created accounts")
    parser.add_argument("--proxies-file", type=str, default=os.getenv("PROXIES_FILE", DEFAULT_PROXIES_FILE), help="Path to file with proxies, one per line (e.g., http://user:pass@host:port)")
    parser.add_argument("--proxy", type=str, default=os.getenv("PROXY", None), help="Single proxy URL to use (overrides proxies file for that browser)")
    return parser.parse_args()

def load_proxies(proxies_file: Optional[str]) -> Tuple[List[str], int]:
    proxies: List[str] = []
    if not proxies_file:
        return proxies, 0
    try:
        with open(proxies_file, "r", encoding="utf-8") as f:
            for line in f:
                url = line.strip()
                if not url or url.startswith("#"):
                    continue
                proxies.append(url)
        cprint_auto(f"[+] Loaded {len(proxies)} proxies from {proxies_file}")
    except Exception as e:
        print(f"[!] Failed to read proxies file: {e}")
    return proxies, len(proxies)

def main():
    global API_URL, EMAIL_DOMAIN, HEADLESS, PROXIES, URL_USERNAME
    args = parse_args()

    version = get_version()
    cprint_auto(f"[+] PixAI Account Creator {version}")

    env_browser_args = os.getenv("BROWSER_ARGS")
    if env_browser_args:
        parsed = [flag.strip() for flag in env_browser_args.split(",") if flag.strip()]
        if parsed:
            BROWSER_ARGS.clear()
            BROWSER_ARGS.extend(parsed)

    API_URL = args.api_url
    EMAIL_DOMAIN = args.email_domain
    HEADLESS = str(args.headless).strip().lower() in ("1", "true", "yes", "on")
    PROXIES, proxies_count = load_proxies(args.proxies_file)
    if args.proxy:
        PROXIES = [args.proxy] + PROXIES
        proxies_count = len(PROXIES)

    if args.browsers is None:
        if proxies_count > 0:
            args.browsers = min(args.accounts, proxies_count)
            cprint_auto(f"[+] Auto-detected browsers: {args.browsers} (based on {proxies_count} proxies and {args.accounts} accounts)")
        else:
            args.browsers = 1
            cprint_auto(f"[+] Auto-detected browsers: {args.browsers} (no proxies available)")

    cprint_auto(f"[DEBUG] Headless: {HEADLESS}")
    if PROXIES:
        cprint_auto(f"[DEBUG] Proxies loaded: {proxies_count}")
        
        if args.browsers > proxies_count:
            cprint_auto(f"[!] Warning: Requested {args.browsers} browsers but only {proxies_count} proxies available")
            cprint_auto(f"[!] Some browsers will share proxies")
        elif args.browsers < proxies_count:
            optimal_browsers = min(args.accounts, proxies_count)
            if optimal_browsers > args.browsers:
                cprint_auto(f"[+] Info: You have {proxies_count} proxies available")
                cprint_auto(f"[+] Info: You could use up to {optimal_browsers} browsers for better performance")
    
    try:
        cprint_auto(f"[DEBUG] Multi-browser mode: {args.accounts} accounts, {args.browsers} browsers")
        result = asyncio.run(create_accounts_multi_browser_async(args.accounts, args.browsers))

        if args.csv:
            try:
                os.makedirs(os.path.dirname(args.csv), exist_ok=True) if os.path.dirname(args.csv) else None
                with open(args.csv, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["email", "password", "status"])
                    for acc in result["created"]:
                        writer.writerow([acc["email"], acc["password"], "created"]) 
                    for acc in result["failed"]:
                        writer.writerow([acc["email"], acc["password"], "failed"]) 
                cprint_auto(f"[+] Saved results to CSV: {args.csv}")
            except Exception as e:
                cprint_auto(f"[!] Failed to write CSV: {e}")

        if args.json:
            print(json.dumps({
                "created": result["created_count"],
                "failed": result["failed_count"],
                "total": args.accounts,
                "browsers": args.browsers,
                "api_url": API_URL,
                "email_domain": EMAIL_DOMAIN,
            }, indent=2))
    except KeyboardInterrupt:
        cprint_auto("[!] Stopped by user")
    except Exception as e:
        cprint_auto(f"[-] Fatal error: {e}")

if __name__ == "__main__":
    main()
