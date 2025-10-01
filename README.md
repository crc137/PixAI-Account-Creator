# PixAI-Account-Creator

Welcome to PixAI-Account-Creator, your go-to Python automation tool for effortlessly generating multiple accounts on the PixAI platform!
Streamline your account provisioning process, integrate new accounts with external systems, and save valuable time.

![img](https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg)

## Features

This project is packed with features designed to make mass account creation a breeze:

### Core Features
*  **Automated Account Registration:** Leverages `Playwright` for robust browser automation, handling PixAI's registration flow from start to finish, supporting both headless (background) and visible browser modes.
*  **Parallel Processing:** Significantly speeds up creation by concurrently registering accounts across multiple browser instances. Configure the number of parallel operations to match your system's capabilities.
*  **Dynamic Credential Generation:** Automatically generates unique email addresses (using a configurable domain) and strong, secure passwords for every new account.
*  **External API Integration:** Seamlessly sends newly created account credentials (email and password) via HTTP POST requests to a user-defined API endpoint, enabling easy integration with your external systems or databases.

### Advanced Features
*  **System Performance Analysis:** Includes a dedicated `system_check.py` script that analyzes your host machine's CPU, RAM, and GPU to recommend the optimal number of parallel browser instances for maximum efficiency.
*  **Proxy Support & Rotation:** Automatic proxy rotation when rate limits are detected, supporting both single proxy and proxy file configurations.
*  **Multi-Configuration Support:** Flexible configuration through config.py, environment variables, and command-line arguments with clear precedence.
*  **Export Capabilities:** Save results to CSV files and generate JSON summaries for integration with other systems.
*  **Color-Coded Output:** Intuitive console output with color-coded messages for better user experience.
*  **Robust Error Handling:** Incorporates comprehensive error handling, retry mechanisms, and automatic proxy rotation to enhance stability.

## Technologies Used

This project is built primarily with Python and relies on powerful libraries for automation and integration:

### Core
*   **Python:** The core programming language powering the automation logic.
*   **Playwright:** A robust library for browser automation, enabling headless and headed interaction with web pages.
*   **Requests:** (Implied) For making HTTP POST requests to external APIs for account integration.

## Getting Started

Follow these steps to get PixAI-Account-Creator up and running on your local machine.

### Prerequisites

*   **Python 3.8+** installed on your system.
*   Internet connection for downloading dependencies and accessing PixAI.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/crc137/PixAI-Account-Creator.git
    cd PixAI-Account-Creator
    ```

2.  **Quick Setup (Recommended):**
    Use the automated installation script:
    ```bash
    chmod +x install.sh
    ./install.sh
    ```

3.  **Manual Installation:**
    If you prefer manual setup:
    ```bash
    # Install Python dependencies
    pip install -r requirements.txt
    
    # Install Playwright browser binaries
    playwright install && playwright install-deps
    ```

### Configuration

The project supports multiple configuration methods with the following precedence (highest to lowest):
1. **Command-line arguments** (highest priority)
2. **Environment variables**
3. **config.py file** (defaults)

#### Method 1: config.py (Recommended for defaults)

Edit `config.py` to set your default configuration:

```python
# API endpoint to receive created accounts
API_URL = "https://your-api.com/endpoint"

# Whether browsers should run headless by default
HEADLESS = True

# Default email domain for generated accounts
EMAIL_DOMAIN = "yourdomain.com"

# Extra Chromium flags
BROWSER_ARGS = [
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
]

# Optional path to proxies file
PROXIES_FILE = "proxies.txt"

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
```

#### Method 2: Environment Variables

Set environment variables to override config.py defaults:

```bash
export API_URL="https://your-api.com/endpoint"
export EMAIL_DOMAIN="yourdomain.com"
export HEADLESS="false"
export PROXY="http://user:pass@proxy:port"
export PROXIES_FILE="proxies.txt"
export BROWSER_ARGS="--no-sandbox,--disable-gpu,--disable-dev-shm-usage"

# Timing settings (use with caution!)
export ACCOUNT_CREATION_DELAY="1.5"
export FORM_FIELD_DELAY="200"
export FORM_SUBMISSION_DELAY="800"
export PAGE_LOAD_DELAY="300"
export RETRY_DELAY="3.0"
export RATE_LIMIT_DELAY="10.0"
export MAX_RETRY_ATTEMPTS="5"
```

#### Method 3: Command-line Arguments (Highest Priority)

All settings can be overridden via CLI arguments (see Usage section below).

### Usage

#### 1. System Performance Check (Recommended)

Run the system analysis to get optimal browser recommendations:

    ```bash
# Basic system check
python3 system_check.py

# With JSON output for integration
python3 system_check.py --json

