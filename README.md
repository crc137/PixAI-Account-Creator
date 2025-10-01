<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" />
  </a>
  <h1>PixAI Account Creator</h1>
</div>

Automated PixAI account creation with parallel browser processing.

![PixAI](https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg)

## Install

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

## Usage

```bash
# Check system
python3 system_check.py

# Create accounts
python3 account_creator.py --accounts 10 --browsers 2

# Preview browser
python3 preview_browser.py --headless=false
```

## Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--accounts` | Number of accounts | `--accounts 10` |
| `--browsers` | Parallel browsers | `--browsers 2` |
| `--headless` | Headless mode | `--headless false` |
| `--proxy` | Single proxy | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | Proxy file | `--proxies-file "proxies.txt"` |
| `--csv` | Save to CSV | `--csv "results.csv"` |
| `--json` | JSON output | `--json` |

## Configuration

Edit `src/core/config.py` for defaults:

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
```

## Troubleshooting

**Playwright issues:**
```bash
python3 system_check.py --auto-install
```

**Rate limiting:**
- Use proxies
- Increase delays in config
- Reduce browser count

## Requirements

- Python 3.8+
- 4GB+ RAM
- 2+ CPU cores

## License

MIT © [Coonlink](https://coonlink.com)
