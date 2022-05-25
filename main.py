#I have to put the actual process names later. Cant do it rn as I'm not on my desktop.
#619 861 2322


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
  print("[1] Easy Anti-Cheat")
  print("[2] Battleye")
  print("[3] Richote")
  print("[4] Help")
  
  options = inout("Select Anti-Cheat to Check ---> ")
  

def main_menu():
  os.system("cls")
  app_logo()
  menu()
  
def getService(name):

    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service

def EAC():
  
  service = getService('EasyAntiCheat')
  print(service)

  if service:
      print(Fore.GREEN + "Easy Anti-Cheat is running" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
  else:
      print(Fore.RED + "Easy Anti-Cheat is  not running")
      input("Press any key to continue ---> ")
      return main_menu()
    
def BATTLEYE():
  
  service = getService('Battleye')
  print(service)

  if service:
      print(Fore.GREEN + "Battleye is running" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
  else:
      print(Fore.RED + "Battleye is  not running")
      input("Press any key to continue ---> ")
      return main_menu()
    
def RICOCHET():
  
  service = getService('Ricochet')
  print(service)

  if service:
      print(Fore.GREEN + "Ricochet is running" + Fore.RESET)
      input("Press any key to continue ---> ")
      return main_menu()
  else:
      print(Fore.RED + "Ricochet is  not running")
      input("Press any key to continue ---> ")
      return main_menu()
    
if '__name__' == '__main__':
  main_menu()
  
