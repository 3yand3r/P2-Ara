# HELLO WORLD !!! Good day folks , i am [ 3yand3r ] this tools was created  for Recon..100% Python 
# NIGERIA NO1 CYBER SEC [ 3yand3r ]
# this tools was created 4 Nigeria SYS ADMIN and CyberSec Expert.
 
#!/usr/bin/env python
from subprocess import call, sys
import socket
#!/usr/bin/env python
import colorama
from colorama import Fore, Back, Style, init
from rich.progress import Progress
from rich.progress import Progress
from rich.table import Table
from rich.console import Console
import os
import requests
from bs4 import BeautifulSoup
import random
import sys
import time
import pyshorteners
import qrcode
from PIL import Image
import whois
import string
import random
#import PyPDF2, pyttsx3
import urllib.request as urllib2
import json
#from rembg import remove
from PIL import Image
import subprocess
import re
import secrets
from pytubefix import YouTube
import zipfile
import datetime
#

colorama.init(autoreset=True)

init(autoreset=False)
print (Style.BRIGHT)
R = Style.BRIGHT+Fore.RED
B = Style.BRIGHT+Fore.BLUE
G = Style.BRIGHT+Fore.GREEN
C = Style.BRIGHT+Fore.CYAN
Y = Style.BRIGHT+Fore.YELLOW
M = Style.BRIGHT+Fore.MAGENTA
W = Style.BRIGHT+Fore.WHITE  
colors=['\033[1;31m', '\033[1;32m','\033[1;33m', '\033[1.34m','\033[1;35m',]
w='\033[0m'

tick = "\u2714" 
cross = "\u274C"
italic = "\033[3m"
italic2 = "\033[0m"


def ZipF():
    Display_banners()
    print (f"{B}Enter names of the files you want to Zip ")
    print (f"{Y}= = = = = = = = {W}*{Y}*{R}*{C}*{Y} = = = = = = = = = = = = =")
    file_paths = input(f"{Y}Enter file path (seprated by comma): ")
    file_paths = [path.strip() for path in file_paths.split(",")]
    zip_file_name = input(f"{Y}Enter zip file name: ")

    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for file_path in file_paths:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                zip_file.write(file_path, os.path.basename(file_path))
                print (f"{C}File: {Style.RESET_ALL}{W}{file_path} Added{G}{tick}")
            else:
                print (f"{R}[-]File not found: {file_path}[-]")
   
    print (f"{G}Zip File {zip_file_name} Created Successfully!")
    print (f"{W}{italic}Press enter to continue...{italic2}")


