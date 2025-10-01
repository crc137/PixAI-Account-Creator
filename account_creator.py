#!/usr/bin/env python3

import os
import sys
import time
import random
import string
import asyncio
import requests
from typing import List, Dict
from playwright.async_api import async_playwright

# Settings
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add" # change to your API URL
HEADLESS = False # True - headless, False - visible
BROWSER_ARGS = ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"] # add your own browser arguments
EMAIL_DOMAIN = "coonlink.com" # change to your domain

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

async def create_account_once_async(pw, context, page, email: str, password: str) -> bool:
    try:
        await page.goto("https://pixai.art/", timeout=60000)
        
        max_attempts = 3
        
        for attempt in range(max_attempts):
            print(f"[+] Account creation attempt {attempt + 1}/{max_attempts}")
            
            try:
                try:
                    await page.get_by_role("button", name="Sign in").click()
                    await page.wait_for_timeout(300)
                except Exception as e:
                    print(f"[-] Could not find Sign in button: {e}")
                    print("[+] Refreshing page and trying again...")
                    await page.reload()
                    await page.wait_for_timeout(1000)
                    await page.get_by_role("button", name="Sign in").click()
                    await page.wait_for_timeout(300)

                try:
                    await page.get_by_role("button", name="Continue with Email", exact=False).click()
                except Exception:
                    if await page.locator("text=Continue with Email").count():
                        await page.locator("text=Continue with Email").click()
                    else:
                        print("[-] Could not find 'Continue with Email' button — continue anyway")

                await page.wait_for_timeout(300)
                
                if await page.locator("text=Register").count():
                    await page.locator("text=Register").click()

                print("[+] Filling email field for registration...")
                if await page.get_by_role("textbox", name="Email").count():
                    await page.get_by_role("textbox", name="Email").click()
                    await page.wait_for_timeout(300)
                    await page.get_by_role("textbox", name="Email").press("ControlOrMeta+a")
                    await page.wait_for_timeout(100)
                    await page.get_by_role("textbox", name="Email").fill(email)
                    await page.wait_for_timeout(500)
                    print(f"[+] Email filled: {email}")
                else:
                    await page.fill("input[type='email']", email)
                    await page.wait_for_timeout(500)

                print("[+] Filling password field for registration...")
                if await page.get_by_role("textbox", name="Password").count():
                    await page.get_by_role("textbox", name="Password").click()
                    await page.wait_for_timeout(300)
                    await page.get_by_role("textbox", name="Password").press("ControlOrMeta+a")
                    await page.wait_for_timeout(100)
                    await page.get_by_role("textbox", name="Password").fill(password)
                    await page.wait_for_timeout(500)
                    print("[+] Password filled")
                else:
                    await page.fill("input[type='password']", password)
                    await page.wait_for_timeout(500)

                print("[+] Verifying registration fields are filled...")
                try:
                    email_value = await page.get_by_role("textbox", name="Email").input_value()
                    password_value = await page.get_by_role("textbox", name="Password").input_value()
                    print(f"[+] Email field value: {email_value[:10]}...")
                    print(f"[+] Password field value: {'*' * len(password_value)}")
                    
                    if not email_value or not password_value:
                        print("[-] Registration fields are empty, retrying...")
                        await page.wait_for_timeout(1000)
                        continue
                except Exception as e:
                    print(f"[-] Could not verify registration fields: {e}")
                
                print("[+] Waiting before registration submission...")
                await page.wait_for_timeout(1000)

                print("[+] Submitting registration...")
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

                print("[+] Submitted registration. Waiting for response...")
                await page.wait_for_timeout(2000)
                
                try:
                    error_selectors = [
                        "div:has-text('Too many requests')"
                    ]
                    
                    rate_limit_found = False
                    for selector in error_selectors:
                        if await page.locator(selector).count() > 0:
                            error_text = await page.locator(selector).first.inner_text()
                            print(f"[-] Rate limit detected after registration: '{error_text}'")
                            print(f"[+] Waiting 15 seconds before retry attempt {attempt + 1}...")
                            await asyncio.sleep(15)
                            print("[+] Continuing with retry...")
                            rate_limit_found = True
                            break
                    
                    if rate_limit_found:
                        continue
                        
                except Exception as e:
                    print(f"[-] Error checking for rate limit: {e}")

                print("[+] Waiting for account creation to complete...")
                await page.wait_for_timeout(1500)
                
                try:
                    if await page.locator("button:has-text('Close')").count():
                        await page.locator("button:has-text('Close')").first.click()
                except Exception:
                    pass
                
                print("[+] Waiting for account creation confirmation...")
                
                try:
                    await page.wait_for_selector("button:has-text('Generate')", timeout=5000)
                    print("[+] Account creation confirmed!")
                    return True
                except Exception:
                    print("[-] Account creation failed - no Generate button found")
                    return False
                    
            except Exception as e:
                print(f"[-] Account creation attempt {attempt + 1} failed: {e}")
                if attempt < max_attempts - 1:
                    print(f"[+] Waiting 5 seconds before retry...")
                    await asyncio.sleep(5)
                else:
                    print("[-] All account creation attempts failed")
                    return False
        return False
        
    except Exception as e:
        print(f"[-] Create account failed: {e}")
        return False

