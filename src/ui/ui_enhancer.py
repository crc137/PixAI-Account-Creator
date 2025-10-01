#!/usr/bin/env python3

import os
import requests
from typing import Optional
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core import config as cfg
import asyncio

GREEN = getattr(cfg, "GREEN", '\033[0;32m')
RED = getattr(cfg, "RED", '\033[0;31m')
BLUE = getattr(cfg, "BLUE", '\033[0;34m')
YELLOW = getattr(cfg, "YELLOW", '\033[0;33m')
CYAN = getattr(cfg, "CYAN", '\033[0;36m')
NC = getattr(cfg, "NC", '\033[0m')

class UIEnhancer:

    def __init__(self):
        self.logo_svg_url = cfg.LOGO_SVG_URL
        self.logo_ico_url = cfg.LOGO_ICO_URL
        self.font_phonk_url = cfg.FONT_PHONK_URL
        self.font_gilroy_medium_url = cfg.FONT_GILROY_MEDIUM_URL
        self.font_gilroy_semibold_url = cfg.FONT_GILROY_SEMIBOLD_URL
        self.font_gilroy_extrabold_url = cfg.FONT_GILROY_EXTRABOLD_URL
        self.font_hanson_url = cfg.FONT_HANSON_URL
        self.project_url = cfg.PROJECT_URL
        self.author = cfg.AUTHOR
        self.title = cfg.TITLE
        self.version = cfg.VERSION_STRING

    async def enhance_page(self, page) -> bool:
        try:
            await page.wait_for_load_state('load')
            await self._set_fonts(page)
            await self._set_logo(page)
            await self._set_title(page)
            await asyncio.sleep(0.3)
            await self._add_author_credit(page)
            await asyncio.sleep(1)
            await page.evaluate(f"document.title = '{self.title}';")
            
            return True
        except Exception as e:
            print(f"{RED}[-] UI Enhancement failed: {e}{NC}")
            return False

    async def _set_fonts(self, page) -> None:
        try:
            await page.evaluate(f"""
                const fontStyle = document.createElement('style');
                fontStyle.textContent = `
                    @font-face {{
                        font-family: 'PhonkSans';
                        src: url('{self.font_phonk_url}') format('woff');
                        font-weight: 900;
                        font-style: normal;
                        font-display: swap;
                    }}
                    @font-face {{
                        font-family: 'Gilroy';
                        src: url('{self.font_gilroy_medium_url}') format('woff');
                        font-weight: 500;
                        font-style: normal;
                        font-display: swap;
                    }}
                    @font-face {{
                        font-family: 'Gilroy';
                        src: url('{self.font_gilroy_semibold_url}') format('woff');
                        font-weight: 600;
                        font-style: normal;
                        font-display: swap;
                    }}
                    @font-face {{
                        font-family: 'Gilroy';
                        src: url('{self.font_gilroy_extrabold_url}') format('woff');
                        font-weight: 800;
                        font-style: normal;
                        font-display: swap;
                    }}
                    @font-face {{
                        font-family: 'Hanson';
                        src: url('{self.font_hanson_url}') format('woff');
                        font-weight: 700;
                        font-style: normal;
                        font-display: swap;
                    }}
                `;
                document.head.appendChild(fontStyle);
                
                console.log('{GREEN}Custom fonts loaded: PhonkSans, Gilroy (Medium/SemiBold/ExtraBold), Hanson{NC}');
            """)
            print(f"{GREEN}[+] Custom fonts loaded: PhonkSans, Gilroy (Medium/SemiBold/ExtraBold), Hanson{NC}")
        except Exception as e:
            print(f"{RED}[-] Font loading failed: {e}{NC}")

    async def _set_logo(self, page) -> None:
        try:
            await page.evaluate("""
                const oldFavicons = document.querySelectorAll('link[rel="icon"], link[rel="shortcut icon"]');
                oldFavicons.forEach(link => link.remove());
            """)
            
            svg_content = await self._download_logo(self.logo_svg_url)
            if svg_content:
                import urllib.parse
                encoded_svg = urllib.parse.quote(svg_content)
                await page.evaluate(f"""
                    let link = document.createElement('link');
                    link.rel = 'icon';
                    link.type = 'image/svg+xml';
                    link.href = 'data:image/svg+xml,{encoded_svg}';
                    document.head.appendChild(link);
                """)
                print(f"{GREEN}[+] SVG logo loaded{NC}")
                return

            ico_content = await self._download_logo(self.logo_ico_url)
            if ico_content:
                await page.evaluate(f"""
                    let link = document.createElement('link');
                    link.rel = 'icon';
                    link.type = 'image/x-icon';
                    link.href = 'data:image/x-icon;base64,{ico_content}';
                    document.head.appendChild(link);
                """)
                print(f"{GREEN}[+] ICO logo loaded{NC}")
                return

            await page.evaluate("""
                let link = document.createElement('link');
                link.rel = 'icon';
                link.type = 'image/svg+xml';
                link.href = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">🎨</text></svg>';
                document.head.appendChild(link);
            """)
            print(f"{GREEN}[+] Fallback emoji logo set{NC}")
        except Exception as e:
            print(f"{RED}[-] Logo setting failed: {e}{NC}")

    async def _download_logo(self, url: str) -> Optional[str]:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                if url.endswith('.svg'):
                    return response.text
                else:
                    import base64
                    return base64.b64encode(response.content).decode('utf-8')
        except Exception as e:
            print(f"{RED}[-] Failed to download logo from {url}: {e}{NC}")
        return None

    async def _set_title(self, page) -> None:
        try:
            for attempt in range(3):
                await page.evaluate("""
                    const titles = document.querySelectorAll('title');
                    titles.forEach(title => title.remove());
                """)
                
                await page.evaluate(f"""
                    const newTitle = document.createElement('title');
                    newTitle.textContent = '{self.title}';
                    document.head.appendChild(newTitle);
                """)
                
                await page.evaluate(f"document.title = '{self.title}';")
                
                await page.evaluate(f"""
                    if (document.title !== '{self.title}') {{
                        document.title = '{self.title}';
                        const titleEl = document.querySelector('title');
                        if (titleEl) titleEl.textContent = '{self.title}';
                    }}
                """)
                
                current_title = await page.evaluate("document.title")
                if current_title == self.title:
                    print(f"{GREEN}[+] Page title successfully changed to: {self.title}{NC}")
                    return
                
                await asyncio.sleep(0.5)
            
            print(f"{YELLOW}[!] Title change partially successful: {current_title}{NC}")
        except Exception as e:
            print(f"{RED}[-] Title change failed: {e}{NC}")

    async def _add_author_credit(self, page) -> None:
        try:
            await page.wait_for_load_state('domcontentloaded')
            
            await asyncio.sleep(1)
            
            await page.evaluate(f"""
                document.querySelectorAll('.pixai-credit, .pixai-title').forEach(e => e.remove());

                const style = document.createElement('style');
                style.textContent = `
                    @keyframes fadeIn {{
                        from {{opacity: 0; transform: translateY(10px);}}
                        to {{opacity: 1; transform: translateY(0);}}
                    }}
                    .pixai-credit {{
                        position: fixed;
                        bottom: 5rem;
                        right: 5rem;
                        background: rgba(136, 104, 255, 0.2);
                        color: #fff;
                        font-weight: bold;
                        font-family: Gilroy, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
                        border: 1px solid rgba(136, 104, 255, 0.3);
                        padding: 8px 12px;
                        height: 32px;
                        border-radius: 8px;
                        font-size: 12px;
                        display: flex;
                        flex-direction: row-reverse;
                        align-items: center;
                        justify-content: center;
                        gap: 6px;
                        backdrop-filter: blur(8px);
                        box-shadow: 0 4px 12px rgba(136, 104, 255, 0.15);
                        transition: all 0.3s ease;
                        animation: fadeIn 0.6s ease forwards;
                        z-index: 999999;
                    }}
                    .pixai-credit:hover {{
                        background: rgba(136, 104, 255, 0.3);
                        transform: translateY(-2px);
                        box-shadow: 0 6px 16px rgba(136, 104, 255, 0.25);
                    }}
                    .pixai-credit a {{
                        color: #fff;
                        text-decoration: underline;
                        font-weight: bold;
                        opacity: 0.9;
                    }}
                    .pixai-credit a:hover {{
                        text-decoration: none;
                        opacity: 1;
                    }}
                    .pixai-title {{
                        position: fixed;
                        top: 1rem;
                        left: 1rem;
                        display: flex;
                        align-items: center;
                        gap: 10px;
                        font-size: 1.5rem;
                        font-weight: 700;
                        font-family: Hanson, Phonk Sans, Dela Gothic One, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
                        color: #222;
                        text-shadow: 0 2px 4px rgba(255,255,255,0.8);
                        animation: fadeIn 0.8s ease forwards;
                        z-index: 999999;
                        background: rgba(255,255,255,0.9);
                        padding: 8px 16px;
                        border-radius: 12px;
                        backdrop-filter: blur(6px);
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                        border: 1px solid rgba(255,255,255,0.3);
                    }}
                    .pixai-title img {{
                        width: 1.5rem;
                        height: 1.5rem;
                        object-fit: contain;
                        border-radius: 6px;
                        transition: transform 0.3s ease;
                        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));
                    }}
                    .pixai-title img:hover {{
                        transform: scale(1.1);
                    }}
                `;
                document.head.appendChild(style);

                const titleDiv = document.createElement('div');
                titleDiv.className = 'pixai-title';
                titleDiv.innerHTML = `
                    <img src="{self.logo_svg_url}" alt="Logo">
                    <span>{self.title}</span>
                `;
                document.body.appendChild(titleDiv);

                const credit = document.createElement('div');
                credit.className = 'pixai-credit';
                credit.innerHTML = `
                    <a href="{self.project_url}" target="_blank">GitHub</a>
                    <span>{self.author} {self.version}</span>
                `;
                document.body.appendChild(credit);
                
                console.log('{GREEN}PixAI UI elements added successfully{NC}');
            """)
            print(f"{GREEN}[+] Modern title and author added{NC}")
        except Exception as e:
            print(f"{RED}[-] Adding modern UI failed: {e}{NC}")

    async def remove_enhancements(self, page) -> None:
        try:
            await page.evaluate("""
                document.querySelectorAll('link[rel="icon"]').forEach(l => l.remove());
                const credit = document.querySelector('.pixai-credit');
                if (credit) credit.remove();
                document.querySelectorAll('style').forEach(s => {
                    if (s.textContent.includes('pixai-credit')) s.remove();
                });
            """)
            print(f"{GREEN}[+] UI enhancements removed{NC}")
        except Exception as e:
            print(f"{RED}[-] Failed to remove enhancements: {e}{NC}")

ui_enhancer = UIEnhancer()
