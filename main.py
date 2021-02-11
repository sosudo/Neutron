from icecream import ic as println # Used for custom outputs
from encryption import *
println.configureOutput(prefix='Neutron > ', includeContext=False) # Setting up custom outputs
sk = input("Neutron > SK (h for help): ") # Neutron Start Key, determining what function Neutron leads to (0, 1, 2, h)
if sk == "h":
     println("SK 0 is used to access the email client")
     println("SK 1 is used to access the password manager")
     println("SK 2 is used to access the encryption machine")
elif sk == "0":
     println(sk)
elif sk == "1":
     println(sk)
elif sk == "2":
     println(sk)
     operation = input("Neutron > Operation: ")

     string = input("Neutron > String: ")
     println(encrypt(string))
else:
     println("Error")