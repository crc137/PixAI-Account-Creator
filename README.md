# PixAI-Account-Creator

Welcome to PixAI-Account-Creator, your go-to Python automation tool for effortlessly generating multiple accounts on the PixAI platform!
Streamline your account provisioning process, integrate new accounts with external systems, and save valuable time.

## Features

This project is packed with features designed to make mass account creation a breeze:
*  **Automated Account Registration:** Leverages `Playwright` for robust browser automation, handling PixAI's registration flow from start to finish, supporting both headless (background) and visible browser modes.
*  **Parallel Processing:** Significantly speeds up creation by concurrently registering accounts across multiple browser instances. Configure the number of parallel operations to match your system's capabilities.
*  **Dynamic Credential Generation:** Automatically generates unique email addresses (using a configurable domain) and strong, secure passwords for every new account.
*  **External API Integration:** Seamlessly sends newly created account credentials (email and password) via HTTP POST requests to a user-defined API endpoint, enabling easy integration with your external systems or databases.
*  **System Performance Analysis:** Includes a dedicated `system_check.py` script that analyzes your host machine's CPU, RAM, and GPU to recommend the optimal number of parallel browser instances for maximum efficiency.
*  **Highly Configurable:** Easily customize key operational parameters such as the external API URL, headless browser mode, email domain, and additional browser arguments directly within the script.
*  **Robust Error Handling:** Incorporates basic error handling and retry mechanisms to enhance stability and ensure smoother operation against transient website issues.

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
2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Playwright Browser Binaries:**
    Playwright requires browser binaries (like Chromium, Firefox, WebKit). Install them with:
    ```bash
    playwright install
    ```

### Configuration (Required)

Before running, you **MUST** configure the following settings in the `account_creator.py` script:

```python
# Настройки
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"  # YOUR API URL
HEADLESS = False  # True - headless, False - visible browser
BROWSER_ARGS = ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
EMAIL_DOMAIN = "your-domain.com"  # Your domain for email generation
```

**Important Settings:**
*   `API_URL`: **REQUIRED** - Your external API endpoint for receiving account data
*   `HEADLESS`: Set to `False` to watch the browser automation in action
*   `EMAIL_DOMAIN`: The domain for generated email addresses

### Running the Creator

1.  **Check System Performance (Recommended First Step):**
    Run the `system_check.py` script to get recommendations for optimal parallel browser instances based on your hardware:
    ```bash
    python system_check.py
    ```
    This will help you configure the `--parallel` argument efficiently.

2.  **Execute the Account Creator:**
    Run the `account_creator.py` script from your terminal. You can specify the number of accounts to create and the number of parallel browser instances using command-line arguments:

    ```bash
    # Example: Create 10 accounts using 2 parallel browser instances
    python account_creator.py --accounts=10 --browsers=2

    # Example: Create 5 accounts with 1 browser
    python account_creator.py --accounts=5 --browsers=1
    ```
    
    **Command Parameters:**
    *   `--accounts=N`: The total number of PixAI accounts to create
    *   `--browsers=N`: The number of browser instances to run concurrently
    
    **Important:** Make sure you have configured the `API_URL` in the script before running, otherwise accounts won't be saved to your server!
