import colorama
import time, sys
from colorama import Fore, Style
Green = Fore.GREEN
Yellow =Fore.YELLOW
Blue = Fore.BLUE
def show_banner() :
    banner = print(f'''
{Fore.YELLOW}
    __  __        _       ____          __       ___
   / / / /  __   | |     / / /_  ____ _/ /______/   |  ____  ____
  / /_/ / |/_/   | | /| / / __ \/ __ `/ __/ ___/ /| | / __ \/ __ \
 / __  />  <     | |/ |/ / / / / /_/ / /_(__  ) ___ |/ /_/ / /_/ /
/_/ /_/_/|_|     |__/|__/_/ /_/\__,_/\__/____/_/  |_/ .___/ .___/
                    By Mr Juice                    /_/   /_/
    
    Coded➠ by Mr Juice
    Follow On Instagram link is below
    Chat Me➠ https://bio.link/mrjuice
    
Subscribe To My YouTube Channel
➠ Mr Juice OFC and Infinity Tech
    ''')
show_banner()
def delay_print(s) :
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.095)
def num():
    while True:
        number = input("Enter number to hack : +263")
        numberr = "+263" +number
        lenfind = len(number)
        if (number.isnumeric()):
            if (lenfind < 10):
                print(f"{Fore.RED}Number must be atleast 10 digits")
            elif (lenfind > 10):
                print(f"{Fore.RED}Number must be less than 10 digits")
            elif (lenfind==10):
                delay_print(f"{Fore.YELLOW}Signalling " + numberr + " . . .\n")
                delay_print(f"{Fore.YELLOW}Checking the network availability . . .\n")
                delay_print("Connection successfull with " + numberr+"\n")
                print(f"{Fore.BLUE}****MAKE SURE YOU REQUESTED THE OTP****\n")
                delay_print(f"{Fore.YELLOW}Gaining access to SMS . . . ( This will take some time )\n")
                time.sleep(3)
                delay_print(f"{Fore.GREEN}Access gained to SMS of " + numberr+"\n")
                delay_print(f"{Fore.YELLOW}Reading SMS . . .\n")
                print(f"{Fore.GREEN}Whatsapp OTP found ! !\n")
                otp = input("Press '1' to show the OTP : ")
                print(f"{Fore.CYAN}USE THE OTP CODE AND LOGIN\n")
                print(f"{Fore.RED}Follow and Support Me By Subscribing and following on Instagram. . . ")
            else:
                print("Unexpected error occured Check➠ http://t.me/HackersBot_2022bot for a solution")
        else: print(f"{Fore.RED}Number format is incorrect")
        num()

num()



