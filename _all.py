import shelve
from decryption import Decrypt
def All():
      password = shelve.open("password")
      key_list = list(password.keys())
      value_list = [password[i] for i in key_list]
      return_list = []
      for i in range(len(key_list)):
            append_value = str(key_list[i]) + ":" + str(Decrypt(value_list[i]))
            return_list.append(append_value)
      return return_list