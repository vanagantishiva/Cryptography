def left_shift(bits, n):
    return bits[n:] + bits[:n]


# DES shift schedule
shift_schedule = [
    1, 1, 2, 2,
    2, 2, 2, 2,
    1, 2, 2, 2,
    2, 2, 2, 1
]


def generate_keys(key_56):
    keys = []
    
    # Split 56-bit key into two 28-bit halves
    C = key_56[:28]
    D = key_56[28:]

    for shift in shift_schedule:
        C = left_shift(C, shift)
        D = left_shift(D, shift)

        combined = C + D

        # For demonstration, use first 48 bits
        keys.append(combined[:48])

    return keys


key = "101010101011101100001001000110000010011100110110"

keys = generate_keys(key)

print("DES Encryption Keys:")

for i, k in enumerate(keys):
    print(f"K{i + 1:2d} =", k)

print("\nDES Decryption Key Order:")

for i, k in enumerate(reversed(keys)):
    print(f"K{16 - i:2d} =", k)
