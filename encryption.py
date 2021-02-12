import random
from circ import *
from alphanum import alphanum
def Encrypt(string:str) -> str:
      encrypted_string = string
      while encrypted_string==string:
            shift_value = random.randint(-10000000,10000000)
            if shift_value < 0:
                  encrypted_string = lcirc(shift_value, string)
            else:
                  encrypted_string = rcirc(shift_value, string)
      encrypted_list = [i for i in encrypted_string]
      encrypted_string = ''
      for i in encrypted_list:
            encrypted_string += str(alphanum[i])+"."
      symbol = random.choice(["!","#","%","^","&","=","`","~"])
      encrypted_list = [i for i in encrypted_string]
      for i in range(len(encrypted_list)):
            if i%2 == 0:
                  encrypted_list.insert(i,symbol)
      encrypted_string = ''
      for i in encrypted_list:
            encrypted_string += str(alphanum[i])+"."
      encrypted_string += "|"+str(shift_value)+"|"+symbol
      return encrypted_string