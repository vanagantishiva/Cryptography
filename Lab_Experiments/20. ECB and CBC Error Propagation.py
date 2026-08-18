from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"0123456789abcdef"
iv = b"1234567890123456"

plaintext = b"Block1-12345678Block2-12345678"

# ECB Encryption
ecb = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb.encrypt(pad(plaintext, AES.block_size))

# CBC Encryption
cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cbc.encrypt(pad(plaintext, AES.block_size))

print("Original Plaintext:")
print(plaintext)

print("\nECB Ciphertext:")
print(ecb_ciphertext.hex())

print("\nCBC Ciphertext:")
print(cbc_ciphertext.hex())


# Introduce an error in the first ciphertext block
ecb_error = bytearray(ecb_ciphertext)
ecb_error[0] ^= 1

cbc_error = bytearray(cbc_ciphertext)
cbc_error[0] ^= 1


# ECB Decryption
ecb_dec = AES.new(key, AES.MODE_ECB)

try:
    ecb_plaintext = ecb_dec.decrypt(bytes(ecb_error))
    print("\nECB after ciphertext error:")
    print(ecb_plaintext)
except Exception as e:
    print("ECB error:", e)


# CBC Decryption
cbc_dec = AES.new(key, AES.MODE_CBC, iv)

try:
    cbc_plaintext = cbc_dec.decrypt(bytes(cbc_error))
    print("\nCBC after ciphertext error:")
    print(cbc_plaintext)
except Exception as e:
    print("CBC error:", e)
