<div align="center">
  <a href="https://github.com/coonlink">
    <img width="90px" src="https://raw.coonlink.com/cloud/PixAI Daily/logo.svg" alt="PixAI Logo" />
  </a>
  <h1>Создатель аккаунтов PixAI</h1>

[![English](https://img.shields.io/badge/lang-English%20🇺🇸-white)](README.md)
[![Русский](https://img.shields.io/badge/язык-Русский%20🇷🇺-white)](README.ru.md)
[![日本語](https://img.shields.io/badge/言語-日本語%20🇯🇵-white)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어%20🇰🇷-white)](README.ko.md)
[![繁體中文](https://img.shields.io/badge/語言-繁體中文%20🇹🇼-white)](README.zh-TW.md)

<img alt="last-commit" src="https://img.shields.io/github/last-commit/crc137/PixAI-Account-Creator?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/crc137/PixAI-Account-Creator?style=flat&amp;color=0080ff" style="margin: 0px 2px;">
<img alt="version" src="https://img.shields.io/badge/version-1.0.0-blue" style="margin: 0px 2px;">

<sub><i>Я создал скрипт и зарегистрировал ___~50,000___ аккаунтов. Если вам нужны аккаунты для бустинга, напишите мне в ___Telegram___. </i></sub>
</div>

<br />

<div align="center">
  <p>Автоматизированное создание аккаунтов PixAI с параллельной обработкой браузеров.</p>
  <img width="600" src="https://raw.coonlink.com/cloud/photo_5974064291013316193_x.jpg" alt="Демо создания аккаунтов в терминале" />
</div>

## Установка

```bash
git clone https://github.com/crc137/PixAI-Account-Creator.git
cd PixAI-Account-Creator
chmod +x src/scripts/install.sh
./src/scripts/install.sh
```

> [!WARNING]  
> Скрипт установки пытается установить необходимые системные пакеты и зависимости Python. Запустите его с правами root, если некоторые системные пакеты не устанавливаются.

## Использование

```bash
# Проверка системы
python3 system_check.py

# Создание аккаунтов
python3 account_creator.py --accounts 10 --browsers 2

# Предварительный просмотр браузера
python3 preview_browser.py --headless=false
```

## Аргументы

| Аргумент         | Описание                                 | Пример                           |
|------------------|------------------------------------------|----------------------------------|
| `--accounts`     | Количество аккаунтов для создания        | `--accounts 10`                  |
| `--browsers`     | Количество параллельных экземпляров браузера | `--browsers 2`               |
| `--headless`     | Режим headless (true/false)              | `--headless false`               |
| `--proxy`        | URL одного прокси                        | `--proxy "http://user:pass@host:port"` |
| `--proxies-file` | Файл с прокси (по одному на строку)      | `--proxies-file "proxies.txt"`   |
| `--csv`          | Сохранить результаты в CSV-файл          | `--csv "results.csv"`            |
| `--json`         | Вывести результаты в формате JSON        | `--json`                         |

## Конфигурация

Значения по умолчанию находятся в `src/core/config.py` — отредактируйте их под вашу среду:

```python
API_URL = "https://pixai.coonlink.com/api/v1/boostlikes/accountcreator-add"
EMAIL_DOMAIN = "coonlink.com"
HEADLESS = False
# другие настройки: задержки, таймауты, опции браузера, ключи сервиса капчи и т.д.
```

> [!TIP]  
> Если вы сталкиваетесь с ограничением по скорости, увеличьте задержки и уменьшите `--browsers`.

## Устранение неисправностей

**Проблемы с Playwright / браузером:**

```bash
python3 system_check.py --auto-install
```

**Общие исправления:**

- Убедитесь, что браузеры Playwright установлены и обновлены.
- Используйте `--headless=false` для визуальной отладки потоков.
- Проверьте валидность и формат прокси.

**Ограничение по скорости / блокировка аккаунтов:**

- Используйте резидентные прокси (ротация на браузер).
- Увеличьте случайные задержки в конфигурации.
- Уменьшите количество параллельных браузеров.
- Добавьте поведение, похожее на человеческое (случайные движения мыши, реалистичные задержки печати).

## Примечание по безопасности и этике

Этот репозиторий автоматизирует создание аккаунтов в большом масштабе. Убедитесь, что вы понимаете и соблюдаете Условия использования целевой платформы и все применимые законы. Злоупотребление автоматизацией может привести к блокировке IP, юридическим последствиям и удалению аккаунтов.

## Требования

- Python 3.8+
- Playwright (устанавливается через скрипт установки или `pip`)
- 4 ГБ+ ОЗУ (рекомендуется)
- 2+ ядра CPU (рекомендуется)

## Лицензия

MIT © [Coonlink](https://coonlink.com)
