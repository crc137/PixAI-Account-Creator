<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" alt="PixAI Logo" />
  </a>
  <h1>PixAI 계정 생성기</h1>

[![English](https://img.shields.io/badge/lang-English%20🇺🇸-white)](README.md)
[![Русский](https://img.shields.io/badge/язык-Русский%20🇷🇺-white)](README.ru.md)
[![日本語](https://img.shields.io/badge/言語-日本語%20🇯🇵-white)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어%20🇰🇷-white)](README.ko.md)
[![繁體中文](https://img.shields.io/badge/語言-繁體中文%20🇹🇼-white)](README.zh-TW.md)

<img alt="last-commit" src="https://img.shields.io/github/last-commit/crc137/PixAI-Account-Creator?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="version" src="https://img.shields.io/badge/version-1.0.0-blue" style="margin: 0px 2px;">

<sub><i>스크립트를 만들었고 __~50,000__ 개의 계정을 생성했습니다. 부스팅을 위한 계정이 필요하시면 __Telegram__ 으로 메시지를 보내주세요.</i></sub>
</div>

<br />

<div align="center">
  <p>병렬 브라우저 처리로 PixAI 계정 자동 생성.</p>
  <img width="600" src="https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg" alt="터미널에서 계정 생성 데모" />
</div>

## 설치

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

> [!WARNING]  
> 설치 스크립트는 필요한 시스템 패키지와 Python 종속성을 설치하려고 시도합니다. 일부 시스템 패키지가 실패하면 root 권한으로 실행하세요.

## 사용법

```bash
# 시스템 확인
python3 system_check.py

# 계정 생성
python3 account_creator.py --accounts 10 --browsers 2

# 브라우저 미리보기
python3 preview_browser.py --headless=false
```

## 인수

| 인수             | 설명                                     | 예시                             |
|------------------|------------------------------------------|----------------------------------|
| `--accounts`     | 생성할 계정 수                           | `--accounts 10`                  |
| `--browsers`     | 병렬 브라우저 인스턴스 수                | `--browsers 2`                   |
| `--headless`     | 헤드리스 모드 (true/false)               | `--headless false`               |
| `--proxy`        | 단일 프록시 URL                          | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | 프록시 파일 (줄당 하나)                  | `--proxies-file "proxies.txt"`   |
| `--csv`          | 결과를 CSV 파일에 저장                   | `--csv "results.csv"`            |
| `--json`         | 결과를 JSON으로 출력                     | `--json`                         |

## 구성

기본값은 `src/core/config.py`에 있습니다 — 환경에 맞게 편집하세요：

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
# 기타 설정: 지연, 타임아웃, 브라우저 옵션, CAPTCHA 서비스 키 등
```

> [!TIP]  
> 속도 제한에 걸리면 지연을 늘리고 `--browsers`를 줄이세요.

## 문제 해결

**Playwright / 브라우저 문제：**

```bash
python3 system_check.py --auto-install
```

**일반적인 수정：**

- Playwright 브라우저가 설치되고 최신인지 확인.
- `--headless=false`를 사용하여 흐름을 시각적으로 디버그.
- 프록시 유효성과 형식 확인.

**속도 제한 / 계정 차단：**

- 레지덴셜 프록시 사용 (브라우저당 로테이션).
- 구성에서 랜덤 지연 증가.
- 병렬 브라우저 수 줄이기.
- 인간다운 동작 추가 (랜덤 마우스 이동, 현실적인 타이핑 지연).

## 보안 및 윤리 주의사항

이 리포지토리는 대규모 계정 생성을 자동화합니다. 대상 플랫폼의 이용 약관과 모든 적용 법률을 이해하고 준수하세요. 자동화 남용은 IP 차단, 법적 결과, 계정 종료로 이어질 수 있습니다.

## 요구사항

- Python 3.8+
- Playwright (설치 스크립트 또는 `pip`로 설치)
- 4GB+ RAM (권장)
- 2+ CPU 코어 (권장)

## 라이선스

MIT © [Coonlink](https://coonlink.com)
