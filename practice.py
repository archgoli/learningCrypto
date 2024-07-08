import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESCCM
from cryptography.hazmat.primitives import hashes, hmac
import binascii

# AES-GCM
data = b"a secret message"
aad = b"authenticated but unencrypted data"

key = AESGCM.generate_key(128)  # generates a random AES-GCM key

aesgcm = AESGCM(key)

nonce = os.urandom(
    12)  # iv - ensure same plaintext will produce different ciphertexts when encrypting with the same key,
# make sure to not use same nonce and key again
ct = aesgcm.encrypt(nonce, data, aad)  # encrypts and authenticates the data, authenticates the aad
print(aesgcm.decrypt(nonce, ct,
                     aad))  # decrypts data and authenticates aad, which must be same as one in encrypt function


# Another Implementation of AES-GCM
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


iv, ciphertext, tag = encrypt(
    key,
    b"a secret message :)",
    b"authenticated but not encrypted payload"
)

print(decrypt(
    key,
    b"authenticated but not encrypted payload",
    iv,
    ciphertext,
    tag
))

# AES with different modes of operation

# AES-CBC
key2 = os.urandom(32)
nonce2 = os.urandom(16)
cipher = Cipher(algorithms.AES(key2), modes.CBC(nonce2))
encryptor = cipher.encryptor()
ct2 = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()
print(decryptor.update(ct2) + decryptor.finalize())

# AES-CBC-MAC (CCM)
data3 = b"a secret message!"
aad3 = b"authenticated but unencrypted data"
key3 = AESCCM.generate_key(128)
aesccm = AESCCM(key)
nonce3 = os.urandom(13)
ct3 = aesccm.encrypt(nonce3, data3, aad3)
print(aesccm.decrypt(nonce3, ct3, aad3))

# AES-CTR
key2 = os.urandom(32)
nonce2 = os.urandom(16)
cipher = Cipher(algorithms.AES(key2), modes.CTR(nonce2))
encryptor = cipher.encryptor()
ct2 = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()
print(decryptor.update(ct2) + decryptor.finalize())

# Hashing

digest = hashes.Hash(hashes.SHA256())
digest2 = hashes.Hash(hashes.SHA3_256())
digest.update(b"ab")  # updates hash object, equivalent to concatenation of all arguments
digest.update(b"cd")
digest2.update(b"ab")
digest2.update(b"cd")

myDigest = digest.finalize()  # finalize current context, no longer can be updated
print(myDigest)
myDigest2 = digest2.finalize()
print(myDigest2)

# HMAC using SHA-256
h = hmac.HMAC(key, hashes.SHA256())
h.update(b"message to hash")
signature = h.finalize()
print(signature)

# HMAC using SHA3-256
h2 = hmac.HMAC(key, hashes.SHA3_256())
h2.update(b"message to hash")
signature2 = h2.finalize()
print(signature2)
