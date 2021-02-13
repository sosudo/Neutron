import random
import shelve
from encryption import Encrypt
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+\|]}[{'';:/?.>,<ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Generate(name:str, length:int) -> str:
      Password = ''
      for c in range(length):
            Password+=random.choice(chars)
      password = shelve.open("password")
      password[name] = Encrypt(Password)
      password.close()
      return Password