# Custom resource requirements
python3 system_check.py --memory-per-browser 1.0 --cpu-per-browser 0.5

# Auto-install missing dependencies
python3 system_check.py --auto-install
```

#### 2. Account Creation

**Basic Usage:**
```bash
# Create 10 accounts with 2 browsers
python3 account_creator.py --accounts 10 --browsers 2

# Visible browser mode
python3 account_creator.py --accounts 5 --browsers 1 --headless false
```

**Advanced Usage:**
```bash
# With custom API and domain
python3 account_creator.py --accounts 10 --browsers 2 \
  --api-url "https://your-api.com/endpoint" \
  --email-domain "yourdomain.com"

# With proxy support
python3 account_creator.py --accounts 10 --browsers 2 \
  --proxy "http://user:pass@proxy:port"

# With proxy file (one proxy per line)
python3 account_creator.py --accounts 10 --browsers 2 \
  --proxies-file "proxies.txt"

# Export results
python3 account_creator.py --accounts 10 --browsers 2 \
  --csv "results/accounts.csv" --json
```

#### Command-line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--accounts` | Total number of accounts to create | `--accounts 10` |
| `--browsers` | Number of parallel browser instances | `--browsers 2` |
| `--headless` | Run browsers in headless mode | `--headless false` |
| `--api-url` | API endpoint for account data | `--api-url "https://api.com/endpoint"` |
| `--email-domain` | Domain for generated emails | `--email-domain "yourdomain.com"` |
| `--proxy` | Single proxy URL | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | File with proxy URLs (one per line) | `--proxies-file "proxies.txt"` |
| `--csv` | Save results to CSV file | `--csv "results/accounts.csv"` |
| `--json` | Print JSON summary | `--json` |

#### Proxy Configuration

The tool supports both single proxy and proxy rotation:

**Single Proxy:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --proxy "http://user:pass@proxy:port"
```

**Proxy File (proxies.txt):**
```
http://user1:pass1@proxy1:port
http://user2:pass2@proxy2:port
socks5://user3:pass3@proxy3:port
```

**Automatic Proxy Rotation:**
When rate limits are detected ("Too many requests"), the tool automatically:
1. Closes the current browser
2. Switches to the next proxy in the list
3. Relaunches the browser with the new proxy
4. Retries the same account

#### Output Formats

**Console Output:**
The tool provides color-coded console output:
- `[+]` - Success messages (green)
- `[-]` - Error messages (red)
- `[>]` - Information (blue)
- `[!]` - Warnings (yellow)
- `[?]` - Debug messages (cyan)

**CSV Export:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --csv "results/accounts.csv"
```
Creates a CSV file with columns: `email`, `password`, `status`

**JSON Export:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --json
```
Outputs JSON summary with creation statistics.

####Timing Configuration (Advanced Users Only)

**WARNING:** These settings control automation speed. Faster settings may trigger rate limits or get detected as bot activity. Test carefully and adjust based on your internet connection and server response times.

**Available Timing Settings:**
- `ACCOUNT_CREATION_DELAY` - Delay between account creation attempts (seconds)
- `FORM_FIELD_DELAY` - Delay between form field interactions (milliseconds)
- `FORM_SUBMISSION_DELAY` - Delay before form submission (milliseconds)
- `PAGE_LOAD_DELAY` - Delay after page load (milliseconds)
- `RETRY_DELAY` - Delay between retry attempts (seconds)
- `RATE_LIMIT_DELAY` - Delay when rate limited (seconds)
- `MAX_RETRY_ATTEMPTS` - Maximum retry attempts per account

**Example - Faster Settings (Use at your own risk!):**
```python
# In config.py
ACCOUNT_CREATION_DELAY = 1.0  # Faster account creation
FORM_FIELD_DELAY = 150        # Faster form filling
FORM_SUBMISSION_DELAY = 500    # Faster submission
PAGE_LOAD_DELAY = 200          # Faster page processing
RETRY_DELAY = 2.0             # Faster retries
RATE_LIMIT_DELAY = 8.0        # Shorter rate limit wait
MAX_RETRY_ATTEMPTS = 5        # More retry attempts
```

**Example - Slower Settings (More stable):**
```python
# In config.py
ACCOUNT_CREATION_DELAY = 5.0  # Slower, more human-like
FORM_FIELD_DELAY = 800        # More realistic typing
FORM_SUBMISSION_DELAY = 2000  # Longer form review
PAGE_LOAD_DELAY = 1000        # More page processing time
RETRY_DELAY = 10.0           # Longer retry delays
RATE_LIMIT_DELAY = 30.0      # Longer rate limit wait
MAX_RETRY_ATTEMPTS = 2       # Fewer retry attempts
```
