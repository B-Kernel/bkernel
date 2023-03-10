#Imported Variables
import os
import shutil
import time
import subprocess
from sys import version_info
os.system('color')
# Pre-determined variables
locationdir = os.getcwd()
comlistdir = locationdir + " "
locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/registry/r~1.py"])
booted = False
history = []
# Colors
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
# Error Codes
error_codes = {
  "0x001": "The 'bootloader' instance is already running.",
  "0x002": "The item you were searching for was not found.",
  "0x003": "The file cannot be executed.",
  "0x004": "The directory is not accessible.",
  "0x005": "That command doesn't exist. Type 'help' for a list of available commands."
}


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

help = {
  "help" : "Bruh.\n",
  "registry" : "Lists active variables.\nSYNTAX: registry\n",
  "execute" : "Executes a function OR an application.\nSYNTAX: execute <function>\n",
  "whereami" : "Specifies the current working directory.\nSYNTAX: whereami\n",
  "cd" : "Changes Directory.\nSYNTAX: cd\n",
  "rd" : "Reads the contents of the Directory.\nSYNTAX: rd\n",
  "rf" : "Reads the contents of a File.\nSYNTAX: rf\n",
  "wd" : "Creates a directory with a given name.\nSYNTAX: wd\n",
  "wf" : "Creates a file with a given name + data.\nSYNTAX: wf\n",
  "mvf" : "Moves a file with a given path.\nSYNTAX: mvf\n",
  "ef" : "Edits a file with a given path.\nSYNTAX: ef\n",
  "rc" : "Runs code with a given path.\nSYNTAX: rc\n",
  "cls": "Clears the Screen.\nSYNTAX: cls\n",
  "delta":"Clock.\n",
  "calc":"Calculator.\nSYNTAX: calc\n",
  "os": "Gets the current OS + OS Version.\nSYNTAX: os"
}

def help_command(command=None):
  clear_screen()
  if command in help:
    return command + ": " + help[command]
  elif command == None:
    for i in help:
      print( i + ": " + help[i] )
    return "\nPossible Help Options."
  else:
    return print_error("0x002", print_error=True)

import random

def Bootloader():
  if booted == False:
    os.system('color e0')
    print("B-Kernel 3.0.0 Windows")
    print("(c) 2023")
    time.sleep(random.randint(2, 5))
    clear_screen()
    os.system('color 0f')
    return True
  else:
    print_error("0x001")

def hex_rgb():
    hex = input("Insert HEX: ")
    hexdictionary = {
      "0":"0",
      "1":"1",
      "2":"2",
      "3":"3",
      "4":"4",
      "5":"5",
      "6":"6",
      "7":"7",
      "8":"8",
      "9":"9",
      "a":"10",
      "b":"11",
      "c":"12",
      "d":"13",
      "e":"14",
      "f":"15",
      "A":"10",
      "B":"11",
      "C":"12",
      "D":"13",
      "E":"14",
      "F":"15"
    }
    hex1 = []
    hex2 = []
    hex3 = []
    hex1.append(hex[0])
    hex1.append(hex[1])
    hex2.append(hex[2])
    hex2.append(hex[3])
    hex3.append(hex[4])
    hex3.append(hex[5])
    R = []
    G = []
    B = []
    for i in hex1:
      i = int(hexdictionary[i])
      R.append(i)
    for i in hex2:
      i = int(hexdictionary[i])
      G.append(i)
    for i in hex3:
      i = int(hexdictionary[i])
      B.append(i)
    r = R[0] * 16 + R[1]
    g = G[0] * 16 + G[1]
    b = B[0] * 16 + B[1]
    print(str(r) + ", " + str(g) + ", " + str(b))

def rgb_hex():
  #inputs
  rgbdictionary = {
    "0":"0",
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "10":"A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15":"F"
  }
  R = int(input("Insert R: "))
  G = int(input("Insert G: "))
  B = int(input("Insert B: "))
  def rgbtohex(r,g,b,hexdict):
    rtime = 0
    gtime = 0
    btime = 0
    while r >= 16:
      rtime += 1
      r -= 16
    while g >= 16:
      gtime += 1
      g -= 16
    while b >= 16:
      btime += 1
      b -= 16
    r = hexdict[str(r)]
    rtime = hexdict[str(rtime)]
    g = hexdict[str(g)]
    gtime = hexdict[str(gtime)]
    b = hexdict[str(b)]
    btime = hexdict[str(btime)]
    print(str(rtime) + str(r) + str(gtime) + str(g) + str(btime) + str(b))
  rgbtohex(R,G,B,rgbdictionary)

