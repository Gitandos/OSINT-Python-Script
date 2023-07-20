import requests
import colorama
import pyfiglet
import pystyle
import os
from pyfiglet import figlet_format
from colorama import *
from pystyle import Center, Colors, Colorate, Box
from bs4 import BeautifulSoup as BS

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_blue, Center.XCenter(Box.DoubleCube(pyfiglet.figlet_format("Search Detective")))))
    print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(Box.DoubleCube("Hello, Welcome to Search Detective"))))
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube("1. Пробив По Гугл Дорки \n2. Пробив По Номеру\n3. Пробив По ФИО\n4. Пробив По VK [Закрыто]\n5. Пробив По IP\n6. Выход"))))
    chose()

def search():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube(figlet_format("Google Dorkie")))))
    es = input(f"\n\n{Fore.WHITE}[{Fore.RED}REQUEST{Fore.WHITE}] > ")
    url1 = fr"https://www.google.com/search?q={es}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    r1 = requests.get(url1,headers=headers)
    html1 = BS(r1.text, 'html.parser')

    for el in html1.select(".yuRUbf > a"):
        print(f"{Fore.WHITE}[{Fore.RED}URL{Fore.WHITE}] " + el['href'])

    input(f"\n{Fore.WHITE}[{Fore.RED}#{Fore.WHITE}] > Press enter for exit...")
    main()


def phonesearch():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube(figlet_format("Phone Search")))))
    es = input(f"\n\n{Fore.WHITE}[{Fore.RED}PHONE NUMBER{Fore.WHITE}] > +7")
    url1 = f"https://кто-звонит.рф/{es}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    r1 = requests.get(url1,headers=headers)
    html1 = BS(r1.text, 'html.parser')
    a = html1.find_all("div", class_="tel")

    for tel in a:
        print(f"{Fore.WHITE}[{Fore.RED}INFO{Fore.WHITE}] " + tel.text)

    input(f"\n{Fore.WHITE}[{Fore.RED}#{Fore.WHITE}] > Press enter for exit...")
    main()

def fiosearch():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube(figlet_format("Name Searcher")))))

    name = input(f"\n\n{Fore.WHITE}[{Fore.RED}NAME{Fore.WHITE}] > ")
    firstname = input(f"{Fore.WHITE}[{Fore.RED}FULL NAME{Fore.WHITE}] > ")
    url1 = f"https://looking-4.me/search?first_name={name}&last_name={firstname}&action=do_search&first_page_request=yes/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    r1 = requests.get(url1, headers=headers)
    html1 = BS(r1.text, 'html.parser')
    a = html1.select(".no-margin-top > a")
    print("")

    for people in a:
        print(f"{Fore.WHITE}[{Fore.RED}PEOPLE{Fore.WHITE}] " + people.text + ": " + people['href'])


    input(f"\n{Fore.WHITE}[{Fore.RED}#{Fore.WHITE}] > Press enter for exit...")
    main()

def ipsearch():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube(figlet_format("IP Searcher")))))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    ip = input(f"\n\n{Fore.WHITE}[{Fore.RED}IP-ADRESS{Fore.WHITE}] > ")
    
    url = f"https://ru.infobyip.com/ip-{ip}.html"
    r = requests.get(url, headers=headers)
    bs = BS(r.text, "lxml")

    res = bs.find("table", class_="results wide home")

    for ip in res:
        print(f"{Fore.WHITE}[{Fore.RED}IP-INFO{Fore.WHITE}] " + ip.text)

    input(f"\n{Fore.WHITE}[{Fore.RED}#{Fore.WHITE}] > Press enter for exit...")
    main()



def vkid():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(Box.DoubleCube(figlet_format("VK-ID")))))

    id = input(f"\n\n{Fore.WHITE}[{Fore.RED}VK ID{Fore.WHITE}] > ")
    url1 = f"https://vk.com/{id}]"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    r1 = requests.get(url1, headers=headers)
    html1 = BS(r1.text, 'html.parser')
    a = html1.find("h2", class_="OwnerPageName vkuiTitle vkuiTitle--l-2 vkuiTitle--w-1")

    print(a)

def chose():
    inp = input(f"\n\n{Fore.WHITE}[{Fore.RED}#{Fore.WHITE}] > ")
    if inp == "1":
        search()

    if inp == "2":
        phonesearch()

    if inp == "3":
        fiosearch()

    if inp == "4":
        vkid()

    if inp == "5":
        ipsearch()

    if inp == "6":
        quit()

    else:
        main()


if __name__ == '__main__':
    main()