async def logout_if_possible_async(page) -> None:
    try:
        print("[+] Logging out...")
        print("[+] Navigating to profile to clear popups...")
        await page.goto("https://pixai.art/@crc137/artworks", timeout=30000)
        await page.wait_for_timeout(1000)
        await page.locator("button[aria-haspopup='true']").first.click()
        await page.wait_for_timeout(300)
        await page.get_by_role("menuitem", name="Log out").click()
        print("[+] Logged out successfully")
        await page.wait_for_timeout(500)
        return True
        
    except Exception as e:
        print(f"[-] Logout failed: {e}")
        return False

async def create_accounts_multi_browser_async(accounts_count: int, browsers_count: int):
    headless = HEADLESS
    accounts_per_browser = accounts_count // browsers_count
    remainder = accounts_count % browsers_count
    
    print(f"[+] Starting multi-browser account creation")
    print(f"[+] Total accounts: {accounts_count}")
    print(f"[+] Browsers: {browsers_count}")
    print(f"[+] Accounts per browser: {accounts_per_browser}")
    print(f"[+] Remainder: {remainder}")
    
    created_accounts = []
    failed_accounts = []
    
    async def browser_worker(browser_index: int, accounts_to_create: int):
        nonlocal created_accounts, failed_accounts
        
        print(f"[+] Browser {browser_index + 1}: Starting with {accounts_to_create} accounts")
        
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=headless, args=BROWSER_ARGS)
            context = await browser.new_context()
            page = await context.new_page()
            
            try:
                for i in range(accounts_to_create):
                    email = generate_email(EMAIL_DOMAIN)
                    password = generate_password()
                    
                    print(f"[+] Browser {browser_index + 1}: Creating account {i+1}/{accounts_to_create}: {email}")
                    
                    try:
                        success = await create_account_once_async(pw, context, page, email, password)
                        
                        if success:
                            if send_account_to_api(email, password):
                                created_accounts.append({"email": email, "password": password})
                                print(f"[+] Browser {browser_index + 1}: Account {email} created and sent to API")
                                
                                await logout_if_possible_async(page)
                            else:
                                print(f"[-] Browser {browser_index + 1}: Failed to send {email} to API")
                                failed_accounts.append({"email": email, "password": password})
                        else:
                            print(f"[-] Browser {browser_index + 1}: Failed to create {email}")
                            failed_accounts.append({"email": email, "password": password})
                            
                    except Exception as e:
                        print(f"[-] Browser {browser_index + 1}: Error creating account: {e}")
                        failed_accounts.append({"email": email, "password": password})
                    
                    await asyncio.sleep(2)
                    
            except Exception as e:
                print(f"[-] Browser {browser_index + 1}: Fatal error: {e}")
            finally:
                await context.close()
                await browser.close()
                print(f"[+] Browser {browser_index + 1}: Completed")
    
    tasks = []
    for browser_index in range(browsers_count):
        accounts_for_this_browser = accounts_per_browser + (1 if browser_index < remainder else 0)
        if accounts_for_this_browser > 0:
            task = browser_worker(browser_index, accounts_for_this_browser)
            tasks.append(task)
    
    print(f"[+] Starting {len(tasks)} browsers in parallel...")
    await asyncio.gather(*tasks, return_exceptions=True)
    print(f"\n[+] Multi-browser creation completed!")
    print(f"[+] Successfully created: {len(created_accounts)}")
    print(f"[+] Failed: {len(failed_accounts)}")
    print(f"[+] Success rate: {(len(created_accounts)/accounts_count)*100:.1f}%")
    
    return len(created_accounts)

def main():
    import sys
    
    if HEADLESS:
        print("[DEBUG] Browser will be headless")
    else:
        print("[DEBUG] Browser will be visible")
    
    accounts_count = None
    browsers_count = None
    
    for arg in sys.argv:
        if arg.startswith('--accounts='):
            accounts_count = int(arg.split('=')[1])
        elif arg.startswith('--browsers='):
            browsers_count = int(arg.split('=')[1])
    
    if not accounts_count or not browsers_count:
        print("Usage: python3 account_creator.py --accounts=N --browsers=M")
        print("Example: python3 account_creator.py --accounts=12 --browsers=3")
        sys.exit(1)
    
    try:
        import asyncio
        
        print(f"[DEBUG] Multi-browser mode: {accounts_count} accounts, {browsers_count} browsers")
        asyncio.run(create_accounts_multi_browser_async(accounts_count, browsers_count))
            
    except KeyboardInterrupt:
        print("[!] Stopped by user")
    except Exception as e:
        print(f"[-] Fatal error: {e}")

if __name__ == "__main__":
    main()
