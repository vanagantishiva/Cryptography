
key = input("Enter 26-letter key: ").upper()
plain = input("Enter plaintext: ").upper()
cipher = ""
for ch in plain:
    if ch.isalpha():
        index = ord(ch) - ord('A')
        cipher += key[index]
    else:
        cipher += ch
print("Ciphertext:", cipher)
