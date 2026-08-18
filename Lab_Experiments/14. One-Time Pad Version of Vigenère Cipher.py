def encrypt(plaintext, key):
    result = ""
    key_index = 0

    for ch in plaintext:
        if ch.isalpha():
            p = ord(ch.lower()) - ord('a')
            c = (p + key[key_index]) % 26
            result += chr(c + ord('a'))
            key_index += 1

    return result


def decrypt(ciphertext, key):
    result = ""

    for i, ch in enumerate(ciphertext):
        c = ord(ch.lower()) - ord('a')
        p = (c - key[i]) % 26
        result += chr(p + ord('a'))

    return result

plaintext = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt(plaintext, key)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)

new_plaintext = "cash not needed"
new_plaintext = new_plaintext.replace(" ", "")

new_key = []

for i in range(len(new_plaintext)):
    c = ord(ciphertext[i]) - ord('a')
    p = ord(new_plaintext[i]) - ord('a')
    new_key.append((p - c) % 26)

print("\nRequired key for Part (b):")
print(new_key)

print("Decrypted text:",
      decrypt(ciphertext, new_key))
