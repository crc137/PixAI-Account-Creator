#!/usr/bin/env python3

# Centralized defaults for the account creator. These can be overridden by
# environment variables and then by CLI flags (highest precedence).

# API endpoint to receive created accounts
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"

URL_USERNAME = "crc137"

# Whether browsers should run headless by default
HEADLESS = True

# Default email domain for generated accounts
EMAIL_DOMAIN = "coonlink.com"

# Extra Chromium flags
BROWSER_ARGS = [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
]

# Optional path to proxies file (one proxy URL per line)
PROXIES_FILE = ""
