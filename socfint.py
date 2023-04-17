import requests
from colorama import Fore,Style

def banner():
    print(F"""  {Fore.CYAN}
     ______             _______ _       
    / _____)           (_______|_)      
    ( (____   ___   ____ _____   _ ____  
    \____ \ / _ \ / ___)  ___) | |  _ \ 
    _____) ) |_| ( (___| |     | | | | |
    (______/ \___/ \____)_|     |_|_| |_|

                       {Style.RESET_ALL}  Coded By Yigoboz | https://github.com/yigoboz                      
                       {Fore.RED}  Warning: This tool does not give 100% results! {Style.RESET_ALL}
    """)

def github():
    r = requests.get(F"https://github.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Github {Style.RESET_ALL}: https://github.com/{username} ")
def tryhackme():
    r = requests.get(F"https://tryhackme.com/p/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] TryHackMe {Style.RESET_ALL}: https://tryhackme.com/p/{username}")

def instagram():
    r = requests.get(F"https://instagram.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Instagram {Style.RESET_ALL}: https://instagram.com/{username}")

def twitter():
    r = requests.get(F"https://twitter.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Twitter {Style.RESET_ALL}: https://twitter.com/{username} ")

def reddit():
    r = requests.get(F"https://reddit.com/user/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Reddit {Style.RESET_ALL}: https://reddit.com/user/{username}")

def blogspot():
    r = requests.get(F"https://{username}.blogspot.com")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Blogspot {Style.RESET_ALL}: https://{username}.blogspot.com")

def fiverr():
    r = requests.get(F"https://fiverr.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Fiverr {Style.RESET_ALL}: https://fiverr.com/{username}")

def hackerone():
    r = requests.get(F"https://hackerone.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] HackerOne {Style.RESET_ALL}: https://hackerone.com/{username}")

def hackerrank():
    r = requests.get(F"https://hackerrank.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] HackerRank {Style.RESET_ALL}: https://hackerrank.com/{username}")

def onlyfans():
    r = requests.get(F"https://onlyfans.com/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Onlyfans {Style.RESET_ALL}: https://onlyfans.com/{username}")

def roblox():
    r = requests.get(F"https://www.roblox.com/user.aspx?username={username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Roblox {Style.RESET_ALL}: https://www.roblox.com/user.aspx?username={username}")

def sourceforge():
    r = requests.get(F"https://sourceforge.net/u/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] SourceForge {Style.RESET_ALL}: https://sourceforge.net/u/{username}")

def sublimeforum():
    r = requests.get(F"https://forum.sublimetext.com/u/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] SublimeForum {Style.RESET_ALL}: https://forum.sublimetext.com/u/{username}")

def psnprofiles():
    r = requests.get(F"https://psnprofiles.com/?psnId={username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] PsnProfiles {Style.RESET_ALL}: https://psnprofiles.com/?psnId={username}")

def telegram():
    r = requests.get(F"https://t.me/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Telegram {Style.RESET_ALL}: https://t.me/{username}")

def tiktok():
    r = requests.get(F"https://tiktok.com/@{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Tiktok {Style.RESET_ALL}: https://tiktok.com/@{username}")

def twitch():
    r = requests.get(F"https://www.twitch.tv/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Twitch {Style.RESET_ALL}: https://www.twitch.tv/{username}")

def vsco():
    r = requests.get(F"https://vsco.co/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Vsco {Style.RESET_ALL}: https://vsco.co/{username}")

def virustotal():
    r = requests.get(F"https://www.virustotal.com/gui/user/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] VirusTotal {Style.RESET_ALL}: https://www.virustotal.com/gui/user/{username}")

def watpadd():
    r = requests.get(F"https://www.wattpad.com/user/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Watpadd {Style.RESET_ALL}: https://www.wattpad.com/user/{username}")

def wix():
    r = requests.get(F"https://{username}.wix.com")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Wix {Style.RESET_ALL}: https://{username}.wix.com")

def wordpress():
    r = requests.get(F"https://{username}.wordpress.com/")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Wordpress {Style.RESET_ALL}: https://{username}.wordpress.com/")

def wordpressprofile():
    r = requests.get(F"https://profiles.wordpress.org/{username}/")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] WordpressProfile {Style.RESET_ALL}: https://profiles.wordpress.org/{username}/")

def youtube():
    r = requests.get(F"https://www.youtube.com/c/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] YouTube {Style.RESET_ALL}: https://www.youtube.com/c/{username}")

def freecodecamp():
    r = requests.get(F"https://www.freecodecamp.org/{username}")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Freecodecamp {Style.RESET_ALL}: https://www.freecodecamp.org/{username}")


try:
    banner()
    username = input(F"Please Type A Username: ")
    github()
    tryhackme()
    instagram()
    twitter()
    reddit()
    blogspot()
    fiverr()
    hackerone()
    hackerrank()
    onlyfans()
    roblox()
    sourceforge()
    sublimeforum()
    psnprofiles()
    telegram()
    tiktok()
    twitch()
    vsco()
    virustotal()
    watpadd()
    wix()
    wordpress()
    wordpressprofile()
    youtube()
    freecodecamp()
except KeyboardInterrupt:
    print(F"\n{Fore.RED} CTRL+C Detected! {Style.RESET_ALL}")


