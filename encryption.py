import random
from circ import *
alphanum = {
     "a":5,
     "b":10,
     "c":24,
     "d":14,
     "e":23,
     "f":15,
     "g":11,
     "h":17,
     "i":9,
     "j":12,
     "k":21,
     "l":1,
     "m":22,
     "n":25,
     "o":6,
     "p":3,
     "q":20,
     "r":7,
     "s":18,
     "t":13,
     "u":26,
     "v":16,
     "w":2,
     "x":8,
     "y":19,
     "z":4,
     "A":27,
     "B":51,
     "C":29,
     "D":38,
     "E":32,
     "F":35,
     "G":34,
     "H":43,
     "I":47,
     "J":39,
     "K":40,
     "L":53,
     "M":45,
     "N":44,
     "O":41,
     "P":28,
     "Q":37,
     "R":36,
     "S":50,
     "T":42,
     "U":46,
     "V":31,
     "W":49,
     "X":33,
     "Y":30,
     "Z":48,
     ".":52,
     "`":70,
     "~":62,
     "!":57,
     "@":68,
     "#":79,
     "$":64,
     "%":61,
     "^":74,
     "&":71,
     "*":60,
     "(":54,
     ")":80,
     "-":73,
     "_":66,
     "=":53,
     "+":82,
     "|":75,
     "]":59,
     "}":72,
     "[":69,         
     "{":56,
     "'":65,
     '"':67,
     ";":77,
     ":":81,
     "/":63,
     "?":76,
     ">":78,
     ",":58,
     "<":55,
     "1":"?",
     "2":"]",
     "3":"/",
     "4":"$",
     "5":"*",
     "6":"(",
     "7":")",
     "8":"-",
     "9":"@",
     "0":"_",
     " ":"+"
}
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