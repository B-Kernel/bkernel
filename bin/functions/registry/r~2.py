import os
import shutil
import subprocess
from sys import version_info

locationdir = os.getcwd()
types = ["fn", "var", "inp", "lst", "bool", "dct"]

variables = {
  "Booted" : types[4],
  "Bootloader" : types[0],
  "Cman" : types[1],
  "Comlistdir" : types[1],
  "Command" : types[2],
  "Echo" : types[2],
  "Location" : types[1],
  "Locationdir" : types[1],
  "Locationstr" : types[1],
  "Types" : types[3],
  "Variables" : types[5]
}


for i in variables:
  print(i, variables[i])