import requests
from colorama import Fore, Style

def scan(url):
    print(Fore.YELLOW + "[Headers] Checking security headers..." + Style.RESET_ALL)
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers
        required = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy", "Strict-Transport-Security"]
        for h in required:
            if h not in headers:
                print(Fore.RED + f"[!] Missing header: {h}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"[+] Present header: {h}" + Style.RESET_ALL)
    except:
        print(Fore.YELLOW + "[~] Could not retrieve headers." + Style.RESET_ALL)
