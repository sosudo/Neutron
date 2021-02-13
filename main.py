from icecream import ic as println
from decryption import Decrypt
from encryption import Encrypt
from retreive import Retreive
from append import Append
from secure_lock import Generate
from _all import All
println.configureOutput(prefix='Neutron > ', includeContext=False)
def init():
     SK = input("Neutron > SK (h for help): ")
     if SK == "h":
          println("SK 0 is used to access the email client.")
          println("SK 1 is used to access the password manager.")
          println("OK 0 for SK 1 is used to append passwords to your personal password database.")
          println("OK 1 for SK 1 is used to retreive passwords from your personal password database.")
          println("OK 2 for SK 1 is used to generate passwords and append them to you personal password database.")
          println("OK 3 for SK 1 is used to retreive all your passwords from your personal password database.")
          println("SK 2 is used to access the encryption machine.")
          println("OK 0 for SK 2 is used to encrypt messages.")
          println("OK 1 for SK 2 is used to decrypt messages previously encrypted by Neutron.")
          init()
     elif SK == "0":
          println(SK)
     elif SK == "1":
          println(SK)
          OK = input("Neutron > OK (h for help): ")
          if OK == "0":
               Site = input("Neutron > Site: ")
               Password = input("Neutron > Password: ")
               println(Append(Site, Password))
          elif OK == "1":
               Site = input("Neutron > Site: ")
               println(Retreive(Site))
          elif OK == "2":
               Name = input("Neutron > Name: ")
               Length = int(input("Neutron > Length: "))
               println(Generate(Name, Length))
          elif OK == "3":
               println(All())
          else:
               println("Error: Invalid Neturon OK. Type h for help.")
               init()
     elif SK == "2":
          println(SK)
          OK = input("Neutron > OK (h for help): ")
          if OK == "h":
               println("OK 0 is used to encrypt messages.")
               println("OK 1 is used to decrypt messages previously encrypted by Neutron.")
          elif OK == "0":
               String = input("Neutron > String: ")
               println(Encrypt(String))
          elif OK == "1":
               String = input("Neutron > String: ")
               println(Decrypt(String))
          else:
               println("Error: Invalid Neutron OK. Type h for help.")
               init()
     else:
          println("Error: Invalid Neutron SK. Type h for help.")
          init()
init()
