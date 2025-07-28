# from colorama import Fore, Style

# def print_banner():
#     banner = f"""{Fore.CYAN}
#   __                  _____ _   
# / _\ ___ __ _ _ __   \_   \ |_ 
# \ \ / __/ _` | '_ \   / /\/ __|
# _\ \ (_| (_| | | | /\/ /_ | |_ 
# \__/\___\__,_|_| |_\____/  \__|
#                                    by Parag & Pushpraj
# {Style.RESET_ALL}"""
#     print(banner)

# utils/banner.py

from colorama import Fore, Style

def show_banner():
    banner = f"""{Fore.RED}
  __                  _____ _   
 / _\ ___ __ _ _ __   \_   \ |_ 
 \ \ / __/ _` | '_ \   / /\/ __|
 _\ \ (_| (_| | | | /\/ /_ | |_ 
 \__/\___\__,_|_| |_\____/  \__|
                                    by Parag & Pushpraj{Style.RESET_ALL}"""
    print(banner)
