import aes

key = open("key.txt", "r").read().encode("cp1252")

message = aes.get_plaintext()

iv, ct, tag = aes.encrypt(key, message, b"authenticated but not encrypted payload")

print(aes.decrypt(key, b"authenticated but not encrypted payload", iv, ct, tag))
