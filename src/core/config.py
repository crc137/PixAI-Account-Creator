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
HEADLESS = False # True for headless, False for visible

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

# =============================================================================
# VERSION INFORMATION
# =============================================================================

VERSION = "1.0.0"
VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_PATCH = 0
VERSION_STRING = "v1.0.0"
BUILD_DATE = "2025-10-01"
RELEASE_NAME = "PixAI Account Creator"
AUTHOR = "PixAI Account Creator"
PROJECT_URL = "https://github.com/crc137/PixAI-Account-Creator"
TITLE = "PixAI Daily"

# =============================================================================
# UI ENHANCEMENT SETTINGS
# =============================================================================

LOGO_SVG_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/logo.svg"
LOGO_ICO_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/logo.ico"
FONT_PHONK_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/PhonkSans-Black.woff"
FONT_GILROY_MEDIUM_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-Medium.woff"
FONT_GILROY_SEMIBOLD_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-SemiBold.woff"
FONT_GILROY_EXTRABOLD_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-ExtraBold.woff"
FONT_HANSON_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/HansonBold.woff"