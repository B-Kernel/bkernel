#Pre-Determined Variables
vardir = [["Bootloader.fun","Registry.fun"], ["Booted.var","Location.var","Locationdir.var","cman.var"], ["Command.inp","Echo.inp"],["Vardir.lst"],["Booted.bool"]]
booted = False
location = 0
locationdir = "/workspaces/bkernel "
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
    print("Error 0x001 - Bootloader Instance Already Running")
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
      print("Error 0x002 - Not Found")
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
      print("Error 0x003 -  File Cannot be Executed")
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
        print("Error 0x004 - Directory is not Accessible")
    elif command == "cd 0":
      if location == 1:
        location = 0
        locationdir = "/workspaces/bkernel "
      else:
        print("Error 0x004 - Directory is not Accessible")
  elif command == "rd":
    if location == 0:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__))))
    elif location == 1:
      print(os.listdir(os.path.dirname(os.path.realpath(__file__)) + r"/About"))
  elif "rdi" in command:
    echo = input()
    if echo == "README.md" or echo == "README":
      if location == 1:
        cman = open(r"/workspaces/bkernel/About/README.md","r")
        print(cman.read())
        cman.close
      else:
        print("File not available in Current Directory.")
        print("Current Directory: " + locationdir)
  elif "exit" in command:
    print("Shutting Down...")
    time.sleep(random.randint(0, 5))
    booted = False