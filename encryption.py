import random
from circ import *
def encrypt(string:str) -> str:
      encrypted_string = string
      while encrypted_string==string:
            shift_value = random.randint(-1000,1000)
            if shift_value < 0:
                  encrypted_string = lcirc(shift_value, string)
            else:
                  encrypted_string = rcirc(shift_value, string)
      return encrypted_string