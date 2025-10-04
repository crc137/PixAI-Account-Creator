<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" alt="PixAI Logo" />
  </a>
  <h1>PixAI アカウントクリエーター</h1>

[![English](https://img.shields.io/badge/lang-English%20🇺🇸-white)](README.md)
[![Русский](https://img.shields.io/badge/язык-Русский%20🇷🇺-white)](README.ru.md)
[![日本語](https://img.shields.io/badge/言語-日本語%20🇯🇵-white)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어%20🇰🇷-white)](README.ko.md)
[![繁體中文](https://img.shields.io/badge/語言-繁體中文%20🇹🇼-white)](README.zh-TW.md)

<img alt="last-commit" src="https://img.shields.io/github/last-commit/crc137/PixAI-Account-Creator?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="version" src="https://img.shields.io/badge/version-1.0.0-blue" style="margin: 0px 2px;">

<sub><i>スクリプトを作成し、約___50,000___のアカウントを作成しました。ブースト用のアカウントが必要な場合は、___Telegram___で私にメッセージを送ってください。</i>
</div>

<br />

<div align="center">
  <p>並列ブラウザ処理によるPixAIアカウントの自動作成。</p>
  <img width="600" src="https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg" alt="ターミナルでのアカウント作成デモ" />
</div>

## インストール

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

> [!WARNING]  
> インストーラースクリプトは、必要なシステムパッケージとPython依存関係をインストールしようとします。一部のシステムパッケージが失敗した場合、root権限で実行してください。

## 使用方法

```bash
# システムチェック
python3 system_check.py

# アカウント作成
python3 account_creator.py --accounts 10 --browsers 2

# ブラウザプレビュー
python3 preview_browser.py --headless=false
```

## 引数

| 引数             | 説明                                     | 例                               |
|------------------|------------------------------------------|----------------------------------|
| `--accounts`     | 作成するアカウント数                     | `--accounts 10`                  |
| `--browsers`     | 並列ブラウザインスタンス数               | `--browsers 2`                   |
| `--headless`     | ヘッドレスモード (true/false)            | `--headless false`               |
| `--proxy`        | 単一のプロキシURL                        | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | プロキシファイル (1行に1つ)              | `--proxies-file "proxies.txt"`   |
| `--csv`          | 結果をCSVファイルに保存                  | `--csv "results.csv"`            |
| `--json`         | 結果をJSONとして出力                     | `--json`                         |

## 設定

デフォルト値は `src/core/config.py` にあります — 環境に合わせて編集してください：

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
# その他の設定: 遅延、タイムアウト、ブラウザオプション、CAPTCHAサービスキーなど
```

> [!TIP]  
> レートリミットに遭遇した場合、遅延を増やし、`--browsers` を減らしてください。

## トラブルシューティング

**Playwright / ブラウザの問題：**

```bash
python3 system_check.py --auto-install
```

**一般的な修正：**

- Playwrightブラウザがインストールされ、最新であることを確認。
- `--headless=false` を使用してフローを視覚的にデバッグ。
- プロキシの有効性と形式を確認。

**レートリミット / アカウントブロック：**

- レジデンシャルプロキシを使用（ブラウザごとにローテーション）。
- 設定でランダム遅延を増やす。
- 並列ブラウザ数を下げる。
- 人間らしい動作を追加（ランダムマウス移動、現実的なタイピング遅延）。

## セキュリティと倫理に関する注意

このリポジトリは、大規模なアカウント作成を自動化します。対象プラットフォームの利用規約とすべての適用法を理解し、遵守してください。自動化の乱用はIPバン、法的結果、アカウント終了につながる可能性があります。

## 要件

- Python 3.8+
- Playwright (インストーラースクリプトまたは `pip` でインストール)
- 4GB+ RAM (推奨)
- 2+ CPUコア (推奨)

## ライセンス

MIT © [Coonlink](https://coonlink.com)
