#!/usr/bin/env python3

import psutil
import platform
import subprocess
import sys
import os
import argparse
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.core import config as cfg

# Import color constants and functions from config
GREEN = cfg.GREEN
RED = cfg.RED
BLUE = cfg.BLUE
YELLOW = cfg.YELLOW
CYAN = cfg.CYAN
NC = cfg.NC
cprint = cfg.cprint
cprint_auto = cfg.cprint_auto

try:
    import GPUtil
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False

def get_system_info():
    cprint("=" * 60, CYAN)
    cprint("[?] SYSTEM ANALYSIS FOR OPTIMAL NUMBER OF BROWSERS", CYAN)
    cprint("=" * 60, CYAN)
    
    cprint(f"[>] Operating System: {platform.system()} {platform.release()}", BLUE)
    cprint(f"[>] Architecture: {platform.machine()}", BLUE)
    cprint(f"[>] Python version: {sys.version.split()[0]}", BLUE)
    print()

def get_cpu_info():
    cprint("[+] CPU:", GREEN)
    cprint("-" * 30, CYAN)
    
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    
    cprint(f"[>] Physical cores: {cpu_count}", BLUE)
    cprint(f"[>] Logical cores: {cpu_count_logical}", BLUE)
    
    cpu_percent = psutil.cpu_percent(interval=1)
    cprint(f"[>] Current load: {cpu_percent}%", BLUE)
    
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        cprint(f"[>] Frequency: {cpu_freq.current:.0f} MHz (max: {cpu_freq.max:.0f} MHz)", BLUE)
    else:
        cprint("[?] Frequency: unavailable", YELLOW)
    
    print()
    return cpu_count

def get_memory_info():
    cprint("[+] MEMORY (RAM):", GREEN)
    cprint("-" * 30, CYAN)
    
    memory = psutil.virtual_memory()
    total_gb = memory.total / (1024**3)
    available_gb = memory.available / (1024**3)
    used_percent = memory.percent
    
    cprint(f"[>] Total: {total_gb:.1f} GB", BLUE)
    cprint(f"[>] Available: {available_gb:.1f} GB", BLUE)
    cprint(f"[>] Used: {used_percent:.1f}%", BLUE)
    
    if total_gb >= 16:
        memory_rating = f"{GREEN}Excellent{NC}"
    elif total_gb >= 8:
        memory_rating = f"{CYAN}Good{NC}"
    elif total_gb >= 4:
        memory_rating = f"{YELLOW}Average{NC}"
    else:
        memory_rating = f"{RED}Low{NC}"
    
    cprint(f"[>] Memory rating: {memory_rating}", BLUE)
    print()
    return total_gb

def get_gpu_info(gpus_info):
    cprint("[+] GPU:", GREEN)
    cprint("-" * 30, CYAN)
    
    if not GPU_AVAILABLE:
        cprint("[!] GPUtil is not installed - GPU information unavailable", YELLOW)
        cprint("[>] Install with: pip install GPUtil  # or run ./install.sh", BLUE)
        print()
        return

    if gpus_info:
        cprint(f"[>] GPUs detected: {len(gpus_info)}", BLUE)
        for i, gpu in enumerate(gpus_info):
            cprint(f"[>] GPU {i+1}: {gpu['name']} ({gpu['memory_total_mb']}MB)", BLUE)
    else:
        cprint("[!] No NVIDIA GPU detected or driver not installed", YELLOW)
    
    print()

def get_disk_info():
    cprint("[+] DISK SPACE:", GREEN)
    cprint("-" * 30, CYAN)
    
    disk = psutil.disk_usage('/')
    total_gb = disk.total / (1024**3)
    free_gb = disk.free / (1024**3)
    used_percent = (disk.used / disk.total) * 100
    
    cprint(f"[>] Total: {total_gb:.1f} GB", BLUE)
    cprint(f"[>] Free: {free_gb:.1f} GB", BLUE)
    cprint(f"[>] Used: {used_percent:.1f}%", BLUE)
    print()

def calculate_optimal_browsers(cpu_cores, total_memory, memory_per_browser=0.5, cpu_per_browser=0.3):
    cprint("[+] RECOMMENDATIONS:", GREEN)
    cprint("-" * 30, CYAN)
    
    max_by_memory = int(total_memory * 0.7 / memory_per_browser) if memory_per_browser > 0 else 10
    max_by_cpu = int(cpu_cores * 0.8 / cpu_per_browser) if cpu_per_browser > 0 else 10
    safe_browsers = max(1, min(max_by_memory, max_by_cpu))
    
    if total_memory >= 16 and cpu_cores >= 8:
        recommended = min(8, safe_browsers)
        rating = f"{GREEN}Excellent{NC} - you can run many browsers"
    elif total_memory >= 8 and cpu_cores >= 4:
        recommended = min(4, safe_browsers)
        rating = f"{CYAN}Good{NC} - moderate number of browsers"
    elif total_memory >= 4 and cpu_cores >= 2:
        recommended = min(2, safe_browsers)
        rating = f"{YELLOW}Average{NC} - limited number of browsers"
    else:
        recommended = 1
        rating = f"{RED}Low{NC} - only 1 browser"
    
    cprint(f"[>] Recommended browsers: {recommended}", BLUE)
    cprint(f"[>] Maximum (by resources): {safe_browsers}", BLUE)
    cprint(f"[>] System rating: {rating}", BLUE)
    

    max_possible_browsers = safe_browsers
    if total_memory >= 24 and cpu_cores >= 8:
        max_possible_browsers = max(safe_browsers, 10)
        cprint(f"[!] High-end system: you can run up to {max_possible_browsers} browsers", YELLOW)
    
    cprint("[>] COMMAND EXAMPLES:", CYAN)
    cprint("-" * 30, CYAN)

    return recommended, safe_browsers

