import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC














file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()




from cryptography.fernet import Fernet
#key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = 'img5.encrypted'
output_file = 'dec_img5.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

# You can delete input_file if you want


import timeit
code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
