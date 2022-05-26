try:
  from colorama import *
  import psutil
  import os
  import sys
except ModuleNotFoundError:
  print("[!] Installing Missing Modules [!]")
  os.system("pip3 install psutil")
  os.system("pip3 install colorama")
  
#----------------------------------Global program functions-----------------------------------------------
def exit():
    os.system("cls") #clears console
    sys.exit()

def clear_screen():
    os.system("cls")

#----------------------------------Interface Functions-----------------------------------------------

def app_logo():
  ascii_menu = """
▄▀█ █▄░█ ▀█▀ █ ▄▄ █▀▀ █░█ █▀▀ ▄▀█ ▀█▀   █▀▄ █▀▀ ▀█▀ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
█▀█ █░▀█ ░█░ █ ░░ █▄▄ █▀█ ██▄ █▀█ ░█░   █▄▀ ██▄ ░█░ ██▄ █▄▄ ░█░ █▄█ █▀▄"""
  print(Fore.BLUE + ascii_menu + Fore.RESET)
  print(Fore.BLUE + "                          github -> teddyscrewthis" + Fore.RESET)
  print("")
  


def menu():
  print("[0] Exit")
  print("[1] Easy Anti-Cheat")
  print("[2] Battleye")
  print("")

  option = input("Enter number of process you want to check ---> ")
  if option == "0":
    return exit()
  if option == "1":
      EAC()
  elif option == "2":
      Battleye()  

def main_menu():
    app_logo()
    menu()
  
#----------------------------------Main function-----------------------------------------------

def check(processName): #thank u stackoverflow
  for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except(psutil.NoSuchProcess):
            print("Unknown Error")
            return False

def EAC():

    clear_screen()
    app_logo()

    proc = check('EasyAntiCheat_EOS')

    if proc == None:
      print(Fore.RED + "[!] Easy Anti-Cheat is not running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      clear_screen()
      return main_menu()
      
    elif proc == True:
      print(Fore.GREEN + "[!] Easy Anti-Cheat is running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      clear_screen()
      return main_menu()

def Battleye():

    clear_screen()
    app_logo()

    proc = check('BEService')

    if proc == None:
        print(Fore.RED + "[!] Battleye is not running [!]" + Fore.RESET)
        input("Press any key to continue ---> ")
        clear_screen()
        return main_menu()
      
    elif proc == True:
        print(Fore.GREEN + "[!] Battleye is running [!]" + Fore.RESET)
        input("Press any key to continue ---> ")
        clear_screen()
        return main_menu()

if __name__ == "__main__":
    main_menu()
