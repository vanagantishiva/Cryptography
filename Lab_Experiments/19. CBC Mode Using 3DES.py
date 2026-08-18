# CBC Mode Using 3DES - Simple Demonstration

def xor_blocks(block1, block2):
    return bytes(a ^ b for a, b in zip(block1, block2))


def simple_3des(block, key):
    # Educational 3DES-style operation
    result = block

    # Encryption stage 1
    result = bytes((result[i] + key[i % len(key)]) % 256
                   for i in range(len(result)))

    # Encryption stage 2
    result = bytes((result[i] ^ key[i % len(key)])
                   for i in range(len(result)))

    # Encryption stage 3
    result = bytes((result[i] + key[i % len(key)]) % 256
                   for i in range(len(result)))

    return result


def cbc_encrypt(plaintext, key, iv):
    # Convert plaintext to bytes
    data = plaintext.encode()

    # Padding
    while len(data) % 8 != 0:
        data += b' '

    ciphertext = b''
    previous = iv

    # Process 8-byte blocks
    for i in range(0, len(data), 8):
        block = data[i:i + 8]

        # CBC: XOR plaintext with previous ciphertext
        xored = xor_blocks(block, previous)

        # Apply 3DES-style encryption
        encrypted = simple_3des(xored, key)

        ciphertext += encrypted
        previous = encrypted

    return ciphertext


# Input
plaintext = input("Enter plaintext: ")

key = b"12345678"
iv = b"abcdefgh"

# Encryption
ciphertext = cbc_encrypt(plaintext, key, iv)

print("\n--- CBC Mode Using 3DES ---")
print("Plaintext :", plaintext)
print("Key       :", key.decode())
print("IV        :", iv.decode())
print("Ciphertext:", ciphertext.hex())
