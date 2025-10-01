# PixAI Account Creator

Welcome to **PixAI Account Creator**, your professional Python automation tool for effortlessly generating multiple accounts on the PixAI platform.
Streamline your account provisioning process, integrate new accounts with external systems, and save valuable time.

![PixAI](https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg)

## Project Structure

This project follows a professional Python package structure:

```
PixAI-Account-Creator/
├── src/                          # Main source code
│   ├── core/                     # Core configuration and version
│   │   ├── config.py             # Centralized configuration
│   │   └── version.py             # Version management
│   ├── ui/                       # UI enhancement modules
│   │   └── ui_enhancer.py        # Browser UI enhancements
│   ├── utils/                    # Utility modules
│   │   └── system_check.py       # System analysis tool
│   └── scripts/                  # Executable scripts
│       ├── account_creator.py    # Main account creation script
│       └── preview_browser.py    # Browser preview script
├── assets/                       # Static assets (fonts, logos)
├── docs/                         # Documentation
├── account_creator.py           # Main script wrapper
├── preview_browser.py           # Preview script wrapper
├── system_check.py              # System check wrapper
└── version.py                   # Version wrapper
```

## Features

This project includes features to make mass account creation simple and efficient:

### Core Features

* **Automated Account Registration:** Uses `Playwright` for browser automation, handling PixAI's registration flow from start to finish. Supports both headless and visible browsers.
* **Parallel Processing:** Create multiple accounts simultaneously across several browser instances. Configure the number of parallel operations based on your system resources.
* **Dynamic Credential Generation:** Generates unique email addresses (with a configurable domain) and strong passwords for each account.
* **External API Integration:** Sends account credentials (email & password) via HTTP POST to a user-defined API endpoint.

### UI Enhancements

* **Custom Browser Styling:** Automatically applies custom fonts, logos, and branding to the PixAI website during automation.
* **Font Collection:** Supports PhonkSans, Gilroy (Medium/SemiBold/ExtraBold), and Hanson fonts from cloud URLs.
* **Logo Integration:** Custom SVG/ICO logos with automatic favicon replacement.
* **Modern UI Elements:** Glassmorphism-style author credits and project branding.

### Advanced Features

* **System Performance Analysis:** `system_check.py` analyzes CPU, RAM, and GPU to recommend the optimal number of parallel browsers.
* **Proxy Support & Rotation:** Automatically rotates proxies when rate limits occur. Supports single proxy or a list of proxies.
* **Flexible Configuration:** Centralized configuration system with `config.py`, environment variables, and command-line arguments.
* **Export Options:** Save results as CSV files and generate JSON summaries.
* **Color-Coded Console Output:** Easily distinguish success, error, info, warnings, and debug messages.
* **Robust Error Handling:** Retries failed accounts, rotates proxies automatically, and handles common errors gracefully.
* **Professional Structure:** Modular architecture with clean separation of concerns.

## Technologies Used

* **Python 3.8+** — Core language for automation logic
* **Playwright** — Headless/headed browser automation
* **Requests** — For sending account data to external APIs
* **psutil** — System resource monitoring
* **GPUtil** — GPU detection and monitoring
* **asyncio** — Asynchronous programming for parallel processing

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
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

**Manual Installation:**

```bash
pip install -r requirements.txt
python3 -m playwright install && python3 -m playwright install-deps
```

## Configuration

Configuration can be done via:

1. **Command-line arguments** (highest priority)
2. **Environment variables**
3. **`src/core/config.py`** (defaults)

### Centralized Configuration (`src/core/config.py`)

```python
# Core Settings
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False

# Browser Settings
BROWSER_ARGS = [
    "--no-sandbox",
    "--disable-setuid-sandbox", 
    "--disable-dev-shm-usage"
]

# UI Enhancement Settings
LOGO_SVG_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/logo.svg"
LOGO_ICO_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/logo.ico"
FONT_PHONK_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/PhonkSans-Black.woff"
FONT_GILROY_MEDIUM_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-Medium.woff"
FONT_GILROY_SEMIBOLD_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-SemiBold.woff"
FONT_GILROY_EXTRABOLD_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/Gilroy-ExtraBold.woff"
FONT_HANSON_URL = "https://raw.coonlink.com/cloud/PixAI%20Daily/HansonBold.woff"

# Timing Settings (use at your own risk!)
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

### 2. Browser Preview

```bash
# Preview with UI enhancements
python3 preview_browser.py --headless=false
python3 preview_browser.py --url="https://pixai.art/" --headless=true
```

### 3. Account Creation

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

### 4. Version Information

```bash
python3 version.py
```

### Proxy Handling

* **Single Proxy:** `--proxy "http://user:pass@proxy:port"`
* **Proxy File:** `--proxies-file "proxies.txt"`
* **Auto-Rotation:** Detects "Too many requests", closes browser, switches proxy, retries.

### Output Formats

* **Console:** Color-coded `[+]`, `[-]`, `[>]`, `[!]`, `[?]`
* **CSV:** Columns `email`, `password`, `status`
* **JSON:** Creation summary

### UI Enhancements

The project includes automatic UI enhancements that apply during browser automation:

* **Custom Fonts:** PhonkSans, Gilroy (Medium/SemiBold/ExtraBold), Hanson
* **Logo Integration:** Custom SVG/ICO logos with favicon replacement
* **Modern Styling:** Glassmorphism effects and smooth animations
* **Branding:** Author credits and project information

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

## Development

### Project Structure

The project follows a professional Python package structure with clear separation of concerns:

- **`src/core/`** - Core configuration and version management
- **`src/ui/`** - UI enhancement modules
- **`src/utils/`** - Utility modules (system analysis)
- **`src/scripts/`** - Executable scripts
- **`assets/`** - Static assets (fonts, logos)
- **`docs/`** - Documentation

### Module Import

```python
from src.core import config as cfg
from src.ui.ui_enhancer import ui_enhancer
from src.core.version import get_version
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For support and questions, please open an issue on GitHub or contact the maintainers.

## 🛡 License
MIT © [Coonlink](https://coonlink.com)
