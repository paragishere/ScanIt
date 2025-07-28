import requests
from colorama import Fore, Style

def scan(url):
    print(Fore.YELLOW + "[XSS] Scanning for XSS..." + Style.RESET_ALL)
    payload = "<script>alert(1)</script>"
    test_url = f"{url}?q={payload}"
    try:
        r = requests.get(test_url, timeout=5)
        if payload in r.text:
            print(Fore.RED + "[!] XSS Vulnerability Found!" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "[+] No XSS vulnerability." + Style.RESET_ALL)
    except:
        print(Fore.YELLOW + "[~] Could not test XSS." + Style.RESET_ALL)
