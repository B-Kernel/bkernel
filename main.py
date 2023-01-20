import os
import shutil
import subprocess

os.system('color')

# Pre-determined variables
vardir = [
  ["Bootloader.fn","Registry.fn"],
  ["Booted.var","Location.var","Locationdir.var", "Locationstr.var", "cman.var", "comlistdir.var"],
  ["Command.inp","Echo.inp"],
  ["Vardir.lst"],
  ["Booted.bool"]
]
booted = False
location = 0

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
  if (command == None or command == ""):
    os.system('cls')
    return "\nTo get help with a specific command, type help <command>\n"
  elif (command == "help"):
    os.system('cls')
    return "\nbruh\n"
  elif (command == "rd"):
    os.system('cls')
    return "\nReads a directory you specify.\n\n\tExample: rd About\n\nSyntax:\n\trd <directory_name>\n\nReturns:\n\tThe directory contents of the directory name you specified. In case you specify an invalid/non-existent directory, you will get an error code of 0x004.\n"
  elif (command == "rf"):
    os.system('cls')
    return "\nReads a file you specify.\n\n\tExample: rf /workspaces/bkernel/docs/Test\n\nSyntax:\n\trf <location of file (path)>\n\nReturns:\n\tThe contents of the filename you specified. In case you specify an invalid/non-existent file, you will get an error code of 0x002.\n"
  elif (command == "wf"):
    os.system('cls')
    return "\nCreates a file with a given name + data\n"
  elif (command == "wd"):
    os.system('cls')
    return "\nCreates a directory with a given name."
  elif (command == "df"):
    os.system('cls')
    return "\nDeletes a file with a given filepath."
  elif (command == "ded"):
    os.system('cls')
    return "\nDeletes an Empty directory."
  elif (command == "dd"):
    os.system('cls')
    return "\nDeletes a directory and all of its contents."
  elif (command == "registry"):
    os.system('cls')
    return "\nDisplays all active variables."
  elif (command == "cls"):
    os.system('cls')
    return "\nClears your Screen\n"
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
#I'll do this when I finish with my work D:
#Okay, I'll make a REGISTRY, you make a Directory sounds good
while booted == True:
  locationdir = os.getcwd();
  comlistdir = locationdir + " "
  locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))

  command = str(input(os.getcwd() + " "))

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
      print_error("0x003")
  elif "echo" in command: #echo
      echo = input()
      print("\"" + str(echo) + "\"")
  elif "whereami" in command: #wherami
    print(locationdir)
  elif "cd" in command:
    locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    echo = input("Insert New Directory (Located in " + locationdir + ") ")
    
    try:
      os.chdir(echo)
    except OSError:
      print("An error occurred.")
  elif command == "help":
    command_help = input("What command do you need help with? ")
    print(help_command(command_help))
  elif command == "rd":
    print(os.listdir(locationdir))
  elif "rf" in command:
    echo = input("Insert Path: ")
    cman = open(echo,"r")
    print(cman.read())
    cman.close
  elif "rc" in command:
    comlistdir = ""
    echo = input("Insert Path: ")
    os.system('cls')
    time.sleep(random.randint(2, 5))
    if ".py" in echo:
      try:
        cmancode = subprocess.Popen(["python", echo]) #Runs Python Code!
      except OSError:
        print("An Error Occured while reading this code.")
    elif ".js" in echo:
      try:
        cmancode = subprocess.Popen(["javascript", echo]) #Runs JS Code!
      except OSError:
        print("An Error Occured while reading this code.")
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