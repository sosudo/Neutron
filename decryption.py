# 71.@.71.52.71.$./.52.|2799149|&
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
      return string