def Download_video():
    Display_banners()
    print(f"""                                                                      {Back.MAGENTA}{W} Press 'Enter' to go Back to {Back.WHITE}{G}[ Main Menu]""") 
    print (f"{B}*{R}*{Y}*{C}Welcome To YouTube Video Downloader Dashbord, Kindly Enter The YouTube Video Url To Download Video.{B}*{R}*{Y}*{Style.RESET_ALL}")
    print (f"{R}###########################")
    url = input(f"{Y}Enter YouTube Url: {Style.RESET_ALL}")
    print (f"{R}###########################")
    yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: print (f"{G}Downloading... {(stream.filesize - bytes_remaining) / stream.filesize * 100:.2f}% {Style.RESET_ALL}"))
    print (f"{M}Title: {Y}{yt.title}")
    print (f"{M}Author: {Y}{yt.author}")
    print (f"{M}Length: {Y}{yt.length} seconds")
    print (f"{W}Downloading Now...")
    yt.streams.get_highest_resolution().download()
    print (f"{G}Download successfully!{tick}")
    print (f"{M}{italic}Press Enter To Continue...{italic2}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner11():
    print(" ")
    print (f""" {G}
⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣷⡄⠀⠀⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⡄⠀⠀⠀⢸⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡄⠀⠀⣾⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣧⠀⠀⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⠟⠛⢿⣿⣿⣿⣿⣿⠛⠻⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣀⣾⣿⣿⣿⣿⣦⣤⣿⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣉⣹⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⡿⠋⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⠏⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⡏⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⠛⡻⠻⠛⠁⠉⠈⠙⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⣼⣿⣿⣿⠷⠄⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠋⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⣿⣿⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")

def banner13():
    print ("")
    print(f"""{R}


███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
{Y}░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
{W}██▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████


 """)

def banner14():
    print("")
    print (f"""{G}

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


""")

def banner15():
    print (" ")
    print (f"""{Y}
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀



""")

def banner1():
    print(" ")
    print(f"""{G}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠶⠒⢚⣛⣉⣉⣙⣛⣓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⠞⢋⣥⣴⣶⣿⣿⠟⠛⠉⠉⢻⣿⣿⣶⣬⡙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠉⠀⠀⣰⣿⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⢀⣼⣿⣿⢿⣿⣿⣾⠉⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣀⣀⣴⣿⣿⣿⣿⡿⠿⣿⣿⣦⣀⣀⣤⣶⣿⣿⣿⠀⠀⠈⣿⣿⣧⡀⠈⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⢞⣡⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣶⣾⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⢻⡵⠋⢙⣿⣿⣿⠟⠛⠉⠉⠛⣿⣶⣿⣿⣿⣿⣿⣿⠛⠋⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣮⣳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⢟⣷⣿⣷⣤⣾⣿⣿⡇⠀⠀⠀⠀⢀⣼⣿⡿⠟⠻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠹⣿⣿⡟⠉⠻⣿⣿⠋⠉⠓⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡼⠷⣟⣛⣛⡻⠿⠿⣿⣿⣿⣶⣤⣴⣶⣿⣿⣿⣇⣀⣀⣿⣿⣿⣿⣶⣤⣀⣀⣠⣼⣿⣿⡆⠀⢀⣿⣿⡀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡾⢁⣾⠟⠧⣉⠉⠙⠓⠲⠦⠤⣤⣌⣉⣉⣭⣭⣭⣉⣩⣉⣉⣍⣩⣭⣭⣭⣍⣛⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣦⡀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⡇⢸⡃⠀⠀⠀⠙⠲⠤⣄⣀⠀⠀⠉⢻⣿⣿⣿⣏⠻⡍⠛⠛⠛⠋⣰⢟⣽⡿⣿⣯⡛⠒⠤⢤⣈⠙⠻⢿⣿⣿⣿⣿⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀
⢧⢸⡗⠦⣄⡀⠀⠀⠀⠀⠉⠙⠓⢲⣿⣿⣧⣨⣿⡇⠁⠀⠀⠀⠀⠁⢸⣿⣠⣿⣿⣿⡒⠒⠚⠛⠛⠲⣤⣝⠻⣿⣿⡇⢿⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢧⢿⡀⠀⠉⠓⠒⠦⢤⣤⣤⣴⣿⣿⣿⣟⣿⡿⠃⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⣄⡀⠀⠀⣀⣹⣷⣮⡻⣷⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢷⣷⣦⣄⣀⣀⣀⣀⣀⣴⠏⠈⢮⠛⠛⠋⠀⠀⠰⠄⠀⠀⠰⠆⠀⠈⠛⠛⠫⠞⠀⠻⣌⠉⠉⠉⠀⠀⠀⠈⣷⡘⢺⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢿⣆⡀⠀⠉⠉⠉⣿⡀⠶⠲⠤⣄⣀⣀⡠⠤⠤⠤⠶⠤⠤⣄⣀⣀⣠⠤⠖⠂⢀⡟⠛⠶⠤⠤⠤⠤⢤⣾⢃⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⢿⣛⠛⠛⣿⠿⢦⡀⠀⠀⠀⠤⣀⣀⡠⠤⠤⣀⣀⡠⠤⠀⠀⠀⢀⡴⢿⣟⠳⠦⣤⣤⣤⠾⢟⣥⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⠶⠶⢭⣷⠞⠛⢦⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⢀⡾⠛⢷⣯⠽⠿⠶⣞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡿⠁⠀⢀⡾⠃⠀⠀⠈⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠁⠀⠸⢀⠀⠀⠙⣷⡀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⢰⠟⠁⠀⠤⢤⡇⠀⠀⠀⠀⠀⠉⠑⠀⠀⠀⠀⠀⠀⠊⠉⠀⠀⠀⠀⠀⣼⡤⠤⠀⠈⢳⡄⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⡄⢸⠀⠀⠀⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⢠⡇⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢳⡈⢧⡀⠀⠀⠀⠀⢿⡦⠤⠀⠀⣀⣀⣠⣤⣤⣤⣤⣀⣀⡀⠀⠀⠠⣾⡏⠀⠀⠀⠀⢠⡞⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⡄⠱⣤⡀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⢀⡴⠋⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣶⢶⣾⢷⣤⣮⣿⣦⠀⠀⠈⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⢀⣴⣯⡤⣤⣿⡶⠦⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣿⣻⠃⢹⡹⡞⠿⣷⡄⢀⣤⣶⣝⡻⠿⢷⡶⠦⠴⣶⡾⠽⣟⣫⣦⣄⠀⣠⣿⣾⣵⢳⡇⠹⡟⣿⡟⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀ ⠀
⠀⠀⠀⠀⠈⠛⠁⠀⠘⠛⠁⠀⠈⠹⡸⣅⢹⡝⠿⣷⠾⠃⠀⠀⠘⠷⣾⠟⣱⠋⣸⢰⠋⠀⠀⠙⠛⠁⠀⠙⠛⠁⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣘⡆⠙⠶⠛⠀⠀⠀⠀⠀⠀⠛⠒⠋⣾⣁⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀ ⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


""")
    
def banner2():
    print(" ")
    print(f""" {Y}⠀⠀⠀⠀⠀⣠⠔⠣⣔⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠞⠁⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡰⠋⠀⠀⠀⠀⠀⣿⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠄⢀⣀⣠⠤⠄⠤⣤⠰⠆⠓⠁⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣇⡁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⡅⡀⠀⠀⠀⠀⠀⠀⢠⣔⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣷⠅⠀⠀⠀⠀⠀⣰⣿⣟⡟⠀⠀⠀⣠⣤⣄⠀⠀⠀⠀⠘⠯⣆⢄⠀⠀⠀⠀⠀⠀
   ⠀⢠⡿⠀⠀⠀⠀⢠⣿⡟⡼⠁⠀⠀⣰⣿⡟⡟⠀⠀⠀⠀⠀⠀⠈⠑⠮⣔⡠⢀⠀⠀⠀
⠀⠀⠀⢸⡟⠀⠀⠀⠀⣼⣿⣱⠁⠀⠀⢰⣿⡿⣹⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠉⠓⢦⣆⡀
⠀⠀⠀⠸⡁⠀⠀⠀⠀⠹⠿⠁⠀⠀⠀⣾⣿⢷⠇⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠶⣀⠆⣆⣾⢰
⠀⠀⠀⠯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⠞⠀⠀⠀⠀⠀⢀⠈⡈⡄⢥⣘⣴⡶⢾⠺⠑⠁
⠀⠀⣸⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⢦⣴⡽⡛⠏⠃⠈⠀⠀⠀⠀
⠀⢰⡎⠔⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡄⣱⡼⠋⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣝⠠⡁⠤⡂⠴⡐⡠⢀⠀⡀⠀⠀⠀⠀⠀⠀⡀⢐⢰⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠡⠞⠚⠲⠣⠭⠍⠁⠣⠗⡜⡢⢄⠀⡂⡡⢄⠌⡥⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢆⠺⡐⡑⠎⠮⡱⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢴⣁⢎⢒⡡⣹⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢈⡊⡔⣻⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢵⡧⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")
    
def banner3():
    print(" ")
    print(f""" {C}
⢶⣿⣶⡢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⢾⡭⠂
⢻⣿⣹⣟⣦⡕⠦⣄⣀⣀⡀⢀⣀⣀⣠⣤⣀⣀⣀⡀⣀⣀⣠⣴⢿⣟⣒⠚⢷⡄
⠸⣷⡏⣵⣟⣻⣷⣮⢻⡿⢹⡿⢿⢿⡟⣫⡟⣽⠿⢩⡿⣫⢾⣱⣧⣦⣭⣷⣾⡇
⠀⢿⣿⣿⣴⡿⣟⠋⡀⠀⢠⡿⠉⣆⢌⡗⠀⣯⠀⠀⠀⠽⠻⢯⣷⣖⣿⣿⡟⠀
⠀⢸⣿⣿⣿⣍⣶⣄⡓⢈⢸⣿⣄⣿⣸⣧⣽⡾⠦⠀⠀⠄⣔⣩⣿⣿⣟⢻⠁⠀
⠀⢸⡛⣿⣽⣿⣽⡿⠳⣬⣾⠟⣿⣹⣿⢻⡟⠁⠤⢢⠀⠐⠿⠿⣫⣿⣿⢺⠀⠀
⠀⢸⣧⡻⣿⡿⠏⠓⠀⠈⣻⠀⣿⣾⣿⣾⠀⠀⠄⠀⠀⠀⠀⠈⠱⠿⠻⡸⠀⠀
⠀⠘⣿⣧⠽⢿⣤⣴⣿⣿⣷⣶⣇⠐⡷⢌⡧⣨⣴⣦⣤⣀⠀⠀⠀⠀⠀⡆⠀⠀
⠀⠀⢻⣿⣿⡿⣿⣿⣿⣿⣿⡯⣿⣠⠞⠈⢠⣿⣿⣿⣿⣿⠱⢤⡀⢀⣼⠃⠀⠀
⠀⠀⠈⣿⣿⣷⣿⣿⡿⢿⣿⣃⣄⠀⠠⠄⢨⡙⠿⢿⠟⢃⡀⠬⠿⣬⠏⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣷⣞⣻⣿⣿⣏⣀⣀⣼⡟⠓⠤⢄⣀⡛⠋⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣿⡿⠋⠉⠀⠈⣻⣿⣟⡁⠀⠈⠉⠙⠉⢉⣴⣲⡞⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣷⢟⣿⢩⡉⣿⣿⠿⣿⢯⣅⠀⠢⡴⠻⢍⣉⠐⣧⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣾⣿⣶⣿⣾⣤⣏⣰⣬⣶⣸⣥⡱⡔⢤⡂⠀⠘⡆⠀⠀⠀⠀
⠀⠀⢠⣿⣛⣿⢿⢻⣿⣿⣿⣿⣿⣿⡿⠟⠻⠟⠉⡀⠘⠋⠀⠀⠀⣼⠀⠀⠀⠀
⠀⠀⣸⠿⡿⣟⢮⡞⣏⡿⣻⠛⠟⠛⠁⠂⠀⠐⠀⠁⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀
⠀⠀⣿⣿⢷⡟⣫⡙⣦⠳⡁⠨⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⢷⠀⠀⠀
⠀⢸⣿⡾⣿⣿⣶⣧⠟⣥⡆⠀⠙⡄⡅⠀⠀⠀⠀⠰⡖⣶⠖⠋⠁⢠⠼⠀⠀⠀
⠀⠘⣿⣿⣿⣾⣿⣿⣿⡟⢰⡎⠀⢽⡈⠀⠀⠀⡀⣼⣵⣁⣬⠴⠚⠀⢸⠀⠀⠀
⠀⠀⢻⣷⢻⣿⣿⣿⣿⣂⣼⡁⢣⠀⠇⠀⠀⠀⠀⣿⠻⡏⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⢈⣷⠿⣯⣿⣿⣿⠦⢹⣇⢾⣆⠸⠁⠀⠀⠀⡿⢀⠁⠀⠤⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣥⣒⠅⡙⣿⣿⣧⣾⣿⢲⣿⠀⡥⠀⠀⢠⡗⠀⠀⠀⠀⠠⡞⠀⠀⠀⠀
⠀⠀⢸⡿⠋⠁⠀⠹⣿⣿⢷⣿⣹⣿⢰⡏⠀⡄⣿⣟⡀⡀⠀⠀⣰⠃⠀⠀⠀⠀
⠀⠀⠈⢿⣔⠆⠀⣰⣿⣿⡾⣿⢿⣿⡷⣧⢰⣻⣿⣿⣤⣧⡤⢐⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⣿⡟⢫⢿⣶⡟⡦⣿⣿⣟⣦⣿⣿⣿⠟⠁⠉⣹⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣗⢎⡞⢻⡑⣃⢫⢿⡿⣽⡟⠏⠋⠀⠀⢰⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣟⣖⣦⣄⢢⣏⣾⠛⢫⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣟⣾⣯⣿⣿⣿⣾⣿⣿⡷⣿⠂⣀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⡘⠿⠛⢡⠟⣿⠃⠁⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠒⠋⠁⠀⠘⠷⣌⣀⡰⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")
    
def banner4():
    print(" ")
    print(f""" {R}⠀⠀⠀⠀⠀⠀
⠿⠿⠟⠛⠛⠛⠛⠉⠉⠀⢀⣴⣿⣿⣿⡿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣀⣀⣀⣠⡄⣠⣴⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣦⣍⣙⡛⠻⠿⠿
⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶
⠉⠉⠉⣿⣯⣁⣀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣋⠁⠀⠈⠁⣩⡝⠻⢿⣿⣿⣿⢿⣿⣿⣿⣿
⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⣤⣤⠀⠀⣠⣿⣿⣷⣄⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣷⣤⣤⣽⣄⠀⠀⠿⣿⣆⠀⠙⢿⣿
⣶⡄⠀⠀⠀⠘⢿⣿⣿⣿⣿⣷⣄⡀⠀⢸⣿⣿⣧⠀⠹⣿⣿⣿⣿⣷⣤⡀⠐⠤⢤⣉⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣦⠀⠀⠀
⠉⠀⣀⣀⣤⣴⣿⣿⣿⣿⣿⣿⠋⠁⢠⣼⣿⣿⣿⠈⠀⠹⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣛⠋⢉⡹⣿⣷⣾⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⣿⣿⣿⣿⡿⠆⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢣⢹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⡿⠿⢛⣁⠀⢀⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠈⣉⠛⠛⠉⠁⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⠘⡄⢻⣿⣿
⣿⣿⣿⡟⠛⠉⠉⠻⠦⠉⠉⠉⠛⢿⣿⣿⡿⠋⠀⠀⣼⣿⣷⣦⣤⡀⠀⠀⠀⠠⠴⠒⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⢸⠈⣿⣿
⣿⡇⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠉⠁⠀⠀⠀⠀⠿⠿⠿⠉⠉⠉⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣤⣀⣼⣿
⣿⡇⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⣼⣴⠖⠚⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣴⣾⣿⠁⠀⠀
⠉⠁⠀⠐⣾⣿⡄⠀⠀⠀⠀⣤⣿⣿⣿⣦⣄⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣦⡀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⢠⣿⣏⣃⣀⣀⣀⣷⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⠀⠀⠀
⠿⠧⠀⢰⣾⣿⡷⠚⢻⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⢻⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣴⢿
⣶⣿⣿⣿⣿⣿⣿⣿⣿⢏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠻⣿⣿⣿⣿⣿⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀
⣿⣿⣿⣿⣿⣿⡿⠋⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠻⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠰
⣿⣿⣿⣿⣿⡿⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠀⠀
⣿⣿⣿⣿⡿⢁⢠⣿⡿⠃⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⣿⣿⣿⠛⢠⣿⣿⣿⣇⣀⣠⣼⡟⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⡛⢛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠋⠉⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀
""")
    
def banner5():
    print(" ")
    print(f""" {B}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣶⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠖⢂⣽⣿⣿⣷⣔⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟
⠀⠀⠀⠀⣀⣤⡶⢿⣋⣥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⢀⣠⣾⠿⠋⠀
⠀⢀⣴⣿⠟⠉⠀⠀⠀⠈⠉⠛⠻⣿⣿⣿⣿⡿⠛⠋⠉⣀⣤⠶⠟⠋⠁⠀⠀⠀
⢰⣿⡟⠁⠀⠀⠀⣷⠀⠀⠀⠀⠀⠈⣿⣿⣟⣀⡤⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠿⣧⣀⡠⠤⢾⣿⣷⠤⠄⠀⠀⠀⢹⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀

""")
    
def banner6():
    print(" ")
    print(f""" ⠀{C}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣛⡛⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣹⣽⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣦⣌⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣴⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡬⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣿⣉⣭⣭⣭⡿⣿⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡃
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣤⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠻⠿⠿⢿⣿⣿⣟⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⡇
⢸⣿⣿⣿⣿⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡏⢹⣿⣿⣿⡿⠟⠛⠛⠿⣿⣿⣿⣿⣿⠀⠐⠛⠛⠃⠀⢢⠀⢹⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣾⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⡏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⡟⣿⠀⣿⡿⠋⠀⠂⠀⠀⠀⠹⣿⡖⣿⣿⠀⠀⠀⠀⠀⠀⢸⠿⠀⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⡏⢠⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢳⣻⣶⡟⠀⠀⠀⠀⠀⢸⠃⠀⣿⠧⠛⢿⣄⡀⠀⠀⣀⢀⠾⠀⢸⣿⣶⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⠇
⢸⣿⣿⣿⣿⣿⠁⠋⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣻⡇⠀⠀⠀⠀⠀⠘⠀⣰⡏⠀⠀⠀⠻⣿⣶⣤⣉⣉⣠⣴⣿⣿⣿⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡿⠋⠀⠀
⢸⣿⣿⣿⣿⣿⡇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠱⢾⡄⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡍⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⡄⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⠀⢰⠋⠉⠀⠀⠀⠀⠈⣿⣿⣿⡿⠿⢿⣿⣿⣿⡿⣡⣿⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢾⣿⣶⣀⣀⣶⣿⣿⣿⣦⣀⣤⢦⣤⣿⣿⣿⣿⣿⠟⢋⡿⢇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⣄⠀⠀⠀
⢸⣿⣿⣿⣿⡿⠃⡄⠀⠀⠀⠰⠀⠀⣠⡯⣽⡛⠀⠀⡀⠈⠻⣿⡧⣾⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⠃⢸⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣟⡶⡆
⢸⣿⣿⣿⣿⡇⠸⣿⣦⡀⠀⣀⣠⣾⠟⠃⢿⣧⠀⠀⠁⠘⠀⠘⣇⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠘⢿⡿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⡟⢃⣡⡧⠀⣾⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣙⠳⡇
⢸⣿⣿⣿⣿⣿⡶⢈⢛⣿⣿⣿⡿⠋⢀⡆⢸⣿⡀⠀⠦⠄⠀⣸⡇⣴⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣷⣶⣷⣶⣾⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⠓⠿⡿⣿⡟⣻⢩⣯⣽⣷⠙⠃⠈⠁⢠⠴⡞⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⢀⠸⣿⣿⣿⣿⠃⡼⢻⣿⣿⣟⣣⣀⡈⠁⢸⣿⣿⣿⣶⣾⢯⣿⢻⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠁⠑⡓⠛⠃⠉⣈⠉⠀⠀⠀⠀⠀⣀⣾⣾⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⠆⢻⣿⣿⡟⢰⣷⠀⠪⢝⡻⢿⣿⣿⣿⣿⣿⣿⢿⣩⡷⢂⣼⣿⣿⣿⣿⣿⣿⡟⠉⠋⠁⠈⢿⣿⠃⠀⠈⠙⢿⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⢳⣀⠀⡀⢀⠀⣀⣠⣖⢺⣟⣛⢸⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⢸⣿⣿⣧⠘⣿⣇⢀⠀⠁⠘⠐⠗⠾⠿⠿⠧⣼⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣠⣀⣀⣹⣷⡀⠀⠀⠀⠀⢻⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠐⣍⣧⣽⣬⣧⣼⣿⣿⣿⣿⣿⡿⠟⠀⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⢃⣸⣿⣿⣿⣧⠸⣿⣿⣤⣀⣆⠠⢠⠤⠤⣤⣶⣼⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⡹⠋⠉⠽⠿⣿⣿⡄⠺⠣⠀⣾⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹⣾⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⣠⡞⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⣸⣿⣿⣿⣿⣿⣆⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡁⠀⠀⠀⠀⠈⠙⠃⠀⣇⡐⠃⣼⣿⣿⣿⣿⢿⣷⣦⣍⣻⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡯⣝⣿⣿⣷⣶⣶⠛⣿⣿⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣟⣻⣟⠛⠛⠿⡇
⢰⣿⣿⣿⣿⣿⣿⣿⣷⠀⢩⣟⡛⠿⠿⠛⢉⣠⡔⠒⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡄⢠⠀⠀⠀⠀⢸⠟⠉⠈⣿⣿⣿⣿⠇⣘⣻⣻⣿⢻⣿⣷⡿⠿⡛⢿⣟⣿⣿⣿⡿⣛⣻⣿⡇⠉⠀⠀⠉⠁⢠⣿⡏⢹⣿⣷⣾⣿⣍⢻⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣷⡆
⢨⣭⣉⣿⡿⠟⠋⠐⠺⠂⣿⣤⣏⢙⣿⣿⣿⠛⠃⠀⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⠈⠀⠀⠀⢠⡾⢶⠋⡀⢹⣿⣿⣏⣿⣿⣿⣿⣿⣉⡁⠹⣿⡌⣿⣿⡿⠉⠉⠀⣀⣀⡀⠈⠁⠨⠀⠀⠀⠀⠊⠙⢃⠈⠍⠉⣿⣿⡿⠟⠛⠛⠛⢉⣉⣭⣿⣿⣿⡆⢉⠉⠁⡄
⠈⠻⢿⣟⠁⠀⠀⠀⠀⠒⠈⠙⠻⠿⣿⣿⣿⠏⠉⠉⠑⢶⣦⡉⢻⣿⣿⣿⣿⡿⠿⠿⣿⣿⡀⠀⠀⠃⢀⣾⡏⠉⠙⠀⠈⣿⣿⣇⣹⣿⣿⣿⣿⣏⠀⠂⢸⣿⣿⣼⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⣀⣀⣀⡀⠂⢀⣩⣴⣶⠿⠛⠉⠀⢠⣤⡄⠯⣾⣿⣿⣿⣿⣿⠇⠀⠻⠀⠀
⠀⠀⣀⠙⣿⣶⣤⣀⡈⢀⣿⣿⣶⣶⣤⣴⣾⠀⠀⠀⠀⠀⣻⣿⣤⣿⣷⣶⣿⣿⣿⣷⣷⣦⣥⠆⣠⣾⣿⠟⠓⠀⠀⡀⠀⠈⠍⠛⢉⣿⣿⣿⣿⣿⡆⠀⣶⡻⣿⡿⠙⢻⣿⣶⣿⣶⣶⣶⣤⣾⣿⣿⣿⣿⣿⠿⠛⡉⠀⠀⠀⠊⢀⣼⣿⠻⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⡀⠀
⢀⠀⢻⣇⠙⣽⠛⠿⢿⣾⣿⣿⣿⣿⣿⡏⢀⣤⣴⣾⣿⣿⣿⣿⣿⡛⠋⠉⠉⠉⠉⠛⣿⣿⣿⡁⢈⠉⢁⣀⠀⠀⠘⠒⢂⡀⠄⠉⢹⣿⠿⠟⠛⠁⠀⠀⢻⣷⡆⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠹⠿⠿⠛⠉⠀⠐⠋⠡⠀⡀⠀⣠⣾⡟⢻⣷⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠁⠀
⠀⠀⠈⠛⣷⣤⣀⡀⣾⣿⣿⣿⣿⣿⣿⣧⠸⡿⠟⠛⠉⠁⢠⣿⣿⠃⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⠈⣿⣿⡷⠉⢙⣩⠅⢠⣤⣤⣿⣿⠆⣠⠀⠀⡀⠀⠀⠹⣷⡀⠙⢿⣿⣿⣿⣿⣿⠏⢁⡀⠀⠀⠀⠀⠀⠀⢀⣐⣉⣴⣾⣿⠟⠀⠀⣿⣿⣧⣿⣿⣿⣫⠟⢻⣷⠀⠀⡀
⠀⠀⠀⠀⢌⠙⠻⣿⡏⠁⣀⠀⠙⠛⠋⠁⠀⠀⠀⢀⣠⣴⣿⣿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣃⣀⣀⠙⠟⢀⣀⡀⠀⣀⡸⢿⣿⣿⠇⣼⣷⣇⣰⠀⠀⠀⠀⠻⢷⡀⠈⢿⣿⠛⠛⠁⢠⣾⣿⣿⣿⡿⠻⡿⠿⠟⠛⣉⠙⢉⣀⣀⠀⢸⣿⡗⢸⣿⣿⡿⠃⡄⣿⣿⣇⠈⠁
⢸⣦⣀⠀⠀⠀⠀⠈⣷⣿⣿⣿⣷⣦⢿⣿⣶⡿⠿⠟⠛⠋⠉⢳⣧⠀⠀⠀⡠⠖⠋⣿⡿⣿⣿⠈⢍⠻⣿⠇⠘⠀⠈⠉⠀⢠⣾⣿⡏⠀⣿⣿⡿⢿⣀⡀⠀⣀⣠⣤⣧⣤⡀⠀⠀⠀⠐⠟⠛⠉⠁⠀⠀⠀⠂⠘⠓⠚⢁⠔⠀⠀⠈⢁⣼⣿⠟⡿⣿⡏⢀⣾⣇⢸⣿⣿⡄⠀
⠈⢿⠿⢿⣦⣤⡀⠺⠛⠿⢿⣿⡿⠋⠀⣀⠘⠉⠀⠀⠀⠀⠀⣸⣿⠀⢀⠎⣠⣾⢰⣿⡽⣿⣿⠀⠤⠠⣤⡆⠀⠲⠶⢶⣶⣾⣿⣿⣥⣞⡁⢹⣷⣈⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣶⡦⠀⢠⡶⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠐⢃⣸⣶⣿⣿⣯⡿⣱⣿⡇⢼⣿⣿⢸⣿⣿⡷⠀
⠐⠢⠀⠀⠉⠉⠛⣷⣦⣄⣸⣥⣀⣠⣦⣤⣤⣤⣤⣶⣦⣾⣿⡿⠃⢀⡌⢰⣿⡿⢸⣿⡇⣿⣿⣇⣀⣀⠈⠉⠀⣀⡀⠀⢠⣿⣿⡏⢨⢹⣷⢸⣿⣿⡌⠙⠿⠿⢿⣿⣏⣿⣿⣿⣧⠀⡆⢸⣿⣄⠀⠀⠀⠀⠈⢓⣀⣤⣴⣾⣿⣿⡿⣿⠟⠁⠀⢹⣿⣿⡌⣿⣿⢸⣿⣿⡇⡄

""")

def banner7():
    print(" ")
    print(f"""{G}⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠀⠀⢰⣿⡿⠗⠀⠠⠄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⠈⠑⢶⣶⡄
⢀⣶⣦⣸⠀⢼⣟⡇⠀⠀⢀⣀⠀⠘⡿⠃
⠀⢿⣿⣿⣄⠒⠀⠠⢶⡂⢫⣿⢇⢀⠃⠀
⠀⠈⠻⣿⣿⣿⣶⣤⣀⣀⣀⣂⡠⠊⠀⠀
⠀⠀⠀⠃⠀⠀⠉⠙⠛⠿⣿⣿⣧⠀⠀⠀
⠀⠀⠘⡀⠀{Y}⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀
⠀⠀⠀⣷⣄⡀⠀⠀⠀⢀⣴⡟⠿⠃⠀⠀
⠀⠀⠀⢻⣿⣿⠉⠉⢹⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀
""")
    
def banner8():
    print(" ")
    print(f""" {R}
⠀⠀⠀⠀⠀⠀⠀⠠⡧⠀⠀⠀⠄⠀⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡄⠀⠀⠀⢺⠂⠀⠀⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧
⠀⠐⠗⠀⠀{Y}⠀⠀⠁⠀⠀⠀⣼⣿⡏⣿⣷⡀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠐⠺⠂⠀⠀⠀⠀⠀⠀⠄
⠤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠇⠀⢿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒
⠀⠀⠘⢿⣿⣿⣟⠛⠛⠛⠛⠀⠀⠀⠛⠛⠛⠛⠋⠉⠉⠉
⠀⠀⠁⠀⠈⠛⣿⣿⣦
⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿
{B}⠀⠀⠠⡧⠀⠀⣾⣿⠁⢀⣤⣾⣦⡀
⠀⠠⠀⠀⠀⠀⣸⣿⢇⣶⣿⠟⠙⠻⣿⣄
⠀⠀⠀⠀⠀⢠⣿⣿⠿⠋⠁⠀⠀⠀⠀⠉⠳⡄
{R}⠀⠀⠀⠀⠀⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈

""")
    
def banner9():
    print(" ")
    print(f""" {C}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀   ⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⢙⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣶⣒⣶⠦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀{R}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀{M}⠀⠀⣀⡤⠞⠁⠁⣰⣆⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉⠀⠀⠀⠠⡧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

def banner12():
    print (" ")
    print (""" ⠻⣿⣿⣿⡿⢣⣾⣿⠏⢀⣬⣭⢝⡻⠿⠃⠋⠀⠈⠙⠻⣷⣝⢿⣮⣑⢮⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡟⣿
⠀⠈⠛⠟⣱⣿⣿⠏⠐⠋⠭⠙⢉⣠⣶⣿⣿⣿⣿⣷⣤⡈⢿⣇⠝⢿⣷⡻⣦⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣷⡿⣿
⠀⠀⠀⣴⣿⣿⡯⠀⠵⢚⣡⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡹⣦⡈⢿⣷⡜⢧⢢⣍⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣯⣟⣽⣫⡗⣿
⠆⠀⢀⣾⣿⣿⡇⠘⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢥⣿⣷⠈⠻⣌⠻⣿⣆⠈⢿⣦⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢾⢷⣯⡗⣿
⣿⢃⢸⣛⣿⡌⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢋⡀⠊⢀⢠⣄⢁⠀⠈⠳⠙⠻⢣⡈⠻⢃⣼⣿⣿⣿⣿⣿⣿⣿⣻⣞⠾⣼⣫⡞⣵⣛⡽
⠏⠀⡿⢸⡿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡞⠀⢎⢋⣡⣌⣉⢀⡐⠆⠀⠟⡤⠙⣄⢈⣻⣿⣿⣿⣟⢿⣻⢟⡶⣏⡟⣖⣣⣛⢶⣩⢟
⠃⡇⣇⢹⡇⣿⡆⢻⣿⣿⣛⣋⠩⡀⠸⣿⣿⣿⣿⣧⣼⣾⣿⣿⣽⣿⣷⣦⡀⢸⣿⠂⠹⣆⣿⣿⡿⠿⠟⠳⡽⠾⣵⢭⣛⢮⣓⢮⡳⣝⡞
⠀⡇⣿⢸⣿⡸⣿⡜⣿⡿⠟⢁⣀⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢡⡅⡀⢦⢻⣌⢿⡞⣿⠟⠀⠀⠉⠘⠚⠽⣎⡽⢎⡳⣍⡞
⡄⢗⢸⡆⣿⣧⠹⣷⡘⠇⢠⣘⠋⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠰⢛⣰⡿⠘⠘⡟⡄⡿⢤⣶⣤⣄⣀⡀⠀⠀⠀⠈⠉⠁⠈⠈
⣇⢈⢂⢻⠘⣿⣷⡹⣷⡀⠰⣊⣴⣿⣿⣿⣿⣿⣿⢿⣧⣶⣿⣿⣿⣿⣷⣿⢠⢠⠸⡇⠀⠇⠱⣿⡇⠺⢿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀
⣿⣦⣂⠄⠁⢹⣿⣷⡜⢏⢊⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⢀⠃⠁⣰⣧⠹⣧⠀⠈⠉⠛⠋⠛⠉⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣦⠁⢹⣿⣿⣦⡁⢁⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⡆⡀⡀⠀⢀⣲⣌⣉⣀⡙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣻⣽⣷⣿⡄⠢⠹⣿⣿⣿⣦⡙⠒⠌⠩⢿⣿⣿⣿⣿⣿⣿⡿⠛⣠⡟⣰⠃⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣷⣻⣿⣿⣿⡀⠁⡹⣧⡻⣿⣦⣄⢮⣶⠶⣦⣄⡰⢥⣤⣤⡴⠾⠋⠼⢣⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣼⣿⣿⣿⣿⣷⠘⢂⡨⡑⢜⠻⢿⣦⠨⣵⣴⠉⢶⣮⣶⠖⠀⠀⠀⠐⣶⣦⣌⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⡀⣀⢀⡀
⣿⢺⣿⣿⣿⡿⢋⠆⠙⢷⡎⣂⠓⠄⢈⡓⠪⠐⣀⣤⡝⣡⣏⡐⠀⣦⣄⠈⠘⠜⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡐⠢⠘
⣛⡿⣿⣿⡿⠃⣠⣿⣿⠀⠀⠈⢻⣇⠍⣠⣶⣿⣿⡟⠱⠿⠟⠀⢰⣿⣿⢣⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡁
⣯⡹⡵⡛⢀⣼⠟⠏⠁⠀⠀⠀⠀⣡⣾⣿⣿⣿⣿⣿⣷⣶⣄⣀⠿⣿⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣏⢧⡓⢁⡜⠋⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡝⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣿
⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⢿⣿⢯
⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣞⣧⣿⡟⣫⣾
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣳⣻⣭⣶⣿⣿⣿
⠀⠀⠀⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⢨⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡠⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀
⠀⢌⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣄⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢁⣴⡄⠀
⢈⠢⠘⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⢼⡟⢱⣦⣬⣉⣙⣛⣛⡛⠛⠛⢉⣩⣤⡴⣾⣻⢾⣿⣳
⠀⠆⡉⠄⠘⣿⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣿⣾⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿
⠈⠔⠠⠘⡀⠘⣿⣿⣆⠻⣿⣷⣭⣿⢿⣭⢿⣟⣾⠟⣽⣿⣿⣿⣿⣿⣿⠃⣼⡿⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠈⠄⡁⠂⠄⡁⠈⢻⣿⣷⣬⣛⣛⠿⠯⠟⠿⢞⣭⣾⣿⣿⣿⣿⣿⡟⢁⣴⠟⣡⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿
⠈⡐⢀⠁⠂⠄⠡⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⣤⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣯⣟⣿⣟⡿⣿⣿⣿⣿⣿⣿
⠀⡐⠠⠈⠐⡈⢀⠁⡐⠀⠀⠉⠙⠛⠿⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣧⣍⢞⠫⣿⣻⢽⣻⣟⣿⣟⣿
⠀⢀⠀⠁⠂
""")

def banner10():
    print(" ")
    print(Fore.LIGHTCYAN_EX + f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠀⣿⡂⢹⡇⠀⠀⣰⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⢸⣇⢸⣇⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠀⠀⣏⠀⡆⠀⠀
⢸⣷⢸⣇⣸⣇⠀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣂⠀⣿⡄⢸⡀⣤
⢠⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣊⡝⠛⠙⠂⠄⠠⠀⠀⠀⠀⠀⠀⡀⠀⠄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⣼⣷⣼⣁⠼
⢸⣿⣿⣿⣿⣿⣿⣀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡻⣥⢋⡔⡀⠀⠀⠀⠀⠂⠁⠀⠄⠀⠠⠀⠂⢀⠀⠐⠈⠀⢀⠠⢀⣀⡀⠘⣿⡟⢿⣿⣿⣄
⠈⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⢯⣿⣾⡔⠀⠀⠀⠀⠀⠂⢁⠠⠈⢀⠐⠀⠂⡀⠂⠠⠈⠀⠀⠉⠁⠁⣀⣈⠧⠈⠻⣿⣿
⠀⣿⣿⣟⢿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡟⠛⠉⡉⢸⡉⠁⢀⠀⠀⠀⠀⠠⢁⠂⡐⢈⠀⠂⡁⠂⠄⢁⠂⠄⠡⠈⠄⠂⠄⡈⠀⠂⡁⠀⢻⠇
⠀⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡇⣤⡤⢔⡿⣇⠀⢦⠀⠀⠀⠀⠐⣀⠂⡐⠢⢈⡐⠠⠁⠌⡀⠂⠌⠠⠁⡌⢐⠂⠔⡈⠆⣔⣠⣯⠀
⠘⡟⣛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⣿⣿⠗⡲⠏⠟⠿⠀⠈⠓⠀⠀⠀⠡⡀⠆⣁⠢⢁⠤⠑⡨⠐⠤⠑⡨⠐⡡⠐⡌⢌⠒⡄⠈⠉⠁⠁⠀
⠃⡜⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣼⣿⡟⢡⡿⠿⠷⠀⠀⠀⠀⠀⢀⠱⣀⠣⢄⠢⡁⢆⠱⢠⠉⢆⠱⣀⠣⡐⠡⢌⠢⡘⠤⡁⠐⠒⠂⠂
⠐⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢻⠸⣡⢶⣿⣟⡃⠀⠘⠀⠀⢆⠡⢂⡜⢠⠃⡜⢠⢃⠦⣉⠦⡑⢢⡑⠬⡑⡌⢢⢑⠢⠅⠀⠀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠐⠀⢁⡰⢸⠣⠉⠉⠋⠉⠀⠀⠀⠀⠈⠀⠣⢡⠜⢢⠩⢔⢣⡘⢲⡐⠦⣙⠢⣌⠓⣌⠲⡡⢎⠥⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣶⡶⠆⠁⠠⠁⠊⠐⠁⠈⠠⠄⠂⠉⠈⠖⠀⠀⠒⣶⢦⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠁⠀⠀⠀⠁⠈⠱⢌⠳⣌⠳⣌⢣⡕⢮⡘⡅⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠏⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠘⡳⢬⠳⡜⢦⡹⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠋⠧⠹⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠃⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢶⠀⡶⣲⠀⣆⡒⣰⠒⢦⢰⠀⢰⡆⣴⠐⣶⠒⣐⣒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣺⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠐⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠚⠃⠻⠴⠃⠦⠝⠘⠤⠎⠸⠤⠘⠧⠞⠀⠛⠀⠰⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣾⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⠀⠀⢠⣤⠀⠀⣤⣄⠀⠀⠀⣤⣤⠀⢠⣤⣤⣤⣤⣤⡄⢠⣤⣄⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⢠⣤⡄⠀⠀⠀⢘⡮⡝⣿⣿⡿⢆⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠏⠉⠉⢿⣷⠀⢸⣿⠀⠠⣿⣿⣧⡀⠀⣿⣿⠀⢸⣿⡏⠉⠉⠉⠁⢼⣿⣿⡄⠀⠀⢸⡿⣿⡇⠀⠀⢀⣿⢻⣷⠀⠀⠀⡞⡜⣹⣿⣿⡙⢆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⠐⣿⡯⢻⣷⡀⣿⣿⠀⢸⣿⣷⣶⣶⡆⠀⢺⣿⠹⣿⡀⢠⣿⠃⣿⡇⠀⠀⣾⡟⠀⢿⣧⠀⠀⢣⠣⢽⣿⣯⡙⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡀⠀⠀⣠⣤⠀⢸⣿⠀⢈⣿⡧⠀⠹⣿⣿⣿⠀⢸⣿⡇⠀⠀⠀⠀⢸⣿⡄⢻⣧⣾⡏⢠⣿⡇⠀⣼⣿⣷⣶⣾⣿⣇⠀⠀⠱⢸⣿⢣⠜⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣶⣾⣿⠏⠀⢸⣿⠀⠀⣿⡷⠀⠀⠹⣿⣿⠀⢸⣿⣿⣿⣿⣿⡆⢸⣿⡆⠀⢿⡿⠀⢰⣿⡇⢀⣿⡏⠀⠀⠀⢹⣿⡀⠀⢁⢸⡇⠈⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠈⠉⠀⠀⠉⠁⠀⠀⠀⠉⠉⠀⠈⠉⠉⠈⠉⠉⠁⠈⠉⠀⠀⠈⠁⠀⠀⠉⠁⠈⠉⠀⠀⠀⠀⠈⠉⠁⠐⡀⢸⡐⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢘⠀⠀⠀⠀⠀⠀
 """)
 


def Display_banners():
    clear_screen()
    banners = [banner1,banner11,banner12,banner13,banner14,banner15, banner2, banner3, banner4, banner7, banner8, banner5, banner6,banner10, banner9]
    random.choice(banners)()
    with Progress()  as progress:
        task = progress.add_task(f"{Fore.CYAN}{Style.BRIGHT} Loading Application Please Wait...{Back.RED}{Y}[{W} P2-Ara{Y} ]{Style.RESET_ALL}", total=100 )
        while not progress.finished:
          progress.update(task, advance=10)
          time.sleep(0.2)



def info():
    print(" ")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print (f"{W}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{Style.RESET_ALL}")
    print ( f" {Back.MAGENTA}[+] Codded By:@\u00A3yand3r {Style.RESET_ALL}{Back.GREEN} {W}### {Style.RESET_ALL} {G}PC Name:{Y} {hostname}")
    print ( f" {Back.CYAN}{M}[+] Version.1.0 {Back.WHITE} {Y}Lagos {Back.WHITE}{G}Nigeria {Style.RESET_ALL} {G}IP Address:{Y} {ip}")
    print (f"{W}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{Style.RESET_ALL}") 
    current_time = datetime.datetime.now().strftime("%H:%M:%S")   
    print (f"{W}{italic}Current Time:{italic2}", f"{Y}{current_time}")
    print (f"{G}[{Y}!{G}] {C}P{Y}2{M}-{R}A{B}r{W}a {B}Wide Range All In One Tools.\n{G}[{Y}!{G}]{C} Get IP Address Info / Domain Info And Many More.{Style.RESET_ALL}")
    



def Exit():
    print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main Menu ]""")
    print(f"{R}[!]{Y}Warning!{Style.RESET_ALL} {R}Are you sure you want to Exit? [!]{Style.RESET_ALL}")
    choice = input(f" Type 'exit' to confirm: ")
    if choice == "X" :
       Display_menu()
    if choice.lower() == "exit":
        print(Back.RED +f"[-]Exiting P2-Ara GOOD BYE!...[-]") 
        sys.exit(0)

def timer(timeLeft):
    while timeLeft > 0:
        #print(timeLeft, end='')
        time.sleep(1)
        timeLeft = timeLeft - 1


def Generate_QR_code():
    Display_banners()
    print(f"{Style.BRIGHT}{Y}Welcome... what did you want to convert to QR_CODE?? ")
    print (f"{C}//////////////////////////////////////////////////////////////////////")
    print (" ")
    data = input(f"{M}Enter anything to generate QR_CODE:>>  {Style.RESET_ALL}")
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    Image = qr.make_image(file="Black", back_color="GreenYellow")
    Image.save("qr_code.png")
    print (f"{Y}{italic}Processing Please Wait...{italic2}{Style.RESET_ALL}")
    print (f"{G}QR_CODE Generated Successfully{tick} Check your FOLDER")
    print (" ")
    print (f"Press Enter to continue ....")
    

def Domain_info():
    Display_banners()
    print(" ")
    print(f"{Y}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    domain = input(f"{C}Enter Domain / URL to get the info: {Style.RESET_ALL}")
    domain_info = whois.whois(domain)
    for key, value in domain_info.items():
        print(key, ':', value)
        print (f"{G}[+]{domain} info Completed successfully [+]")
        print (f"Press Enter to continue ....")
      



def Count_file():
    Display_banners()
    print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main Menu ]""")
    print (f"Kindly Enter The Path / Directorias You Want To Count")
    print(" ")
    print (f"********************************")
    PATH = input(f"{M}Enter The Path You Want to Count: {Style.RESET_ALL}")
    print (f"********************************")
    files, dirs = 0, 0
    for root, dirnames, filenames in os.walk(PATH):
        print(f"{G}[{Y}*{G}]looking in... {Y}{root}{Style.RESET_ALL}")
        dirs += len(dirnames)
        files += len(filenames)
    print (f"{W}[+]Files:  {Back.BLUE}[{files}]")
    print (f"{W}[+]Directories: {Back.YELLOW}[{dirs}]")
    print (f"{W}[+]Total:  {Back.GREEN}[{files + dirs}]")
    print (f"{G}[{Y}*{G}] Total number of file in {PATH} is: [{files}], and all Directories is: [{dirs}], Counting file Succcessfully Completed!{G}[{Y}*{G}]{Style.RESET_ALL}")
    print (f"Press Enter to continue ....")
   
#
def DirCrawler():
   try:
       target_url = input("Enter Target URL: ")
       if not target_url.startswith("http://") and not target_url.startswith("https://"):
           target_url = "https://" + target_url
       file_path = input("Enter file path:")
       with open(file_path, "r") as wordlist_file:
           print (f"Reading wordlist file...")
           for line in wordlist_file:
               word = line.strip()
               if word:
                   print (f"Trying directory: {word}")
                   test_url = f"{target_url} / {word}"
                   try:
                       response = requests.get(test_url)
                       print (f" status code: {response.status_code}")
                       if response.status_code == 200: 
                           print ("[+] Discoverd URL -->  {test_url}")
                           with open("discuverd_url.txt", "a") as f:
                               f.write(test_url + "\n")
                       else: 
                           print("{test_url}return status code {response.status_code}")
                   except requests.exceptions.RequestException as e:
                       print (f"Error trying {test_url}: {e}")
               else:
                    print ("Skiping emty linem in wordlist...")
   except FileNotFoundError:
       print (f"Wordlist file not found.")
   except Exception as e:
       print ("An Error occured:", str(e))
#

def ip_info():
    Display_banners()
    print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main Menu ]""")     
    print(f"{G}[{Y}::{G}]IP Address Infomation Tools{G}[{Y}::{G}]{Style.RESET_ALL}")
    print(f"{Y}-----------------------------------------------------{Style.RESET_ALL}")
    choice = input(f"{C}Do you want to get info about your own IP Address or a Specific IP? {Back.YELLOW}(own/specific): {Style.RESET_ALL}" )
    try:
        if choice == "X":
            Display_menu()
        elif choice.lower() == "own":
            ip_address = requests.get("https://ident.me", verify=False).text
        elif choice.lower() == "specific":
            ip_address = input(f"{M}Enter the target IP address: {Style.RESET_ALL}")

        else:
            print(f"invalid choice. Exiting.")
            return
        print(f" {B}[*]Your ip address is : {G}{ip_address}{Style.RESET_ALL}")
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()
        ip_info_response = response.json()
        print(f"{G}IP:  {Y}{ip_info_response['query']}{Style.RESET_ALL}")
        print(f"{G}City: {Y}{ip_info_response['city']}{Style.RESET_ALL}")
        print(f"{G}ISP:  {Y}{ip_info_response['isp']}{Style.RESET_ALL}")
        print(f"{G}Country: {Y}{ip_info_response['country']}{Style.RESET_ALL}")
        print(f"{G}Region: {Y}{ip_info_response['region']}{Style.RESET_ALL}")
        print(f"{G}Timezone: {Y}{ip_info_response['timezone']}{Style.RESET_ALL}")
        print(f"{G}Latitude: {Y}{ip_info_response['lat']}{Style.RESET_ALL}")
        print(f"{G}Longitude: {Y}{ip_info_response['lon']}{Style.RESET_ALL}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occuried {http_err}..")
    except Exception as e:
        print (f"An error occurred: {e}")

#
def Remove_BG():
    try:
        Display_banners()
        image_path = input(f"{C}Enter Image path to Remove BG:{Style.RESET_ALL}")
        with open(image_path, 'rb') as i:
            result = remove(i.read())
            with open('output.png', 'wb') as o:
               o.write(result)

        print(f"{G}[{Y}<<>>{G}] Backgroun Remove Successfully saved to output.png {G}[{Y}<<>>{G}]{Style.RESET_ALL}") 
    except Exception as e:
        print(f"An error occured: {e}")
#
def Scrape_emails():
    try:
        Display_banners()
        print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main Menu ]""")
        print (f"{R}[{Y}@{R}]{W}**************************************************{R}[{Y}@{R}]")
        print (f"{C}Welcome Kindly Enter The Website Url or Ip-Address Below To Extract Emails.{Style.RESET_ALL}")
        url = input(f"{R}Enter  Target Url / Ip{Style.RESET_ALL}:>> ")
        if url ==  "X":
           Display_menu()

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko ) Chrome/91.04472.164 Safari/537.36'

}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
            if emails:
                print (f"{Y}Extracted Emails:")
                with open(f"Extracted_Emails.txt", "a") as file:
                    for email in emails:
                        print (email)
                        file.write(email + "\n")
                print (f"{G}Emails Saved to Extracted_emails.txt. Total emails: {Back.CYAN}{len(emails)}")
                user_choice = input(f"#:> ")
                if user_choice == "X":
                   Display_menu()

            else:
                print (f"{R}[!]No emails found.[!]")
        else:
            print (f"{R}Failed to retrieve webpage. status code:", response.status_code)

    except Exception as e:
        print (f"{R}An error occurred:", str(e))

#
def Buy_tools():
    Display_banners()
    print (f"{G}Welcome Kindly fill the form below to continue!")
    Buyer_name = input(f"{C}Enter yout name: ")
    Buyer_ID = input(f"{C}Enter yout ID: ")
    Buyer_email = input(f"{C}Enter your email: ")
    Message = input(f"{C}Enter msg:> I'AM {Buyer_name},{Buyer_ID},with Email {Buyer_email}, i want to Buy ")
    print (f"{G}Hello {Buyer_name}, ID:{Buyer_ID}" "\n" f"{W}We will get intouch with you soon via your email {Buyer_email} THANK YOU!")
    #sendmail(xxx,xxxx,msg())
    print (f"{M}we just recive your mail will get back to you ASAP!")



def Other_tools():   
    Display_banners()
    print(f" ")   
    print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main  Menu ]""") 
    print(f"{Back.CYAN}Other Tools:")
    print(f""" {Y}
  [{W}+{Y}] {C}WELCOME TO [\u00A3yand3r] GET ALL KINDS OF ADVANCE WEBSITE / TOOLS 100% RELIABLE {Y}[{W}+{Y}]
{G}[{R}*{G}]{Y}-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --{G}[{R}*{G}]
{Y}~>> {G}[{W}1{G}]{C}Advance SMS / EMAIL Sender  {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}2{G}]{C}Advance EMAIL BOOMBER       {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}! 
{Y}~>> {G}[{W}3{G}]{C}Advance Stealer             {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}4{G}]{C}Advance Spyware             {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}5{G}]{C}Advance RAT                 {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}6{G}]{C}Advance Trojan              {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}7{G}]{C}Advance BTC_Cleper          {G}[{W}{Style.RESET_ALL}{italic} PREMIUM {tick}{G}]{italic2}!
{Y}~>> {G}[{W}8{G}]{C}CUSTUME T00ls and many more!!!
{M}Kindly select your choice below! {Back.GREEN}\u00A3yand3r{Style.RESET_ALL}
{G}[{R}*{G}]{Y}-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --{G}[{R}*{G}]
{Style.RESET_ALL}""")
    print(f" ")
    user_choice= input(f"{Y}Enter choice: ")
    if user_choice == "1":
       Buy_tools()
    elif user_choice == "2":
         Buy_tools()
    elif user_choice == "3":
         Buy_tools()
    elif user_choice == "4":
         Buy_tools() 
    elif user_choice == "5":
         Buy_tools() 
    elif user_choice == "6":
         Buy_tools() 
    elif user_choice == "7":
         Buy_tools() 
    elif user_choice == "8":
         Buy_tools()
    elif user_choice == "X" or "x":
         Display_menu()
    else:
        print (f"{R}[-]Invalid option please try again.")
         


