<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" alt="PixAI Logo" />
  </a>
  <h1>PixAI 帳戶建立器</h1>

[![English](https://img.shields.io/badge/lang-English%20🇺🇸-white)](README.md)
[![Русский](https://img.shields.io/badge/язык-Русский%20🇷🇺-white)](README.ru.md)
[![日本語](https://img.shields.io/badge/言語-日本語%20🇯🇵-white)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어%20🇰🇷-white)](README.ko.md)
[![繁體中文](https://img.shields.io/badge/語言-繁體中文%20🇹🇼-white)](README.zh-TW.md)

<i>我建立了一個腳本並創建了約 50,000 個帳戶。如果您需要用於提升的帳戶，請在 Telegram 上訊息我。</i>
</div>

<br />

<div align="center">
  <p>使用並行瀏覽器處理自動建立 PixAI 帳戶。</p>
  <img width="600" src="https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg" alt="終端機中帳戶建立示範" />
</div>

## 安裝

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

> [!WARNING]  
> 安裝腳本會嘗試安裝所需的系統套件和 Python 依賴項。如果某些系統套件失敗，請以 root 權限執行。

## 使用方法

```bash
# 系統檢查
python3 system_check.py

# 建立帳戶
python3 account_creator.py --accounts 10 --browsers 2

# 瀏覽器預覽
python3 preview_browser.py --headless=false
```

## 參數

| 參數             | 描述                                     | 範例                             |
|------------------|------------------------------------------|----------------------------------|
| `--accounts`     | 要建立的帳戶數量                         | `--accounts 10`                  |
| `--browsers`     | 並行瀏覽器實例數量                       | `--browsers 2`                   |
| `--headless`     | 無頭模式 (true/false)                    | `--headless false`               |
| `--proxy`        | 單一代理 URL                             | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | 代理檔案 (每行一個)                      | `--proxies-file "proxies.txt"`   |
| `--csv`          | 將結果儲存至 CSV 檔案                    | `--csv "results.csv"`            |
| `--json`         | 以 JSON 格式輸出結果                     | `--json`                         |

## 設定

預設值位於 `src/core/config.py` — 請依環境編輯：

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
# 其他設定：延遲、逾時、瀏覽器選項、CAPTCHA 服務金鑰等
```

> [!TIP]  
> 如果遇到速率限制，請增加延遲並減少 `--browsers`。

## 疑難排解

**Playwright / 瀏覽器問題：**

```bash
python3 system_check.py --auto-install
```

**常見修正：**

- 確保 Playwright 瀏覽器已安裝且為最新版本。
- 使用 `--headless=false` 以視覺方式偵錯流程。
- 檢查代理有效性和格式。

**速率限制 / 帳戶封鎖：**

- 使用住宅代理 (每個瀏覽器輪換)。
- 在設定中增加隨機延遲。
- 降低並行瀏覽器數量。
- 新增類似人類的行為 (隨機滑鼠移動、現實打字延遲)。

## 安全與倫理注意事項

此儲存庫自動化大規模帳戶建立。請確保了解並遵守目標平台的服務條款及所有適用法律。濫用自動化可能導致 IP 封鎖、法律後果及帳戶終止。

## 需求

- Python 3.8+
- Playwright (透過安裝腳本或 `pip` 安裝)
- 4GB+ RAM (建議)
- 2+ CPU 核心 (建議)

## 授權

MIT © [Coonlink](https://coonlink.com)
