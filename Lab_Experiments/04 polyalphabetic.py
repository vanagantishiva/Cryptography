plaintext = input("Enter Plaintext: ").upper()
key = input("Enter Key: ").upper()

cipher = ""
j = 0

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[j % len(key)]) - ord('A')
        c = (p + k) % 26
        cipher += chr(c + ord('A'))
        j += 1
    else:
        cipher += plaintext[i]

print("Cipher Text:", cipher)
