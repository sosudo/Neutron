from decryption import Decrypt
import shelve
def Retreive(Site:str) -> str:
      password = shelve.open("password")
      Password = password[Site]
      password.close()
      return Decrypt(Password)