def dho():
  echo = int(input("Insert Number: "))
  print("DECIMAL: " + str(echo))
  octal = oct(echo)
  octallist = []
  octalresult = ""
  for i in octal:
    octallist.append(i)
  octalpos = 0
  for i in octallist:
    if octalpos < 2:
      octalpos += 1
      pass
    else:
      octalpos += 1
      octalresult += str(i)
  print("OCTAL: " + octalresult)
  hexa = hex(echo)
  hexalist = []
  hexaresult = ""
  for i in hexa:
    hexalist.append(i)
  hexapos = 0
  for i in hexalist:
    if hexapos < 2:
      hexapos += 1
      pass
    else:
      hexapos += 1
      hexaresult += str(i)
  print("HEXADECIMAL: " + hexaresult)

#Calling Bootloader


booted = Bootloader()

while booted == True:
  command = str(input(os.getcwd() + " "))
  locationdir = os.getcwd()
  comlistdir = locationdir + " "
  locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
  history.append("\"" + command + "\"")
  if command == "$REGISTRY":
    subprocess.Popen(["python", str(locationdir) + "/bin/functions/registry/r~2.py"])
  elif command == "$EXECUTE":
    command == input("Insert Command to Execute: [Syntax - execute <command>]")
    if command == "execute Bootloader.fn":
      Bootloader()
    elif command == "execute Registry":
      subprocess.Popen(["python", str(locationdir) + "/bin/functions/registry/r~2.py"])
    elif command == "execute Booted.bool":
      print(str(booted) + "\n" + "Done!")
    else:
      print_error("0x003")
  elif command == "echo": #echo
      echo = input()
      print("\"" + str(echo) + "\"")
  elif command == "whereami": #wherami
    print(locationdir)
  elif command == "cd":
    locationstr = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    echo = input("Insert New Directory (Located in " + locationdir + ") ")
    try:
      os.chdir(echo)
    except OSError:
      print("An error occurred.")
  elif command == "help":
    command_help = input("What command do you need help with? ")
    if command_help == "":
      print(help_command(None))
    else:
      print(help_command(command_help))
  elif command == "rd":
    print(os.listdir(locationdir))
  elif command == "rf":
    echo = input("Insert Path: ")
    cman = open(echo,"r")
    print(cman.read())
    cman.close
  elif command == "history":
    placement = 0
    for i in history:
      placement += 1
      print(str(placement) + ". " + i)
  elif command =="rc":
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
  elif command == "wf":
    echo = input("Insert Name: ")
    try:
      with open("docs/" + echo, 'w') as filer:
        os.system('cls')
        print("Write Text Here...")
        File_Temp = True
        while File_Temp == True:
          me = input()
          if me != "$EXIT":
            filer.write(me)
            filer.write("\n")
          else:
            filer.close()
            break
    except:
      pass
  elif command == "cf":
    try:
      src = input("Insert path (of old file): ")
      dst = input("Insert path of new file: ")
      shutil.copyfile(src, dst)
    except OSError:
      pass
  elif command == "mvf":
    try:
      src = input("Insert Old Path [including file]: ")
      dst = input("Insert New Path [including file]: ")
      shutil.copyfile(src,dst)
      os.remove(src)
    except OSError as err:
      print(err)
  elif command == "ef":
    echoo = input("Insert Filepath: ")
    with open(echoo, 'a') as a:
      clear_screen()
      print("Editing (" + echoo + ").")
      print(" ")
      d = open(echoo,"r")
      c = d.read()
      print(c)
      try:
        with open(echoo, 'a') as filer:
          os.system('cls')
          print("Write Text Here...")
          File_Temp = True
          while File_Temp == True:
            me = input()
            if me != "$EXIT":
              filer.write(me)
              filer.write("\n")
            else:
              filer.close()
              break
      except:
        pass
  elif command == "df":
    echo = input("Insert Path: ")
    if ".py" in echo:
      if "windows.py" in echo:
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
  elif command == "ded":
    echo = input("Insert Directory Path: ")
    os.rmdir(echo)
  elif "dd" in command:
    echo = input("Insert Directory Path: ")
    try:
      shutil.rmtree(echo)
    except OSError as Error:
      print_error("0x004")
  elif command == "wd":
    echo = input("Insert Directory Name: ")
    os.mkdir(echo)    
  elif command == "cls":
    clear_screen()
  elif command == "os":
    try:
      cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/check.py"]) #Runs Check
    except OSError:
      print("An Error Occured while reading this code.")
  elif command == "delta":
    try:
      cmancode = subprocess.Popen(["python", str(locationdir) + "/bin/functions/clock.py"])
    except OSError as err:
      print(err)
  elif command == "calc":
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
    elif command == "cHEXRGB":
      hex_rgb()
    elif command == "cRGBHEX":
      rgb_hex()
    elif command == "cDHO":
      dho()
    else:
      print("Command / Operation Not Found.")
  elif command == "tip":
    subprocess.Popen(["python", str(locationdir) + "/bin/functions/wintips.py"])
  elif command == "$EXIT":
    clear_screen()
    print("Shutting Down...")
    time.sleep(random.randint(0, 5))
    booted = False
  else:
    print_error("0x005")