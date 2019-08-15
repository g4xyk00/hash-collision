# PBKDF2-HMAC-SHA224 collision by TihanyiNorbert 
# Python script: g4xyk00

import hashlib,base64

def hash(string):
  hash = hashlib.pbkdf2_hmac("sha224",string,"salt",1000)
  return base64.b64encode(hash)

string1 = "Tihanyi_collision_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaae6vit9wh";
string2 = ")P.!{(]??/lQrfzs4QTQt#6qQe+8";

print hash(string1)
print hash(string2)