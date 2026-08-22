def pad(data, block_size=8):
    data += "1"
    while len(data) % block_size != 0:
        data += "0"
    return data

plaintext = input("Enter binary plaintext: ")

padded = pad(plaintext)

print("Original Plaintext :", plaintext)
print("Padded Plaintext   :", padded)
print("ECB Mode           :", padded)
print("CBC Mode           :", padded)
print("CFB Mode           :", padded)
