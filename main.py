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
  print("[1] Test Software")
  print("[2] Easy Anti-Cheat")
  print("[3] Battleye")
  print("[4] Richote")
  print("[5] Help")
  
  
