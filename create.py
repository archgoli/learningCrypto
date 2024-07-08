import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(128)

with open('key.txt', 'w') as output:
    output.write(key.decode("cp1252"))