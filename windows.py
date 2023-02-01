import os
import shutil
import subprocess
from sys import version_info

os.system('color')

# Pre-determined variables
location = 0
locationdir = os.getcwd()
comlistdir = locationdir + " "
locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/registry/r~1.py"])
subprogram = False
booted = False

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

def clear_screen():
    os.system("cls")

def help_command(command=None):
  if (command == None or command == ""):
    clear_screen()
    return "\nTo get help with a specific command, type help <command>\n"
  elif (command == "help"):
    clear_screen()
    return "\nbruh\n"
  elif (command == "rd"):
    clear_screen()
    return "\nReads a directory you specify.\n\n\tExample: rd About\n\nSyntax:\n\trd <directory_name>\n\nReturns:\n\tThe directory contents of the directory name you specified. In case you specify an invalid/non-existent directory, you will get an error code of 0x004.\n"
  elif (command == "rf"):
    clear_screen()
    return "\nReads a file you specify.\n\n\tExample: rf /workspaces/bkernel/docs/Test\n\nSyntax:\n\trf <location of file (path)>\n\nReturns:\n\tThe contents of the filename you specified. In case you specify an invalid/non-existent file, you will get an error code of 0x002.\n"
  elif (command == "wf"):
    clear_screen()
    return "\nCreates a file with a given name + data\n"
  elif (command == "wd"):
    clear_screen()
    return "\nCreates a directory with a given name."
  elif (command == "df"):
    clear_screen()
    return "\nDeletes a file with a given filepath."
  elif (command == "ded"):
    clear_screen()
    return "\nDeletes an Empty directory."
  elif (command == "dd"):
    clear_screen()
    return "\nDeletes a directory and all of its contents."
  elif (command == "registry"):
    clear_screen()
    return "\nDisplays all active variables."
  elif (command == "cls"):
    clear_screen()
    return "\nClears your Screen\n"
  elif (command == "cf"):
    clear_screen()
    return "\nCopies Files\n"
  elif (command == "rc"):
    clear_screen()
    return "\nRuns Code\nCURRENTLY SUPPORTED:\n1. Python\n2. JavaScript"
#Imported Extensions
import random
import os
import time
#Bootloader
def Bootloader():
  if booted == False:
    os.system('color e0')
    print("B-Kernel")
    print("(c) B-Kernel, 2023")
    print("Version 1.130.0")
    time.sleep(random.randint(2, 5))
    clear_screen()
    os.system('color 0f')
    print(f"{bcolors.WARNING}Welcome to {bcolors.BOLD}B Kernel{bcolors.ENDC}")
    return True
  else:
    print_error("0x001")

#Post-Determined Variables
booted = Bootloader()
#Default Directory: /workspaces/bkernel
while booted == True:
  command = str(input(os.getcwd() + " "))
  locationdir = os.getcwd()
  comlistdir = locationdir + " "
  locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
  if "registry" in command:
    #Registry
    subprocess.Popen(["python", str(locationdir) + "/bin/functions/registry/r~2.py"])
  elif "execute" in command:
    if command == "execute Bootloader.fn":
      Bootloader()
      print("Completed.")
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
    clear_screen()
    time.sleep(random.randint(2, 5))
    if ".py" in echo:
      try:
        cmancode = subprocess.Popen(["python", echo]) #Runs Python Code!
      except OSError:
        print("An Error Occured while reading this code.")
    elif ".js" in echo:
      try:
        # Made by Arnav Thorat
        # After a lot of hard work,
        # we finally got this working :)
        def line_prepender(filename, line):
          with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)
        def is_exec(filename):
          with open(filename) as f:
            if '#!/usr/bin/env node' in f.read():
              return True
        if not is_exec(echo):
          line_prepender(echo, "#!/usr/bin/env node")
        p = subprocess.Popen(["C:\\Program Files\\nodejs\\node.exe", echo])
        # cmancode = subprocess.Popen(["javascript", echo]) #Runs JS Code!
      except OSError as err:
        print(err)
  elif "wf" in command:
    echo = input("Insert Name: ")
    with open("docs/" + echo, 'w') as f:
      clear_screen()
      print("Editing File with Name (" + echo + ").")
      f.write(input(""))
  elif "cf" in command:
    try:
      src = input("Insert path (of old file): ")
      dst = input("Insert path of new file: ")
      shutil.copyfile(src, dst)
    except OSError:
      pass
  elif "mvf" in command:
    try:
      src = input("Insert Old Path [including file]: ")
      dst = input("Insert New Path [including file]: ")
      shutil.copyfile(src,dst)
      os.remove(src)
    except OSError as err:
      print(err)
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
    clear_screen()
  elif "os" in command:
    try:
      cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/check.py"]) #Runs Check
    except OSError:
      print("An Error Occured while reading this code.")
  elif "delta" in command:
    try:
      cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/clock.py"])
    except OSError as err:
      print(err)
  elif "calc" in command:
    #B-Kernel Calculator
    import os
    import math
    def add(val1, val2):
      print(val1 + val2)
    def sub(val1, val2):
      print(val1 - val2)
    def mlt(val1, val2):
      print(val1 * val2)
    def div(val1, val2):
      print( val1 / val2 )
    def exp(val1, val2):
      print( val1 ** val2 )
    def fldiv(val1, val2):
      print( val1 // val2 )
    def rem(val1,val2):
      print( val1 % val2 )
    command = input()
    if command == "add" or command == "Add" or command == "ADD":
      add(int(input()), int(input()))
    elif command == "subtract" or command == "Subtract" or command == "SUBTRACT":
      sub(int(input()), int(input()))
    elif command == "multiply" or command == "Multiply" or command == "MULTIPLY":
      mlt(int(input()), int(input()))
    elif command == "divide" or command == "Divide" or command == "DIVIDE":
      div(int(input()), int(input()))
    elif command == "exponent" or command == "Exponent" or command == "EXPONENT":
      exp(int(input()), int(input()))
    elif command == "floor" or command == "Floor" or command == "FLOOR":
      sub(int(input()), int(input()))
    elif command == "remainder" or command == "Remainder" or command == "REMAINDER":
      sub(int(input()), int(input()))
    else:
      print("Command / Operation Not Found.")
  elif "exit" in command:
    clear_screen()
    print("Shutting Down...")
    time.sleep(random.randint(0, 5))
    booted = False
  else:
    print_error("0x005")
