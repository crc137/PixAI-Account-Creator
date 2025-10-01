# PixAI Account Creator

Professional Python automation tool for creating multiple PixAI accounts with parallel browser processing.

![PixAI](https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg)

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator

# Install dependencies
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

### Basic Usage

```bash
# Check system capabilities
python3 system_check.py

# Create accounts (5 accounts, 2 browsers)
python3 account_creator.py --accounts 5 --browsers 2

# Preview browser with enhancements
python3 preview_browser.py --headless=false
```

## Commands

### System Analysis
```bash
python3 system_check.py                    # Basic system check
python3 system_check.py --json             # JSON output
python3 system_check.py --auto-install     # Auto-install Playwright
```

### Account Creation
```bash
# Basic usage
python3 account_creator.py --accounts 10 --browsers 2

# With custom settings
python3 account_creator.py --accounts 10 --browsers 2 \
  --api-url "https://your-api.com/endpoint" \
  --email-domain "yourdomain.com" \
  --headless false

# With proxy support
python3 account_creator.py --accounts 10 --browsers 2 \
  --proxy "http://user:pass@proxy:port"

# Export results
python3 account_creator.py --accounts 10 --browsers 2 \
  --csv "results/accounts.csv" --json
```

### Browser Preview
```bash
python3 preview_browser.py --headless=false
python3 preview_browser.py --url="https://pixai.art/"
```

### Version Info
```bash
python3 version.py
```

## Configuration

### Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--accounts` | Number of accounts to create | `--accounts 10` |
| `--browsers` | Number of parallel browsers | `--browsers 2` |
| `--headless` | Headless mode | `--headless false` |
| `--api-url` | API endpoint for account data | `--api-url "https://api.com/endpoint"` |
| `--email-domain` | Domain for generated emails | `--email-domain "yourdomain.com"` |
| `--proxy` | Single proxy URL | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | File with proxy URLs | `--proxies-file "proxies.txt"` |
| `--csv` | Save results to CSV | `--csv "results/accounts.csv"` |
| `--json` | Print JSON summary | `--json` |

### Environment Variables

```bash
export API_URL="https://your-api.com/endpoint"
export EMAIL_DOMAIN="yourdomain.com"
export HEADLESS="false"
export PROXY="http://user:pass@proxy:port"
export PROXIES_FILE="proxies.txt"
```

### Configuration File

Edit `src/core/config.py` for default settings:

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

# Timing Settings (use at your own risk!)
ACCOUNT_CREATION_DELAY = 2.0
FORM_FIELD_DELAY = 300
FORM_SUBMISSION_DELAY = 1000
PAGE_LOAD_DELAY = 500
RETRY_DELAY = 5.0
RATE_LIMIT_DELAY = 15.0
MAX_RETRY_ATTEMPTS = 3
```

## Advanced Usage

### Proxy Support

**Single Proxy:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --proxy "http://user:pass@proxy:port"
```

**Proxy File:**
```bash
# Create proxies.txt with one proxy per line
echo "http://user:pass@proxy1:port" > proxies.txt
echo "http://user:pass@proxy2:port" >> proxies.txt

python3 account_creator.py --accounts 10 --browsers 2 --proxies-file "proxies.txt"
```

### Output Formats

**Console Output:**
- `[+]` Success messages
- `[-]` Error messages  
- `[>]` Info messages
- `[!]` Warning messages

**CSV Export:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --csv "results/accounts.csv"
```

**JSON Summary:**
```bash
python3 account_creator.py --accounts 10 --browsers 2 --json
```

## System Requirements

- **Python 3.8+**
- **4GB+ RAM** (recommended)
- **2+ CPU cores** (recommended)
- **Internet connection**

## Troubleshooting

### Common Issues

**Playwright not installed:**
```bash
python3 system_check.py --auto-install
```

**Permission denied:**
```bash
chmod +x src/scripts/install.sh
```

**Rate limiting:**
- Use proxy rotation
- Increase delays in config
- Reduce browser count

### Performance Tips

1. **Start small:** Begin with 1-2 browsers
2. **Monitor resources:** Use `system_check.py` to analyze capabilities
3. **Use proxies:** For high-volume operations
4. **Adjust timing:** Slower = more stable, faster = more risky

## Support

- **Issues:** Open a GitHub issue
- **Documentation:** Check `docs/` folder
- **System Check:** Run `python3 system_check.py` for diagnostics

## 🛡 License 
MIT © [Coonlink](https://coonlink.com)
