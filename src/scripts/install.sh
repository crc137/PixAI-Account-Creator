#!/bin/bash

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' 

echo -e "${GREEN}[+]${NC} [1/7] Updating package lists..."
sudo apt update

echo -e "${GREEN}[+]${NC} [2/7] Installing required Python packages..."
sudo apt install -y python3-pip python3-setuptools python3-venv build-essential

echo -e "${GREEN}[+]${NC} [3/7] Upgrading pip and setuptools..."
python3 -m pip install --upgrade pip setuptools wheel

echo -e "${GREEN}[+]${NC} [4/7] Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt --break-system-packages

echo -e "${BLUE}[>]${NC} [5/7] Verifying GPUtil installation..."
python3 -c "import GPUtil; print('GPUtil successfully installed:', GPUtil.getGPUs())" || echo -e "${RED}[-]${NC} GPUtil is installed, but no GPU may be detected on this machine."

echo -e "${GREEN}[+]${NC} [6/7] Installing Playwright system dependencies..."
if ! sudo -E python3 -m playwright install-deps; then
  echo -e "${RED}[-]${NC} Failed to install Playwright system deps via playwright."
  echo -e "${BLUE}[>]${NC} Falling back to installing common Chromium dependencies..."
  sudo apt install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libdrm2 \
    libgbm1 \
    libasound2t64 \
    libxshmfence1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libx11-xcb1 \
    libxkbcommon0 \
    libx11-6 \
    libxext6 \
    libxss1 \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcups2 \
    libxkbfile1 \
    libxtst6 \
    libgtk-3-0 \
    fonts-liberation \
    ca-certificates \
    wget || echo -e "${YELLOW}[!]${NC} Some fallback packages failed to install; continuing anyway."
fi

echo -e "${GREEN}[+]${NC} [7/7] Installing Playwright Chromium browser..."
python3 -m playwright install chromium

echo -e "${GREEN}[OK]${NC} Installation complete. Requirements, Playwright deps, and Chromium are ready."
