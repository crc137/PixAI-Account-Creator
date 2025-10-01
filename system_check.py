#!/usr/bin/env python3

import psutil
import platform
import subprocess
import sys
import os

try:
    import GPUtil
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False

def get_system_info():
    print("=" * 60)
    print("[?] SYSTEM ANALYSIS FOR OPTIMAL NUMBER OF BROWSERS")
    print("=" * 60)
    
    print(f"[>] Operating System: {platform.system()} {platform.release()}")
    print(f"[>] Architecture: {platform.machine()}")
    print(f"[>] Python version: {sys.version.split()[0]}")
    print()

def get_cpu_info():
    print("[+] CPU:")
    print("-" * 30)
    
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    
    print(f"[>] Physical cores: {cpu_count}")
    print(f"[>] Logical cores: {cpu_count_logical}")
    
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"[>] Current load: {cpu_percent}%")
    
    try:
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            print(f"[>] Frequency: {cpu_freq.current:.0f} MHz (max: {cpu_freq.max:.0f} MHz)")
    except:
        print("[?] Frequency: unavailable")
    
    print()
    return cpu_count

def get_memory_info():
    print("[+] MEMORY (RAM):")
    print("-" * 30)
    
    memory = psutil.virtual_memory()
    total_gb = memory.total / (1024**3)
    available_gb = memory.available / (1024**3)
    used_percent = memory.percent
    
    print(f"[>] Total: {total_gb:.1f} GB")
    print(f"[>] Available: {available_gb:.1f} GB")
    print(f"[>] Used: {used_percent:.1f}%")
    
    if total_gb >= 16:
        memory_rating = "Excellent"
    elif total_gb >= 8:
        memory_rating = "Good"
    elif total_gb >= 4:
        memory_rating = "Average"
    else:
        memory_rating = "Low"
    
    print(f"[>] Memory rating: {memory_rating}")
    print()
    return total_gb

def get_gpu_info():
    print("[+] GPU:")
    print("-" * 30)
    
    if not GPU_AVAILABLE:
        print("GPUtil не установлен - информация о GPU недоступна")
        print("Для полной информации установите: pip install GPUtil")
        print()
        return
    
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            for i, gpu in enumerate(gpus):
                print(f"[>] GPU {i+1}: {gpu.name}")
                print(f"[>] Memory: {gpu.memoryUsed}MB / {gpu.memoryTotal}MB")
                print(f"[>] Load: {gpu.load * 100:.1f}%")
                print(f"[>] Temperature: {gpu.temperature}°C")
        else:
            print("[-] No GPU found or not supported")
    except Exception as e:
        print(f"[-] Error getting GPU info: {e}")
        print("[?] Maybe nvidia-ml-py is not installed")
    
    print()

def get_disk_info():
    print("[+] DISK SPACE:")
    print("-" * 30)
    
    disk = psutil.disk_usage('/')
    total_gb = disk.total / (1024**3)
    free_gb = disk.free / (1024**3)
    used_percent = (disk.used / disk.total) * 100
    
    print(f"[>] Total: {total_gb:.1f} GB")
    print(f"[>] Free: {free_gb:.1f} GB")
    print(f"[>] Used: {used_percent:.1f}%")
    print()

def calculate_optimal_browsers(cpu_cores, total_memory):
    print("[+] RECOMMENDATIONS:")
    print("-" * 30)
    
    memory_per_browser = 0.5
    cpu_per_browser = 0.3
    
    max_by_memory = int(total_memory * 0.7 / memory_per_browser)
    max_by_cpu = int(cpu_cores * 0.8 / cpu_per_browser)
    safe_browsers = min(max_by_memory, max_by_cpu, 10)
    
    if total_memory >= 16 and cpu_cores >= 8:
        recommended = min(8, safe_browsers)
        rating = "Excellent - you can run many browsers"
    elif total_memory >= 8 and cpu_cores >= 4:
        recommended = min(4, safe_browsers)
        rating = "Good - moderate number of browsers"
    elif total_memory >= 4 and cpu_cores >= 2:
        recommended = min(2, safe_browsers)
        rating = "Average - limited number of browsers"
    else:
        recommended = 1
        rating = "Low - only 1 browser"
    
    print(f"[>] Recommended browsers: {recommended}")
    print(f"[>] Maximum (by resources): {safe_browsers}")
    print(f"[>] System rating: {rating}")
    print(f"[?] If you have 24GB+ and 8+ cores, you can run 8 browsers")
    
    print("[>] COMMAND EXAMPLES:")
    print("-" * 30)
    print(f"# Conservative mode (safe)")
    print(f"python3 account_creator.py --accounts=10 --browsers=1")
    print()
    print(f"# Recommended mode")
    print(f"python3 account_creator.py --accounts=20 --browsers={recommended}")
    print()
    print(f"# Maximum mode (caution!)")
    print(f"python3 account_creator.py --accounts=50 --browsers={safe_browsers}")
    print()
    
    return recommended, safe_browsers

def check_browser_requirements():
    print("[+] BROWSER CHECK:")
    print("-" * 30)
    
    try:
        result = subprocess.run(['playwright', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"[>] Playwright installed: {result.stdout.strip()}")
        else:
            print("[-] Playwright not found")
            print("[>] Install: pip install playwright && playwright install chromium")
    except Exception as e:
        print(f"[-] Error checking Playwright: {e}")
    
    print()

def main():
    try:
        get_system_info()
        cpu_cores = get_cpu_info()
        total_memory = get_memory_info()
        get_gpu_info()
        get_disk_info()
        check_browser_requirements()
        
        recommended, max_browsers = calculate_optimal_browsers(cpu_cores, total_memory)
        
        print("=" * 60)
        print("[+] ANALYSIS COMPLETE")
        print("=" * 60)
        print(f"[>] Recommended: use {recommended} browser(s)")
        print(f"[>] Maximum safe: {max_browsers} browser(s)")
        print()
        print("[?] WARNING: Start with a small number of browsers")
        print("[?] and gradually increase, monitoring system load!")
        
    except KeyboardInterrupt:
        print("\n[-] Analysis interrupted by user")
    except Exception as e:
        print(f"\n[-] Analysis error: {e}")

if __name__ == "__main__":
    main()