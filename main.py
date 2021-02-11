from icecream import ic # Used for custom outputs
from icecream import install  # Used to install icecream project wide
from encryption import *
ic.configureOutput(prefix='Neutron > ', includeContext=False) # Setting up custom outputs
install()
sk = input("Neutron > SK (h for help): ") # Neutron Start Key, determining what function Neutron leads to (0, 1, 2, h)
if sk == "h":
     ic("SK 0 is used to access the email client")
     ic("SK 1 is used to access the password manager")
     ic("SK 2 is used to access the encryption machine")
elif sk == "0":
     ic(sk)
elif sk == "1":
     ic(sk)
elif sk == "2":
     ic(sk)
     string = input("Neutron > String: ")
     ic(encrypt(string))
else:
     ic("Error")