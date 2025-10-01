# PixAI-Account-Creator

Welcome to **PixAI-Account-Creator**, your Python automation tool for effortlessly generating multiple accounts on the PixAI platform.
Streamline your account provisioning process, integrate new accounts with external systems, and save valuable time.

![PixAI](https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg)

## Features

This project includes features to make mass account creation simple and efficient:

### Core Features

* **Automated Account Registration:** Uses `Playwright` for browser automation, handling PixAI's registration flow from start to finish. Supports both headless and visible browsers.
* **Parallel Processing:** Create multiple accounts simultaneously across several browser instances. Configure the number of parallel operations based on your system resources.
* **Dynamic Credential Generation:** Generates unique email addresses (with a configurable domain) and strong passwords for each account.
* **External API Integration:** Sends account credentials (email & password) via HTTP POST to a user-defined API endpoint.

### Advanced Features

* **System Performance Analysis:** `system_check.py` analyzes CPU, RAM, and GPU to recommend the optimal number of parallel browsers.
* **Proxy Support & Rotation:** Automatically rotates proxies when rate limits occur. Supports single proxy or a list of proxies.
* **Flexible Configuration:** Supports `config.py`, environment variables, and command-line arguments with clear priority.
* **Export Options:** Save results as CSV files and generate JSON summaries.
* **Color-Coded Console Output:** Easily distinguish success, error, info, warnings, and debug messages.
* **Robust Error Handling:** Retries failed accounts, rotates proxies automatically, and handles common errors gracefully.

## Technologies Used

* **Python 3.8+** — Core language for automation logic
* **Playwright** — Headless/headed browser automation
* **Requests** — For sending account data to external APIs

## Getting Started

### Prerequisites

* Python 3.8+ installed on your system
* Internet connection for dependencies and PixAI access

### Installation

**Clone the repository:**

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
```

**Quick Setup (Recommended):**

```bash
chmod +x install.sh
./install.sh
```

**Manual Installation:**

```bash
pip install -r requirements.txt
playwright install && playwright install-deps
```

## Configuration

Configuration can be done via:

1. **Command-line arguments** (highest priority)
2. **Environment variables**
3. **config.py** (defaults)

### config.py (Recommended)

```python
API_URL = "https://your-api.com/endpoint"
HEADLESS = True
EMAIL_DOMAIN = "yourdomain.com"
BROWSER_ARGS = ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
PROXIES_FILE = "proxies.txt"

# Timing (use at your own risk!)
ACCOUNT_CREATION_DELAY = 2.0
FORM_FIELD_DELAY = 300
FORM_SUBMISSION_DELAY = 1000
PAGE_LOAD_DELAY = 500
RETRY_DELAY = 5.0
RATE_LIMIT_DELAY = 15.0
MAX_RETRY_ATTEMPTS = 3
```

### Environment Variables

```bash
export API_URL="https://your-api.com/endpoint"
export EMAIL_DOMAIN="yourdomain.com"
export HEADLESS="false"
export PROXY="http://user:pass@proxy:port"
export PROXIES_FILE="proxies.txt"
export BROWSER_ARGS="--no-sandbox,--disable-gpu,--disable-dev-shm-usage"

export ACCOUNT_CREATION_DELAY="1.5"
export FORM_FIELD_DELAY="200"
export FORM_SUBMISSION_DELAY="800"
export PAGE_LOAD_DELAY="300"
export RETRY_DELAY="3.0"
export RATE_LIMIT_DELAY="10.0"
export MAX_RETRY_ATTEMPTS="5"
```

### Command-Line Arguments

| Argument         | Description                   | Example                                |
| ---------------- | ----------------------------- | -------------------------------------- |
| `--accounts`     | Number of accounts to create  | `--accounts 10`                        |
| `--browsers`     | Number of parallel browsers   | `--browsers 2`                         |
| `--headless`     | Headless mode                 | `--headless false`                     |
| `--api-url`      | API endpoint for account data | `--api-url "https://api.com/endpoint"` |
| `--email-domain` | Domain for generated emails   | `--email-domain "yourdomain.com"`      |
| `--proxy`        | Single proxy URL              | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | File with proxy URLs          | `--proxies-file "proxies.txt"`         |
| `--csv`          | Save results to CSV           | `--csv "results/accounts.csv"`         |
| `--json`         | Print JSON summary            | `--json`                               |

## Usage

### 1. System Check

```bash
python3 system_check.py
python3 system_check.py --json
python3 system_check.py --memory-per-browser 1.0 --cpu-per-browser 0.5
python3 system_check.py --auto-install
```

### 2. Account Creation

**Basic:**

```bash
python3 account_creator.py --accounts 10 --browsers 2
python3 account_creator.py --accounts 5 --browsers 1 --headless false
```

**Advanced:**

```bash
python3 account_creator.py --accounts 10 --browsers 2 \
  --api-url "https://your-api.com/endpoint" \
  --email-domain "yourdomain.com"

python3 account_creator.py --accounts 10 --browsers 2 --proxy "http://user:pass@proxy:port"
python3 account_creator.py --accounts 10 --browsers 2 --proxies-file "proxies.txt"

python3 account_creator.py --accounts 10 --browsers 2 --csv "results/accounts.csv" --json
```

### Proxy Handling

* **Single Proxy:** `--proxy "http://user:pass@proxy:port"`
* **Proxy File:** `--proxies-file "proxies.txt"`
* **Auto-Rotation:** Detects "Too many requests", closes browser, switches proxy, retries.

### Output Formats

* **Console:** Color-coded `[+]`, `[-]`, `[>]`, `[!]`, `[?]`
* **CSV:** Columns `email`, `password`, `status`
* **JSON:** Creation summary

### Timing Configuration (Advanced)

Adjust delays and retry counts to control automation speed and human-likeness:

**Example Faster Settings (Risky):**

```python
ACCOUNT_CREATION_DELAY = 1.0
FORM_FIELD_DELAY = 150
FORM_SUBMISSION_DELAY = 500
PAGE_LOAD_DELAY = 200
RETRY_DELAY = 2.0
RATE_LIMIT_DELAY = 8.0
MAX_RETRY_ATTEMPTS = 5
```

**Example Slower Settings (Stable):**

```python
ACCOUNT_CREATION_DELAY = 5.0
FORM_FIELD_DELAY = 800
FORM_SUBMISSION_DELAY = 2000
PAGE_LOAD_DELAY = 1000
RETRY_DELAY = 10.0
RATE_LIMIT_DELAY = 30.0
MAX_RETRY_ATTEMPTS = 2
```
