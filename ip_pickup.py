import requests
import json
import sys
from colorama import Fore,init


RED = Fore.RED
L_BLUE = Fore.LIGHTBLUE_EX
L_CYAN = Fore.LIGHTCYAN_EX
L_RED = Fore.LIGHTRED_EX
L_GREEN = Fore.LIGHTGREEN_EX
L_WHITE = Fore.LIGHTWHITE_EX


banner = """ 
______________¶¶¶
_____________¶¶_¶¶¶¶
____________¶¶____¶¶¶
___________¶¶¶______¶¶
___________¶¶¶_______¶¶
__________¶¶¶¶________¶¶
__________¶_¶¶_________¶¶
__________¶__¶¶_________¶¶____¶¶
__________¶__¶¶__________¶¶¶¶¶¶¶
_________¶¶__¶¶¶______¶¶¶¶¶¶___¶
_________¶¶___¶¶__¶¶¶¶¶¶__¶¶
_______¶¶_¶____¶¶¶¶________¶¶
______¶¶__¶¶___¶¶__________¶¶
_____¶¶____¶¶___¶¶__________¶¶
___¶¶_______¶¶___¶¶_________¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
________¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
______¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶¶
______¶__¶¶_¶¶¶¶¶¶
_____¶¶______¶___¶
_____¶¶_____¶¶___¶
_____¶______¶¶___¶
____¶¶______¶¶___¶¶
____¶¶______¶¶___¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
__¶¶________¶¶¶____¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

ʙʏ OᴄᴄᴜᴘʏTʜᴇWᴇʙ
[^-^] Ipピックアップ [^-^]
"""

print(L_GREEN + banner)


def help():
    print(L_RED)
    print('Hello Friend!!')
    print('*'*60)
    print('This Tool Get information from Ip Address')
    print('Usage: ./ip_pickup.py [Target ip]')
    print('Example: ./ip_pickup.py  8.8.8.8')
    print('*'*60)
    print(f'\n[^-^] Ipピックアップ [^-^] ')
    init(autoreset=True)


def main():
    try:
        target = sys.argv[1]
        req = requests.get(f'https://ipinfo.io/{target}')
        ip_inf = req.text
        inf = json.loads(ip_inf)

        print(f'{L_CYAN}[+] Ip: {inf["ip"]}\n[+] City: {inf["city"]}\n[+] Region: {inf["region"]}\n[+] Country: {inf["country"]}\n[+] Location: {inf["loc"]}\n[+] Org: {inf["org"]}\n[+] Postal: {inf["postal"]}\n[+] Timezone: {inf["timezone"]}\n')
        init(autoreset=True)
    except KeyError:
        print(f'{RED}[!] Ip Address: {target} \nNot Valid Please Try a Real Ip Address')
        init(autoreset=True)
        help()
        sys.exit(1)
    
    except Exception:
        help()
        pass


if __name__=='__main__': 
    main()



