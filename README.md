<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" alt="PixAI Logo" />
  </a>
  <h1>PixAI Account Creator</h1>

[![English](https://img.shields.io/badge/lang-English%20🇺🇸-white)](README.md)
[![Русский](https://img.shields.io/badge/язык-Русский%20🇷🇺-white)](README.ru.md)
[![日本語](https://img.shields.io/badge/言語-日本語%20🇯🇵-white)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어%20🇰🇷-white)](README.ko.md)
[![繁體中文](https://img.shields.io/badge/語言-繁體中文%20🇹🇼-white)](README.zh-TW.md)

<img alt="last-commit" src="https://img.shields.io/github/last-commit/crc137/PixAI-Account-Creator?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="version" src="https://img.shields.io/badge/version-1.0.0-blue" style="margin: 0px 2px;">

<sub><i>I've built a script and created ___~50,000___ accounts. If you need accounts for boosting, message me on ___Telegram___. </i></sub>
</div>

<br />

<div align="center">
  <p>Automated PixAI account creation with parallel browser processing.</p>
  <img width="600" src="https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg" alt="Demo of account creation in terminal" />
</div>

## Install

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

> [!WARNING]  
> The installer script attempts to install required system packages and Python dependencies. Run it with root privileges if some system packages fail.

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

| Argument          | Description                              | Example                          |
|-------------------|------------------------------------------|----------------------------------|
| `--accounts`      | Number of accounts to create             | `--accounts 10`                  |
| `--browsers`      | Number of parallel browser instances     | `--browsers 2`                   |
| `--headless`      | Headless mode (true/false)               | `--headless false`               |
| `--proxy`         | Single proxy URL                         | `--proxy "http://user:pass@host:port"` |
| `--proxies-file`  | File with proxies (one per line)         | `--proxies-file "proxies.txt"`   |
| `--csv`           | Save results to CSV file                 | `--csv "results.csv"`            |
| `--json`          | Output results as JSON                   | `--json`                         |

## Configuration

Defaults live in `src/core/config.py` — edit to fit your environment:

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
# other settings: delays, timeouts, browser options, captcha-service keys, etc.
```

> [!TIP]  
> If you run into rate-limiting, increase delays and reduce `--browsers`.

## Troubleshooting

**Playwright / browser issues:**

```bash
python3 system_check.py --auto-install
```

**Common fixes:**

- Ensure Playwright browsers are installed and up-to-date.
- Use `--headless=false` to visually debug flows.
- Check proxy validity and format.

**Rate limiting / account blocks:**

- Use residential proxies (rotate per browser).
- Increase random delays in config.
- Lower the number of parallel browsers.
- Add human-like behaviors (random mouse movement, realistic typing delays).

## Security & Ethics Note

This repository automates account creation at scale. Make sure you understand and comply with the Terms of Service of the target platform and all applicable laws. Abuse of automation can lead to IP bans, legal consequences, and account termination.

### Recommended Settings by System
- **Low-end (4GB RAM, 2 cores)**: 1-2 browsers, 2-5 accounts each
- **Mid-range (8GB RAM, 4 cores)**: 2-4 browsers, 5-10 accounts each
- **High-end (16GB+ RAM, 8+ cores)**: 4-8 browsers, 10-20 accounts each

### Performance Tips
- Use SSD storage for better I/O performance
- Close unnecessary applications during account creation
- Monitor system resources with `htop` or Task Manager
- Use quality residential proxies

### Minimum Requirements
- **Python**: 3.8+
- **RAM**: 4GB+ (recommended)
- **CPU**: 2+ cores (recommended)
- **OS**: Linux, macOS, Windows
- **Playwright** (installed via installer script or `pip`)

### Recommended for High Performance
- **RAM**: 16GB+
- **CPU**: 8+ cores
- **Storage**: SSD recommended
- **Network**: Stable internet connection

## Future Roadmap

### Planned Features
- [ ] CAPTCHA solving integration
- [ ] Advanced proxy management
- [ ] Account verification workflows
- [ ] Database integration for account storage
- [ ] Web dashboard for monitoring
- [ ] Docker containerization
- [ ] Cloud deployment support
- [ ] Telegram integration
- [ ] Discord integration

## License

MIT © [Coonlink](https://coonlink.com)
