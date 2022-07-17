#!/usr/bin/env python3

# Exploit Title: AreYouReady 
# Date: 2022-07-07
# Exploit Author: Julien Maury
# Software Link: https://github.com/jmau111/areyouready.py
# Version: >= 0.0.7
# Tested on: Windows Vista
# CVE: N/A
# GitHub: https://github.com/jmau111

# -------
# Credits
# -------
#  _____   _  _     ___             _   _    _      _____    ___   __  __    ___    _____    ___             _  _     ___     ___    _  __    ___    _  _     ___             _____    ___     ___   __  __  
# |_   _| | || |   | __|     o O O | | | |  | |    |_   _|  |_ _| |  \/  |  /   \  |_   _|  | __|     o O O | || |   /   \   / __|  | |/ /   |_ _|  | \| |   / __|     o O O |_   _|  | __|   /   \ |  \/  | 
#   | |   | __ |   | _|     o      | |_| |  | |__    | |     | |  | |\/| |  | - |    | |    | _|     o      | __ |   | - |  | (__   | ' <     | |   | .` |  | (_ |    o        | |    | _|    | - | | |\/| | 
#  _|_|_  |_||_|   |___|   TS__[O]  \___/   |____|  _|_|_   |___| |_|__|_|  |_|_|   _|_|_   |___|   TS__[O] |_||_|   |_|_|   \___|  |_|\_\   |___|  |_|\_|   \___|   TS__[O]  _|_|_   |___|   |_|_| |_|__|_| 
#_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| 
#"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
#######

try:
    import requests
except:
    print(f"ERROR: maybe run pip install requests")
    exit()

from argparse import ArgumentParser

class Color:
    CYAN = '\033[96m'
    RED = '\033[91m'
    END = '\033[0m'

def cipher_to_text():
    return "V2hhdCBhcmUgeW91IGxvb2tpbmcgYXQ/IEl0J3Mgbm90IHRoZXJlLiBUaGlzIGZ1bmN0aW9uIHNlZW1zIHVzZWxlc3MuLi4="

def args_parse():
    parser = ArgumentParser(
        usage='%(prog)s -login MY_GITHUB_LOGIN -pass MY_GITHUB_PASSWD',
        description='Script to determine whether you are ready for hacking or not yet.'
    )
    parser.add_argument(
        '-login', 
        dest='login', 
        type=str, 
        required=True, 
        help="Enter your GitHub login"
    )
    parser.add_argument(
        '-pass',
        dest='password', 
        type=str, 
        required=True, 
        help='Enter your GitHub password'
    )
    return parser

def args_get():
    parser = args_parse()
    return parser.parse_args()

def main():
    args = args_get()

    # Bite me...
    if args.login != "biteme" or args.password != "biteme":
        print(Color.RED + "OMG! Did you enter your credentials without checking what the code actually does?")
        exit()
    
    print(Color.CYAN + "╰(▔∀▔)╯ At least, you don't go blindly. There's no reason not to start your journey!")

if __name__ == '__main__':
    main()
