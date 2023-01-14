# Pre-determined variables
vardir = [
  ["Bootloader.fun","Registry.fun"],
  ["Booted.var","Location.var","Locationdir.var","cman.var"],
  ["Command.inp","Echo.inp"],
  ["Vardir.lst"],
  ["Booted.bool"]
]
booted = False
location = 0
locationdir = "/workspaces/bkernel "

# The error codes are in this dictionary for easy re-use; add new ones whenever you wish :)
error_codes = {
  "0x001": "The 'bootloader' instance is already running.",
  "0x002": "The item you were searching for was not found.",
  "0x003": "The file cannot be executed.",
  "0x004": "The directory is not accessible."
}

# Print error function for easy re-use; make sure to use the correct error code
def print_error(error_code, print_error=True):
  try:
    error_message = f"Error code {error_code}: {error_codes[error_code]}"
  except:
    raise Exception(f"The error code, {error_code}, is invalid.")

  if (print_error == True):
    print(error_message)
    return None
  else:
    return error_message

def help_command(command=None):
  if (command == None or command == ""):
    return "\nTo get help with a specific command, type help <command>\n"
  elif (command == "help"):
    return "\nbruh\n"
  elif (command == "rd"):
    return "\nReads a directory you specify.\n\n\tExample: rd about\n\nSyntax:\n\trd <directory_name>\n\nReturns:\n\tThe directory contents of the directory name you specified. In case you specify an invalid/non-existent directory, you will get an error code of 0x004.\n"

#Imported Extensions
import random
import os
import time
#Bootloader
def Bootloader():
  if booted == False:
    print("Booting B Kernel...")
    time.sleep(random.randint(0, 5))
    print("B Kernel")
    return True
  else:
    print_error("0x001");
#Registry
def Registry(x = 0):
  if x == 0: #Prints all Commands
    print(vardir[0]) #.fun Commands
    print(vardir[1]) #.var Commands
    print(vardir[2]) #.inp Commands
    print(vardir[3]) #.lst Commands
    print(vardir[4]) #.bool Commands
  elif x == "fun":
    print(vardir[0]) #only prints .fun Commands
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
  print("Type a command:")
  command = str(input(locationdir))
  if "registry" in command:
    if command == "registry fun":
      Registry("fun")
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
      print_error("0x002");
  elif "execute" in command:
    if command == "execute Bootloader.fun":
      Bootloader()
      print("Completed.")
    elif command == "execute Registry.fun":
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
      print("/workspaces/bkernel")
    elif location == 1:
      print("/workspaces/bkernel/about")
  elif "cd" in command:
    #0 = Root
    #1 = About
    if command == "cd about":
      if location == 0:
        location = 1
        locationdir = "/workspaces/bkernel/about "
        print("Done!")
      else:
        print_error("0x004");
    elif command == "cd 0":
      if location == 1:
        location = 0
        locationdir = "/workspaces/bkernel "
      else:
        print_error("0x004");
  elif command == "help":
    command_help = input("What command do you need help with? ")
    print(help_command(command_help))
  elif command == "rd":
    if location == 0:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
    elif location == 1:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__)) + r"/About"))
  elif "rdi" in command:
    echo = input("Insert Path: ")
    cman = open(echo,"r")
    print(cman.read())
    cman.close
  elif "cls" in command:
    os.system('cls')
  elif "exit" in command:
    print("Shutting Down...")
    time.sleep(random.randint(0, 5))
    booted = False