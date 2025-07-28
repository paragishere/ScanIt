import requests
import urllib3
from colorama import Fore, Style
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scan(url):
    print(Fore.YELLOW + "[Admin] Checking common and sensitive admin paths..." + Style.RESET_ALL)

    # Ensure URL starts with http/https
    if not url.startswith("http"):
        url = "https://" + url

    # Get baseline 404 error page content
    baseline_url = urljoin(url, "/thispagedoesnotexist-999")
    try:
        baseline = requests.get(baseline_url, verify=False, timeout=5).text.strip()
    except:
        print(Fore.RED + "[!] Could not fetch baseline 404 page. Exiting." + Style.RESET_ALL)
        return

    paths = [
        "/admin", "/admin.php", "/admin/login.php", "/admin/index.php",
        "/administrator", "/login", "/cpanel", "/dashboard", "/config", "/config.php",
        "/setup", "/webadmin", "/system", "/adminarea", "/admincontrol", "/useradmin",
        "/adminpanel", "/manage", "/manage.php", "/moderator", "/backend", "/server-status",
        "/server-info", "/portal", "/console", "/superadmin", "/root", "/access", "/auth"
    ]

    for path in paths:
        full_url = urljoin(url, path)
        try:
            r = requests.get(full_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'}, verify=False, allow_redirects=True)
            content = r.text.strip()

            if r.status_code in [401, 403]:
                print(Fore.MAGENTA + f"[!] Restricted path (auth required): {full_url} [{r.status_code}]" + Style.RESET_ALL)
            elif r.status_code == 200 and content != baseline:
                print(Fore.RED + f"[+] Real admin path found: {full_url}" + Style.RESET_ALL)
            # Optional: Uncomment below to see all scanned paths
            # else:
            #     print(f"[-] Not found: {full_url}")
        except requests.RequestException:
            print(Fore.CYAN + f"[x] Failed to fetch: {full_url}" + Style.RESET_ALL)
            continue