def vali_email():
    Display_banners()
    print(f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main  Menu ]""")   
    print(f"  ")
    print(f"{C}-----------------------------------------{Style.RESET_ALL}")
    print(f"{G}||     {G}[{Y}*{G}]Email Validator{G}[{Y}*{G}]     ||{Style.RESET_ALL}")
    print(f"{C}-----------------------------------------{Style.RESET_ALL}")
    print(f"{C}========================================={Style.RESET_ALL}")
    print(f" ")
    print(f"{C}1. Single Email{Style.RESET_ALL}")
    print(f"{C}2. Wordlist of Emails{Style.RESET_ALL}")
    choice = input(f"{Y}[#]Choose an option:>> {Style.RESET_ALL}")
 
    tick = "\u2714"
    cross = "\u274C"
    if choice == "1":
        email = input(f"{C}Enter email : ")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        result = bool(re.match(pattern, email))
        print(f"{email}: {tick} Valid " if result else f"{email}: {cross} Not Valid")

    elif choice == "2":
        wordlist = input(f"{M}Enter the path to the wordlist file: ")
        valid_emails = []
        invalid_emails = []
        try:
            with open(wordlist, 'r') as file:
                emails = file.readlines()
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                for email in emails:
                    email = email.strip().lower()
                    if email:
                         print(f"{W}{email}:{tick}{G} Valid" if bool(re.match(pattern, email)) else f"{W}{email}:{cross} {R}Not Valid")
                         valid_emails.append(email)

                         invalid_emails.append(email)

                with open(f"valid_emails.txt", "w") as valid_file:
                    for email in valid_emails:
                        valid_file.write(f"{email}:{tick}Valid"+"\n" if bool(re.match(pattern, email)) else "  " )


                with open(f"invalid_emails.txt", "w") as invalid_file:
                    for email in invalid_emails:
                        invalid_file.write(f"\n"if bool(re.match(pattern, email)) else f" {email}: {cross}Not Valid"+"\n")
               
        except FileNotFoundError:
            print(f"{R}File not found.")
    elif choice == "X" or "x":
        Display_menu()
    else:
        print(f"{R}[-]Invalid option. Try Again!")


def Check_email():
    email = input("Enter the email: ")
    result = subprocess.run(["holehe", email], capture_output=True, text=True)
    print(result.stdout)

def generate_pass():
    Display_banners()
    print (f"""                                                                          {Back.MAGENTA}{W} Press 'X' to go Back to {Back.WHITE}{G}[ Main Menu ]{Style.RESET_ALL} """)
    print(f"""{R}###- - - - - - - -{Y}###{R}- - - - - - - - - -{Y}###{R} - - -""")
    print(f"{Y}- - - - - - - - - - - - - - - - - - - - - - - - - -- -- - -- -- -")
    print(f" {G}[{Y}Info:{G}] {W}Kindly Enter the length of password you want to generate below!")
    print(f" ")
    length = input(f"{M}Enter password length (default is 12):>> {Style.RESET_ALL}") or 12
    if length == "X" or "x":
       Display_menu()
    else:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break  
    print(f"{G}[{Y}+{G}]Generated Password:>>  {W}{password}")
    print(f"{Back.CYAN}Password generated 100% successfully")
    user_choice = input(f"{M}#:>> ")
    if user_choice == "X" or "x":
       Display_menu()
    else:
       print (f"{M}{italic}Press Enter to continue...{italic2}")   
    
    

