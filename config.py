#!/usr/bin/env python3

# Centralized defaults for the account creator. These can be overridden by
# environment variables and then by CLI flags (highest precedence).

# =============================================================================
# CORE SETTINGS
# =============================================================================

# API endpoint to receive created accounts
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"

# Default email domain for generated accounts
EMAIL_DOMAIN = "coonlink.com"

# Username for PixAI profile navigation
URL_USERNAME = "crc137"

# Whether browsers should run headless by default
HEADLESS = True

# =============================================================================
# BROWSER SETTINGS
# =============================================================================

# Extra Chromium flags
BROWSER_ARGS = [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
]

# =============================================================================
# PROXY SETTINGS
# =============================================================================

# Optional path to proxies file (one proxy URL per line)
PROXIES_FILE = ""

# =============================================================================
# TIMING SETTINGS (USE AT YOUR OWN RISK!)
# =============================================================================

# WARNING: These settings control automation speed. Faster settings may trigger
# rate limits or get detected as bot activity. Test carefully and adjust based
# on your internet connection and server response times.

# Delay between account creation attempts (seconds)
ACCOUNT_CREATION_DELAY = 2.0

# Delay between form field interactions (milliseconds)
FORM_FIELD_DELAY = 300

# Delay before form submission (milliseconds)
FORM_SUBMISSION_DELAY = 1000

# Delay after page load (milliseconds)
PAGE_LOAD_DELAY = 500

# Delay between retry attempts (seconds)
RETRY_DELAY = 5.0

# Delay when rate limited (seconds)
RATE_LIMIT_DELAY = 15.0

# Maximum retry attempts per account
MAX_RETRY_ATTEMPTS = 3

# =============================================================================
# COLOR CODES (for console output)
# =============================================================================

GREEN = '\033[0;32m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
YELLOW = '\033[0;33m'
CYAN = '\033[0;36m'
NC = '\033[0m'