import os
import sys
import shutil

os.system('color')

# Pre-determined variables
vardir = [
  ["Bootloader.fn","Registry.fn"],
  ["Booted.var","Location.var","Locationdir.var","cman.var"],
  ["Command.inp","Echo.inp"],
  ["Vardir.lst"],
  ["Booted.bool"]
]
booted = False
location = 0
locationdir = "/workspaces/bkernel "

# Colors | For more help; see https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# The error codes are in this dictionary for easy re-use; add new ones whenever you wish :)
error_codes = {
  "0x001": "The 'bootloader' instance is already running.",
  "0x002": "The item you were searching for was not found.",
  "0x003": "The file cannot be executed.",
  "0x004": "The directory is not accessible.",
  "0x005": "That command doesn't exist. Type 'help' for a list of available commands."
}

# Print error function for easy re-use; make sure to use the correct error code
def print_error(error_code, print_error=True):
  try:
    error_message = f"{bcolors.FAIL}Error code {error_code}: {error_codes[error_code]}{bcolors.ENDC}"
  except:
    raise Exception(f"The error code, {error_code}, is invalid.")

  if (print_error == True):
    print(error_message)
    return None
  else:
    return error_message

def help_command(command=None):
  if command == None:
    print("Try typing in a command, such as help <command>")
  else:
    os.system('cls')
    if command == "cls":
      print("cls - Clears your Screen")
    elif command == "wf":
      print("wf - Creates File")
    elif command == "rf":
      print("rf -Reads File")
    elif command == "df":
      print("df - Deletes File")
    elif command == "wd":
      print("wd - Creates Directory")
    elif command == "rd":
      print("rd - Read Directory")
    elif command == "ded":
      print("ded - Delete Empty Directory")
    elif command == "dd":
      print("dd - Delete Directory + Contents")
    elif command == "registry":
      print("View all active variables.")
    elif command == "execute":
      print("Executes a function.")
    elif command == "help":
      print("bruh")
    else:
      print("No Data found for this command.")

#Imported Extensions
import random
import os
import time
#Bootloader
def Bootloader():
  if booted == False:
    print(f"{bcolors.BOLD}{bcolors.WARNING}Booting B Kernel...{bcolors.ENDC}")
    time.sleep(random.randint(2, 5))
    os.system('cls')
    print(f"{bcolors.WARNING}Welcome to {bcolors.BOLD}B Kernel{bcolors.ENDC}")
    return True
  else:
    print_error("0x001")
#Registry
def Registry(x = 0):
  if x == 0: #Prints all Commands
    print(vardir[0]) #.fn Commands
    print(vardir[1]) #.var Commands
    print(vardir[2]) #.inp Commands
    print(vardir[3]) #.lst Commands
    print(vardir[4]) #.bool Commands
  elif x == "fn":
    print(vardir[0]) #only prints .fn Commands
  elif x == "var":
    print(vardir[1]) #only prints .var Commands
  elif x == "inp":
    print(vardir[2]) #only prints .inp Commands
  elif x == "lst":
    print(vardir[3]) #only prints .lst Commands
  elif x == "bool":
    print(vardir[4]) # only prints .bool Commands

#Post-Determined Variables

booted = Bootloader()

#Default Directory: /workspaces/bkernel
while booted == True:
  command = str(input(locationdir))
  if "registry" in command:
    if command == "registry fn":
      Registry("fn")
    elif command == "registry var":
      Registry("var")
    elif command == "registry inp":
      Registry("inp")
    elif command == "registry lst":
      Registry("lst")
    elif command == "registry bool":
      Registry("bool")
    elif command == "registry":
      Registry()
    else:
      print_error("0x002")
  elif "execute" in command:
    if command == "execute Bootloader.fn":
      Bootloader()
      print("Completed.")
    elif command == "execute Registry.fn":
      Registry()
      print("Completed")
    elif command == "execute Booted.bool":
      print(str(booted) + "\n" + "Done!")
    else:
      print_error("0x003");
  elif "echo" in command: #echo
      echo = input()
      print("\"" + str(echo) + "\"")
  elif "whereami" in command: #wherami
    if location == 0:
      print("/workspaces/bkernel ")
    elif location == 1:
      print("/workspaces/bkernel/about ")
  elif "cd" in command:
    #0 = Root
    #1 = About
    if command == "cd about":
      if location == 0:
        location = 1
        locationdir = "/workspaces/bkernel/about "
        print("Done!")
      else:
        print_error("0x004")
    elif command == "cd 0":
      if location == 1:
        location = 0
        locationdir = "/workspaces/bkernel "
      else:
        print_error("0x004")
  elif command == "help":
    command_help = input("What command do you need help with? ")
    print(help_command(command_help))
  elif command == "rd":
    if location == 0:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
    elif location == 1:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__)) + r"/About"))
  elif "rf" in command:
    echo = input("Insert Path: ")
    cman = open(echo,"r")
    print(cman.read())
    cman.close
  elif "wf" in command:
    echo = input("Insert Name: ")
    with open("docs/" + echo, 'w') as f:
      os.system('cls')
      print("Editing File with Name (" + echo + ").")
      f.write(input(""))
  elif "df" in command:
    echo = input("Insert Path: ")
    if ".py" in echo:
      if "main.py" in echo:
        print("Access Denied.")
      else:
        eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
        if eco == "Y":
          os.remove(echo)
        else:
          pass
    elif ".exe" in echo:
      eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
      if eco == "Y":
        os.remove(echo)
      else:
        pass
    elif ".iso" in echo:
      eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
      if eco == "Y":
        os.remove(echo)
      else:
        pass
    elif ".bat" in echo:
      eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
      if eco == "Y":
        os.remove(echo)
      else:
        pass
    elif ".dll" in echo:
      eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
      if eco == "Y":
        os.remove(echo)
      else:
        pass
    elif ".img" in echo:
      eco = input("This file might contain important data files. Are you sure you want to continue? [Y/N] ")
      if eco == "Y":
        os.remove(echo)
      else:
        pass
    else:
      os.remove(echo)
  elif "ded" in command:
    echo = input("Insert Directory Path: ")
    os.rmdir(echo)
  elif "dd" in command:
    echo = input("Insert Directory Path: ")
    try:
      shutil.rmtree(echo)
    except OSError as Error:
      print_error("0x004")
  elif "wd" in command:
    echo = input("Insert Directory Name: ")
    os.mkdir(echo)    
  elif "cls" in command:
    os.system('cls')
  elif "exit" in command:
    os.system('cls')
    print("Shutting Down...")
    time.sleep(random.randint(0, 5))
    booted = False
  else:
    print_error("0x005")