def PDF_2_Audio():
    path = open('acd.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    speak = pyttsx3.init()
    for pages in range(pdfReader.numPages):
        text = pdfReader.getPage(pages).extractText()
        speak.say(text)
        speak.runAndWait()
    speak.stop()

def About_Us():
    Display_banners()
    print (f"""                                                                          {Back.MAGENTA}{W} Press X to go Back to{Back.WHITE}{G}[ Main Menu ]{Style.RESET_ALL}""")
    print (f" ")
    print (f"""                          {G}[{W}#{G}]{W}>>>>>.>>>{G}#{W}#{G}#::::::::{G}#{W}#{G}#{W}:::::::{G}#{W}#{G}#<<<.<<<<<{W}{G}[{W}#{G}] 

                      ::>> WE ARE {Back.GREEN}[{W}\u00A3yand3r {tick}]{W}{Style.RESET_ALL} Nigeria Leading TECH Experts.

                      ::>> {W}We Build All kinds of Advance T00ls / Software.

                      ::>> {W}WE ARE \u00A3yand3r, We're Here In {R}[ {Y}Lagos{R}]:{G}Nigeria, {W}The TECH HUB Of Africa!.
 
                      ::>> {W}WE Are {G}NIGERIA.{G}#{W}#{G}#

                      ::>> {W}Contact Us on {C}{italic}Telegram. @\u00A3yand3r{italic2}{W} For More Info....

                    ::>>{G}[#]__________________________________________{W}:: :: ::{G}______________________________________[#]

""")
    print (f" ")
    user_choice = input(f"#:>> ")
    if user_choice == "X":
       Display_menu()
    else:
       print (f"{M}Press enter to continue... ")


def Display_menu():
    Menu = [Main_menu2,Main_menu]
    random.choice(Menu)()

def Pdf_to_docx_audio_text():
    Display_banners()
    print (" ")
    print (f"{C}1. PDF To Audio{Style.RESET_ALL}")
    print (f"{C}2. PDF To Txt{Style.RESET_ALL}")
    print (f"{C}3. PDF To Doc{Style.RESET_ALL}")

    print (f" ")
    user_choice = input(f"{Y}[#]Choose an option:>> {Style.RESET_ALL}")
    if user_choice == "1":
       Pdf2_Audio()

    elif user_choice == "2":
          Pdf2_Txt()
          
    elif user_choice == "3":
         Pdf2_Doc()
    else:
        print (f"{R}[-]Invalid option please try again.")
 

#
def Pdf2_Audio():
    print (f"{M}Kindly Enter The File Name To Convert Pdf To Audio Below")
    print (f" ")
    file_path = input(f"Enter file name here:> ")
    print (f"{R}Coming soon...")

def Pdf2_Txt():
    print (f"{B}Kindly Enter The File Name To Convert Pdf To Txt Below")
    print (f" ")
    file_path = input(f"Enter file name here:> ")
    print (f"{G}Coming soon...")


def Pdf2_Doc():
    print (f"{Y}Kindly Enter The File Name To Convert Pdf To Doc Below")
    print (f" ")
    file_path = input(f"Enter file name here:> ")
    print (f"{C}Coming soon...")

#

def Extract_txt_from_image_pdf():
    Display_banners()
    print (f" ")
    print (f"{Y}1. Extract txt from image{Style.RESET_ALL}")
    print (f"{Y}2. Extract txt from pdf {Style.RESET_ALL} ")
    user_choice = input(f"{M}[#]Choose an option:>> {Style.RESET_ALL}")
    if user_choice == "1":
       Extract_txt_from_image()
       
    elif user_choice == "2":
         Extract_txt_from_pdf()
    else:
        print (f"{R}[-]Invalid option please try again.")
        

#
def Extract_txt_from_pdf():
    print (f"{B}Coming soon...")

def Extract_txt_from_image():
    print (f"{Y}Coming soon...")
#
def Main_menu2():
    Display_banners()
    info()
    while True:
       print(f" ")
       print(f"{C}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {Style.RESET_ALL}")
       print(f"{W}    :: :: ::    {Y}[{C}*{Y}] Main Menu [{C}*{Y}]{W}    :: :: ::{Style.RESET_ALL} ")
       print(f"{C}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {Style.RESET_ALL}")
       print(f" ")
       print(f"{G}-->> {C}[{W}0{C}]{G}==>> {C}Help                           {G}->> {C}[{W}11{C}]{G}==>> {W}DirCrawler   ")
       print(f"{G}-->> {C}[{W}1{C}]{G}==>> {C}About Us                       {G}->> {C}[{W}12{C}]{G}==>> {W}PDF To Docx/Audio/Text")
       print(f"{G}-->> {C}[{W}2{C}]{G}==>> {W}Email Scraper                  {G}->> {C}[{W}13{C}]{G}==>> {W}Generate QR_Code ")
       print(f"{G}-->> {C}[{W}3{C}]{G}==>> {W}Web Scraper                    {G}->> {C}[{W}14{C}]{G}==>> {W}Count File & Folder ")
       print(f"{G}-->> {C}[{W}4{C}]{G}==>> {W}Get Domain Info                {G}->> {C}[{W}15{C}]{G}==>> {W}ZipFile")
       print(f"{G}-->> {C}[{W}5{C}]{G}==>> {W}Remove_BG                      {G}->> {C}[{W}16{C}]{G}==>> {W}Network Scanning")
       print(f"{G}-->> {C}[{W}6{C}]{G}==>> {W}Email Validator                {G}->> {C}[{W}17{C}]{G}==>> {W}Extract Txt From Image/PDF")
       print(f"{G}-->> {C}[{W}7{C}]{G}==>> {W}IP Address Info                {G}->> {C}[{W}18{C}]{G}==>> {W}Download YouTube Video")
       print(f"{G}-->> {C}[{W}8{C}]{G}==>> {W}Password Generator             {G}->> {C}[{W}19{C}]{G}==>> {C}Other Tools")
       print(f"{G}-->> {C}[{W}9{C}]{G}==>> {W}SubDomain Crawler              {G}->> {C}[{R}20{C}]{G}==>> {R}Exit")
       print(f"{G}->> {C}[{W}10{C}]{G}==>> {W}Link Shortener ")
 
       print(f" ")
       user_choice = input(f"{italic}{W}root@P2-Ara{Y}~#: {italic2}{Style.RESET_ALL}")
       if user_choice == "0":
            Help()
 
            input()
            continue
       elif user_choice == "1":
            About_Us()

            input()
            continue
       elif user_choice == "2":
            Scrape_emails()
            
            input()
            continue
       elif user_choice == "3":
            Web_scraper()
       
            input()
            continue
       elif user_choice == "4":
            Domain_info()

            input()
            continue
       elif user_choice == "5":
            Remove_BG()

            input()
            continue
       elif user_choice == "6":
            vali_email()

            input()
            continue
       elif user_choice == "7":
            ip_info()

            input()
            continue
       elif user_choice == "8":
            generate_pass()

            input()
            continue
       elif user_choice == "9":
            SubC()

            input()
            continue
       elif user_choice == "10":
            Links_shortener()

            input()
            continue
       elif user_choice == "20":
            Exit()
    
            input()
            continue
       elif user_choice == "13":
            Generate_QR_code()
    
            input()
            continue
       elif user_choice == "14":
            Count_file()

            input()
            continue
       elif user_choice == "15":
            ZipF()

            input()
            continue
       elif user_choice == "16":
            Network_Scanning()

            input()
            continue
       elif user_choice == "11":
            DirCrawler()

            input()
            continue
       elif user_choice == "12":
            Pdf_to_docx_audio_text()
    
            input()
            continue
       elif user_choice == "14":
            Count_file()

            input()
            continue
       elif user_choice == "19":
            Other_tools()

            input()
            continue   
       elif user_choice == "17":
            Extract_txt_from_image_pdf()

            input()
            continue   
       elif user_choice == "18":
            Download_video()
       else:
           print (f"{R}[!]Invalid option please try again.")



#

def Main_menu():
    Display_banners()
    info()
    while True:
       print(f" ")
       print(f"{Y}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {Style.RESET_ALL}")
       print(f"{W}    :: :: ::    {C}[{Y}*{C}] Main Menu [{Y}*{C}]{W}    :: :: ::{Style.RESET_ALL} ")
       print(f"{Y}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {Style.RESET_ALL}")
       print(f" ")
       print(f"{G}-->> {Y}[{W}0{Y}]{G}==>> {Y}Help ")
       print(f"{G}-->> {Y}[{W}1{Y}]{G}==>> {Y}About Us")
       print(f"{G}-->> {Y}[{W}2{Y}]{G}==>> {W}Email Scraper")
       print(f"{G}-->> {Y}[{W}3{Y}]{G}==>> {W}Web Scraper")
       print(f"{G}-->> {Y}[{W}4{Y}]{G}==>> {W}Get Domain Info")
       print(f"{G}-->> {Y}[{W}5{Y}]{G}==>> {W}Remove_BG")
       print(f"{G}-->> {Y}[{W}6{Y}]{G}==>> {W}Email Validator")
       print(f"{G}-->> {Y}[{W}7{Y}]{G}==>> {W}IP Address Info")
       print(f"{G}-->> {Y}[{W}8{Y}]{G}==>> {W}Password Generator")
       print(f"{G}-->> {Y}[{W}9{Y}]{G}==>> {W}SubDomain Crawler")
       print(f"{G}->> {Y}[{W}10{Y}]{G}==>> {W}Link Shortener")
       print(f"{G}->> {Y}[{W}11{Y}]{G}==>> {W}DirCrawler")
       print(f"{G}->> {Y}[{W}12{Y}]{G}==>> {W}PDF To Docx/Audio/Text ")
       print(f"{G}->> {Y}[{W}13{Y}]{G}==>> {W}Generate QR_Code")
       print(f"{G}->> {Y}[{W}14{Y}]{G}==>> {W}Count File & Folder")
       print(f"{G}->> {Y}[{W}15{Y}]{G}==>> {W}ZipFile")
       print(f"{G}->> {Y}[{W}16{Y}]{G}==>> {W}Network Scanning")
       print(f"{G}->> {Y}[{W}17{Y}]{G}==>> {W}Extract Txt From Image/PDF")
       print(f"{G}->> {Y}[{W}18{Y}]{G}==>> {W}Download YouTube Video")
       print(f"{G}->> {Y}[{W}19{Y}]{G}==>> {Y}Other Tools")
       print(f"{G}->> {Y}[{R}20{Y}]{G}==>> {R}Exit")

       print(f" ")
       user_choice = input(f"{italic}{W}root@P2-Ara{Y}~#: {italic2}{Style.RESET_ALL}")
       if user_choice == "0":
          Help()

          input()
          continue
       elif user_choice == "1":
            About_Us()
            print(" ")

            input()
            continue
       elif user_choice == "2":
            Scrape_emails()
            
            input()
            continue
       elif user_choice == "3":
            Web_scraper()

            input()
            continue
       elif user_choice == "4":
            Domain_info()

            input()
            continue
       elif user_choice == "5":
            Remove_BG()

            input()
            continue
       elif user_choice == "6":
            vali_email()

            input()
            continue
       elif user_choice == "7":
            ip_info()

            input()
            continue
       elif user_choice == "8":
            generate_pass()

            input()
            continue
       elif user_choice == "9":
            SubC()

            input()
            continue
       elif user_choice == "10":
            Links_shortener()

            input()
            continue
       elif user_choice == "20":
            Exit()
    
            input()
            continue
       elif user_choice == "13":
            Generate_QR_code()
    
            input()
            continue
       elif user_choice == "14":
            Count_file()

            input()
            continue
       elif user_choice == "15":
            ZipF()

            input()
            continue
       elif user_choice == "18":
            Download_video()

            input()
            continue
       elif user_choice == "12":
            Pdf_to_docx_audio_text()

            input()
            continue
       elif user_choice == "17":
            Extract_txt_from_image_pdf()

            input()
            continue   
       elif user_choice == "19":
            Other_tools()

            input()
            continue   
       elif user_choice == "11":
            DirCrawler()

            input()
            continue   
       elif user_choice == "16":
            Network_Scanning()
       else:
           print (f"{R}[!]Invalid option please try again.")




#
def Help():
    Display_banners()
    print (f"""                                                                          {Back.MAGENTA}{W} Press Enter to go Back to{Back.WHITE}{G}[ Main Menu ]{Style.RESET_ALL}""")
    print (f"Help / Manual Page:")
    print (f"{M}[{G}${M}]Welcome To {W}[{R}P{B}2{W}-{R}A{Y}r{C}a{W}] Manual Page, Here You Get Overview Of All T00ls And Their Functionality/ Usage")
    print (f" ")
    console = Console()
    table = Table(title=f"{Y}T00ls Overview")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Command", justify="center", style="green")
    table.add_column("What it does", justify="center", style="cyan")

    table.add_row("0", "Help", " command[0]", "This is the manual page for [P2-Ara], its list all available tools and their usage")
    table.add_row("1", "About Us", " command[1]","This page explain how to get intorch with us \u00A3yand3r")
    table.add_row("2", "Email Scraper","command[Enter Target Url]"," This tools help you collect email from any website you provide")  
    table.add_row("3", "Web Scraper", "60")
    table.add_row("4", "Get Domain Info", "60")
    table.add_row("5", "Remove_BG", "60")
    table.add_row("6", "Email Validator", "60")
    table.add_row("7", "IP Address Info", "60")
    table.add_row("8", "Password Generator", "60")
    table.add_row("9", "SubDomain Crawler", "60")
    table.add_row("10", "Link Shortener", "60")
    table.add_row("11", "DirCrawler", "60")
    table.add_row("12", "PDF To Docx/Audio/Text ", "60")
    table.add_row("13", "Generate QR_Code", "60")
    table.add_row("14", "Count File & Folder", "60")
    table.add_row("15", "ZipFile", "60")
    table.add_row("16", "Network Scanning", "60")
    table.add_row("17", "Extract Txt From Image / PDF", "60")
    table.add_row("18", "Download YouTube Video", "60")
    table.add_row("19", "Other Tools", "60")
    table.add_row("20", "Exit", "60")

    console.print(table)
    print (" ")
    print (f"{C}{italic}Press Enter To Continue....{italic2}")
#

def Web_scraper():
    try:
       Display_banners()
       print (f"""                        {M}[{Y}={M}]Welcome To \u00A3yand3r Web Scraper Dashbord {M}[{Y}={M}]
                {Y}<<--{W}Kindly Enter Target Website URL to Extract Website Links{Y}-->>
""")
       print (f"{Y}------------------------------------------------------")
       url = input(f"{W}Enter the target URL: {Style.RESET_ALL}")
       print (f"{Y}______________________________________________________")
       if not url.startswith("http"):
           url = f"https://{url}"
       headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko ) Chrome/91.04472.164 Safari/537.36'
}
       response = requests.get(url,headers=headers)
       if response.status_code == 200:
           soup = BeautifulSoup(response.content, "html.parser")
           title = soup.title.text
           links = [link.get("href") for link in soup.find_all("a") if link.get("href")]
           with open("WebExtraction.txt", "a") as file:
              file.write(f"{Y}Title: {title}\n\n")
              file.write(f"{G}Links\n")
              for link in links:
                  file.write(f"{link}\n")
           print (f"{C}Extraction saved to {G}WebExtraction.txt")
           print (f"{W}Web Extraction for {Y}{url} {W}Completed Successfully {italic}Press Enter To Continue...{italic2}")
       else:
           print (f"{R}[-]Failed to Extract webpage. status code: {response.status_code}[-]")
    except Exception as e:
        print (f"{R}[!]An error occurec: {e}")
       
 #
