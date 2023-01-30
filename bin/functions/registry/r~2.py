import os
import shutil
import subprocess
from sys import version_info

locationdir = os.getcwd()
vardir = [
  ["Bootloader.fn"],
  ["Location.var","Locationdir.var", "Locationstr.var", "cman.var", "comlistdir.var"],
  ["Command.inp","Echo.inp"],
  ["Vardir.lst"],
  ["Booted.bool"]
]

print(vardir[0]) #.fn Commands
print(vardir[1]) #.var Commands
print(vardir[2]) #.inp Commands
print(vardir[3]) #.lst Commands
print(vardir[4]) #.bool Commands