def check_browser_requirements(auto_install=False):
    cprint("[+] BROWSER CHECK:", GREEN)
    cprint("-" * 30, CYAN)
    
    try:
        command = ['playwright.cmd', '--version'] if os.name == 'nt' else ['playwright', '--version']
        subprocess.run(command, check=True, capture_output=True, text=True, timeout=10)
        cprint("[>] Playwright is installed", BLUE)
    except Exception:
        cprint("[-] Playwright not found", RED)
        if auto_install:
            cprint("[>] Installing Playwright and Chromium...", BLUE)
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'playwright'], check=True)
                subprocess.run(['playwright', 'install-deps'], check=True)
                subprocess.run(['playwright', 'install', 'chromium'], check=True)
                cprint("[>] Playwright installed successfully", GREEN)
            except Exception as e:
                cprint(f"[-] Auto-install failed: {e}", RED)
                cprint("[>] Manual install: pip install playwright && playwright install-deps && playwright install chromium", YELLOW)
        else:
            cprint("[>] Install manually: pip install playwright && playwright install-deps && playwright install chromium", YELLOW)
    
    print()

def parse_args():
    parser = argparse.ArgumentParser(description="System analysis for optimal number of browsers")
    parser.add_argument('--memory-per-browser', type=float, default=0.5, help='GB of RAM estimated per browser')
    parser.add_argument('--cpu-per-browser', type=float, default=0.3, help='CPU cores estimated per browser')
    parser.add_argument('--accounts-per-browser', type=int, default=5, help='Accounts processed per browser instance')
    parser.add_argument('--json', action='store_true', help='Print JSON summary in addition to human-readable output')
    parser.add_argument('--auto-install', action='store_true', help='Auto-install Playwright if missing')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Pre-calculate GPU info to avoid double calls
    gpus_info = []
    if GPU_AVAILABLE:
        try:
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                gpus_info.append({"name": gpu.name, "memory_total_mb": gpu.memoryTotal})
        except Exception:
            pass
    
    try:
        get_system_info()
        cpu_cores = get_cpu_info()
        total_memory = get_memory_info()
        get_gpu_info(gpus_info)
        get_disk_info()
        check_browser_requirements(auto_install=args.auto_install)
        
        recommended, max_browsers = calculate_optimal_browsers(
            cpu_cores,
            total_memory,
            memory_per_browser=args.memory_per_browser,
            cpu_per_browser=args.cpu_per_browser
        )
        
        accounts_per_browser = max(1, args.accounts_per_browser)
        conservative_browsers = 1
        conservative_accounts = conservative_browsers * accounts_per_browser
        recommended_accounts = recommended * accounts_per_browser
        max_accounts = max_browsers * accounts_per_browser
        
        cprint("=" * 60, CYAN)
        cprint("[+] ANALYSIS COMPLETE", GREEN)
        cprint("=" * 60, CYAN)
        cprint(f"[>] Recommended: use {recommended} browser(s)", BLUE)
        cprint(f"[>] Maximum safe: {max_browsers} browser(s)", BLUE)
        print()
        cprint("[!] Start with a small number of browsers", YELLOW)
        cprint("[!] Gradually increase, monitoring system load!", YELLOW)
        cprint("[>] COMMAND EXAMPLES:", CYAN)
        cprint("-" * 30, CYAN)
        cprint(f"# Conservative mode (safe)", CYAN)
        cprint(f"python3 account_creator.py --accounts={conservative_accounts} --browsers={conservative_browsers}", BLUE)
        print()
        cprint(f"# Recommended mode", CYAN)
        cprint(f"python3 account_creator.py --accounts={recommended_accounts} --browsers={recommended}", BLUE)
        print()
        cprint(f"# Maximum mode (caution!)", CYAN)
        cprint(f"python3 account_creator.py --accounts={max_accounts} --browsers={max_browsers}", BLUE)
        print()
        
        if total_memory >= 24 and cpu_cores >= 8:
            highend_browsers = max(10, max_browsers)
            highend_accounts = highend_browsers * accounts_per_browser
            cprint(f"# High-end mode", CYAN)
            cprint(f"python3 account_creator.py --accounts={highend_accounts} --browsers={highend_browsers}", BLUE)
            print()

        if args.json:
            summary = {
                "os": {
                    "system": platform.system(),
                    "release": platform.release(),
                    "architecture": platform.machine(),
                    "python": sys.version.split()[0],
                },
                "resources": {
                    "cpu_cores_physical": psutil.cpu_count(logical=False),
                    "cpu_cores_logical": psutil.cpu_count(logical=True),
                    "cpu_load_percent": psutil.cpu_percent(interval=1),
                    "memory_total_gb": round(psutil.virtual_memory().total / (1024**3), 1),
                    "disk_total_gb": round(psutil.disk_usage('/').total / (1024**3), 1),
                },
                "gpu": gpus_info,
                "parameters": {
                    "memory_per_browser_gb": args.memory_per_browser,
                    "cpu_per_browser_core": args.cpu_per_browser,
                    "accounts_per_browser": accounts_per_browser,
                },
                "recommendations": {
                    "recommended_browsers": recommended,
                    "max_safe_browsers": max_browsers,
                    "conservative_browsers": conservative_browsers,
                    "conservative_accounts": conservative_accounts,
                    "recommended_accounts": recommended_accounts,
                    "max_accounts": max_accounts,
                }
            }
            print(json.dumps(summary, indent=2))
        
    except KeyboardInterrupt:
        cprint("\n[-] Analysis interrupted by user", RED)
    except Exception as e:
        cprint(f"\n[-] Analysis error: {e}", RED)

if __name__ == "__main__":
    main()