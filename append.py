from encryption import Encrypt
import shelve
def Append(Site:str,Password:str):
      password = shelve.open("password")
      Password = Encrypt(Password)
      password[Site] = Password
      password.close()
      return "Password added."