def request(url):
  try:  
      return requests.get("https://" + url)
  except requests.exceptions.ConnectionError:
       pass

def SubC():
  Display_banners()
  print(f" ")
  print(f"{G}[Info]{C} Kindly Enter Domain / Website Url {Style.RESET_ALL}")
  print(f"{R}=============================================={Style.RESET_ALL}")
  print(f"{G}[{Y}??{G}] Welcome to Sub_Domain_Crawler Dashbord{G}[{Y}??{G}]{Style.RESET_ALL}")
  print(f"{R}=============================================={Style.RESET_ALL}")
  print(f" ")
  target_url = input (f"{Y}Enter target Url: {Style.RESET_ALL}")
  wordlist_file = input(f"{Y}Enter Your WordList file name: {Style.RESET_ALL}")       
  print ( f"{G}======={Y} Strating SubCrawler Now! {G}======={Style.RESET_ALL}")
  with open (wordlist_file, "r")as file:
      for line in file:
         word = line.strip() 
         test_url = word +"."+ target_url
         response = request(test_url)
         if response:
            print (f"{G}[{Y}+{G}] Discoverd subdomain --->>> {Style.RESET_ALL}"+ test_url)
         else:
            print (f"{R}Error: No subdomain {Style.RESET_ALL}" + " " + word + " "+ "from  " + target_url)
  print (f"{C}====[+] Sub_Domain_Crawlling For " + " " + target_url + "" + "{G}completed")
  print (f"{W}Press Enter To continue...")
  

def Links_shortener():
    Display_banners()
    print(f"{M}[$]>>>>-->>Link Shortener By:{C}\u00A3yand3r {Style.RESET_ALL}{M}<<--<<<<[$]{Style.RESET_ALL}")
    print(f""" 
    >-- Kindly enter the Link / URL you want to shortened bellow --<
""" )
    print("*****************")
    link = input(Back.BLUE +f"Enter the link:: {Style.RESET_ALL}")
    shortener = pyshorteners.Shortener()
    shortened_link = shortener.tinyurl.short(link)
    print("*****************")
    print (f"{G}Shortened Link:{Style.RESET_ALL}",shortened_link)
    if shortened_link:
       print(f"{C}[~] {Y}{link}{C} link shortened Successfullly [~]{Style.RESET_ALL}" )
       print(f"""{B} 
       === === Press Enter to continue...=== ===
""")
    else:
       print(f"{R}[-]Failed to Shortened {link}.[-]{Style.RESET_ALL} {Y}Check your internet connection and try again {R}[!]")



if __name__=='__main__':
    Display_menu()  
    
