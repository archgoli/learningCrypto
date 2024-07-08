import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = open("key.txt", "r")
key = key.read().encode("cp1252")

def get_plaintext():
    fileName = input("Please enter file name: ")
    message = open(fileName, "r")
    message = message.read().encode("cp1252")
    return message


def encrypt(key, plaintext, aad):
    # Generate a random 96-bit IV
    iv = os.urandom(12)

    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV
    encryptor = Cipher(  # what is a Cipher object?
        algorithms.AES(key),
        modes.GCM(iv),
    ).encryptor()

    # associated_data will be authenticated but not encrypted
    encryptor.authenticate_additional_data(aad)

    # encrypt the plaintext and get associated ciphertext - GCM doesn't require padding
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return iv, ciphertext, encryptor.tag  # what does encryptor.tag do?


def decrypt(key, aad, iv, ciphertext, tag):
    # Construct a Cipher object, with the key, iv, and additionally the GCM tag
    # used for authenticating the message
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
    ).decryptor()

    # We put associated_data back in or the tag will fail to verify when
    # we finalize the decryptor
    decryptor.authenticate_additional_data(aad)

    # Decryption gets us the authenticated plaintext.
    # If the tag doesn't match, an InvalidTag exception will be raised
    return decryptor.update(ciphertext) + decryptor.finalize()


# encrypt and decrypt sample message
# iv, ciphertext, tag = encrypt(
#     key,
#     b"a secret message :)",
#     b"authenticated but not encrypted payload"
# )
#
# print(decrypt(
#     key,
#     b"authenticated but not encrypted payload",
#     iv,
#     ciphertext,
#     tag
# ))

# print(key)




