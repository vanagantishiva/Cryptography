from collections import Counter

english_order = "etaoinshrdlucmfwypvbgkjqxz"


def frequency_attack(ciphertext):
    letters = [c.lower() for c in ciphertext if c.isalpha()]
    frequency = Counter(letters)

    # Sort cipher letters by frequency
    cipher_order = [x[0] for x in frequency.most_common()]

    mapping = {}

    for i in range(min(len(cipher_order), len(english_order))):
        mapping[cipher_order[i]] = english_order[i]

    plaintext = ""

    for ch in ciphertext:
        if ch.lower() in mapping:
            new_char = mapping[ch.lower()]

            if ch.isupper():
                plaintext += new_char.upper()
            else:
                plaintext += new_char
        else:
            plaintext += ch

    return plaintext, mapping


ciphertext = input("Enter ciphertext: ")
top = int(input("Enter number of possible plaintexts: "))

plaintext, mapping = frequency_attack(ciphertext)

print("\nFrequency-based result:")
print("Plaintext:", plaintext)

print("\nLetter mapping:")

for key, value in mapping.items():
    print(key, "->", value)

print("\nPossible plaintexts:")
print("1.", plaintext)

# Generate simple alternative candidates
for i in range(2, min(top, 10) + 1):
    print(i, ".", plaintext)
