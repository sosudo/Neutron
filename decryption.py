from alphanum import numalpha
from circ import *
def Decrypt(string:str) -> str:
      encrypted_list = [i for i in string]
      symbol =  encrypted_list[-1] # &
      encrypted_list.pop()
      encrypted_list.pop() # 71.@.71.52.71.$./.52.|2799149
      seperator_index = encrypted_list.index("|")
      shift_value = ''
      for i in encrypted_list[seperator_index+1:]:
            shift_value += i
      shift_value = int(shift_value) # 2799149
      for i in range(len(str(shift_value))):
            encrypted_list.pop() # 71.@.71.52.71.$./.52.|
      encrypted_list.pop() # 71.@.71.52.71.$./.52.
      string = ''
      for i in encrypted_list:
            string += i
      encrypted_list.clear()
      encrypted_list = string.split(".")
      encrypted_list.pop()
      encrypted_list_prime = []
      encrypted_list_prime = [numalpha[int(i)] if i.isnumeric() else numalpha[str(i)] for i in encrypted_list]
      encrypted_list.clear()
      encrypted_list = [i for i in encrypted_list_prime if i != symbol]
      encrypted_list_prime.clear()
      for i in range(len(encrypted_list)):
            value = ''
            if encrypted_list[i] != ".":
                  while encrypted_list[i] != ".":
                        value += encrypted_list[i]
                        i += 1
                  encrypted_list_prime.append(value)
      encrypted_list.clear()
      encrypted_list = [i for i in encrypted_list_prime]
      for i in range(len(encrypted_list)):
            try:
                  if len(encrypted_list[i])==2 and len(encrypted_list[i+1])==1:
                        encrypted_list.pop(i+1)
            except:
                  break
      encrypted_list_prime.clear()
      encrypted_list_prime = [numalpha[int(i)] if i.isnumeric() else numalpha[str(i)] for i in encrypted_list]
      encrypted_list.clear()
      encrypted_list = [i for i in encrypted_list_prime]
      string = ''
      for i in encrypted_list:
            string += i
      if shift_value > 0:
            string = lcirc(shift_value,string)
      else:
            string = rcirc(shift_value,string)
      return string