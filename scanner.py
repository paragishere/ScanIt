# import argparse
# from modules import xss, sqli, headers, admin_panel
# from colorama import Fore, Style


# def main():
#     parser = argparse.ArgumentParser(description="Simple Web Vulnerability Scanner")
#     parser.add_argument("url", help="Target URL (e.g. http://example.com)")
#     args = parser.parse_args()
#     url = args.url

#     print(Fore.CYAN + f"\n[~] Starting Scan on: {url}" + Style.RESET_ALL)
#     xss.scan(url)
#     sqli.scan(url)
#     headers.scan(url)
#     admin_panel.scan(url)

# if __name__ == "__main__":
#     main()

import argparse
from modules import xss, sqli, headers, admin_panel
from colorama import Fore, Style
from utils.banner import show_banner

show_banner()

def main():
    parser = argparse.ArgumentParser(description="Simple Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL (e.g. http://example.com)")
    args = parser.parse_args()
    url = args.url

    print(Fore.CYAN + f"\n[~] Starting Scan on: {url}" + Style.RESET_ALL)
    xss.scan(url)
    sqli.scan(url)
    headers.scan(url)
    admin_panel.scan(url)

if __name__ == "__main__":
    main()
