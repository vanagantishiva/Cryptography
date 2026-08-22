def xor(a,b):
    return ''.join(str(int(x)^int(y)) for x,y in zip(a,b))

iv = "10101010"

plaintext = input("Enter 8-bit plaintext: ")
key = input("Enter 10-bit key: ")

cipher = xor(plaintext, iv)

print("Ciphertext :", cipher)

decrypted = xor(cipher, iv)

print("Decrypted Text :", decrypted)
