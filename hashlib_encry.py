import hashlib
import binascii

hash = hashlib.md5()

hash.update('ain88088'.encode('utf-8'))

print(hash.hexdigest())
print(hash.digest())
print(binascii.unhexlify(hash.hexdigest()))