# PixAI Account Creator

A system for automatically creating PixAI accounts.

## Installation

### 1. Download the files

Copy the project folder to your computer.

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Check your system (recommended)

```bash
python3 system_check.py
```

This script will show the optimal number of browsers for your machine.

### 4. Configure the script

Open `account_creator.py` and adjust the settings at the top:

```python
# Settings
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"  # Your server API
HEADLESS = False  # True = headless mode, False = visible browser
BROWSER_ARGS = ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
EMAIL_DOMAIN = "coonlink.com"  # Your email domain
```

## Usage

```bash
python3 account_creator.py --accounts=10 --browsers=2
```

**Parameters:**

* `--accounts=N` — number of accounts to create
* `--browsers=M` — number of browsers (parallel sessions)

**Examples:**

```bash
# Create 5 accounts with 1 browser
python3 account_creator.py --accounts=5 --browsers=1

# Create 20 accounts with 3 browsers
python3 account_creator.py --accounts=20 --browsers=3
```

## Configuration

You can edit the following in `account_creator.py`:

* **API_URL** — server endpoint to send account data
* **HEADLESS** — browser mode (True/False)
* **EMAIL_DOMAIN** — domain used for email generation
* **BROWSER_ARGS** — extra browser arguments

## How it works

1. The script registers new accounts on PixAI
2. Sends the account data to your server
3. The server stores them in the database
4. Creation statistics are displayed

## Requirements

* Python 3.7+
* Internet connection
* API server access
