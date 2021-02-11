from icecream import ic as println # Used for custom outputs
import os
import sys
from encryption import *
println.configureOutput(prefix='Neutron > ', includeContext=False) # Setting up custom outputs
def init():
     SK = input("Neutron > SK (h for help): ") # Neutron Start Key, determining what function Neutron leads to (0, 1, 2, h)
     if SK == "h":
          println("SK 0 is used to access the email client")
          println("SK 1 is used to access the password manager")
          println("SK 2 is used to access the encryption machine")
          init()
     elif SK == "0":
          println(SK)
     elif SK == "1":
          println(SK)
     elif SK == "2":
          println(SK)
          OK = input("Neutron > OK (h for help): ")
          if OK == "h":
               println("OK 0 is used to encrypt messages.")
               println("OK 1 is used to decrypt messages.")
          elif OK == "0":
               String = input("Neutron > String: ")
               println(Encrypt(String))
     else:
          println("Error: Invalid Neutron SK. Type h for help.")
          init()
init()