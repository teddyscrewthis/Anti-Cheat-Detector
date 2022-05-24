#I have to put the actual process names later. Cant do it rn as I'm not on my desktop.

try:
  from colorama import *
  import psutil
  import os
  import sys
except ModuleNotFoundError:
  print("[!] Installing Missing Modules [!]")
  os.system("pip3 install psutil")
  os.system("pip3 install colorama")
  
def app_logo():
  ascii_menu = """
▄▀█ █▄░█ ▀█▀ █ ▄▄ █▀▀ █░█ █▀▀ ▄▀█ ▀█▀   █▀▄ █▀▀ ▀█▀ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
█▀█ █░▀█ ░█░ █ ░░ █▄▄ █▀█ ██▄ █▀█ ░█░   █▄▀ ██▄ ░█░ ██▄ █▄▄ ░█░ █▄█ █▀▄"""
  print(ascii_menu)
  
  
  
def menu():
  print("[0] Exit")
  print("[1] Test Software")
  print("[2] Easy Anti-Cheat")
  print("[3] Battleye")
  print("[4] Richote")
  print("[5] Help")
  

def main_menu():
  
  ascii_menu = """
▄▀█ █▄░█ ▀█▀ █ ▄▄ █▀▀ █░█ █▀▀ ▄▀█ ▀█▀   █▀▄ █▀▀ ▀█▀ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
█▀█ █░▀█ ░█░ █ ░░ █▄▄ █▀█ ██▄ █▀█ ░█░   █▄▀ ██▄ ░█░ ██▄ █▄▄ ░█░ █▄█ █▀▄"""
  print(ascii_menu)
  print("")
  print("[0] Exit")
  print("[1] Custom")
  print("[2] Easy Anti-Cheat")
  print("[3] Battleye")
  print("[4] Richote")
  print("[5] Help")
  
def check(processName):
  
  for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def EAC():
    if check('EasyAntiCheat'):
      print(Fore.RED + "[!] Easy Anti-Cheat is running [!]" + Fore.RESET)
      
      input("Press any key to continue ---> ")
      return main_menu()
      
    else:
      print(Fore.GREEN + "[!] Easy Anti-Cheat is not running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
  
def Battleye():
    if check('Battleye'):
      print(Fore.RED + "[!] Battleye is running [!]" + Fore.RESET)
      
      input("Press any key to continue ---> ")
      return main_menu()
      
    else:
      print(Fore.GREEN + "[!] Battleye is not running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
    
def richocet():
  if check('ricochet'):
      print(Fore.RED + "[!] ricochet is running [!]" + Fore.RESET)
      
      input("Press any key to continue ---> ")
      return main_menu()
      
    else:
      print(Fore.GREEN + "[!] ricochet is not running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
    
def custom():
  test_proc = input("Enter Proc name you want to test ---> ")
  
  if check(test_proc):
      print(Fore.RED + f"[!] {test_proc} is running [!]" + Fore.RESET)
      
      input("Press any key to continue ---> ")
      return main_menu()
      
    else:
      print(Fore.GREEN + f"[!] {test_proc} is not running [!]" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
    
if '__name__' == '__main__':
  main_menu()
  
