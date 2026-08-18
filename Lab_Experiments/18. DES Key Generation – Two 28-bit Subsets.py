def left_shift(bits, n):
    return bits[n:] + bits[:n]


shift_schedule = [
    1, 1, 2, 2,
    2, 2, 2, 2,
    1, 2, 2, 2,
    2, 2, 2, 1
]


key_56 = (
    "10101010101110110000100100011000"
    "0010011100110110"
)

C = key_56[:28]
D = key_56[28:]

print("Initial 28-bit subset C:")
print(C)

print("\nInitial 28-bit subset D:")
print(D)

print("\nGenerated subkeys:")

for round_no, shift in enumerate(shift_schedule, start=1):

    C = left_shift(C, shift)
    D = left_shift(D, shift)

    # Demonstration of 48-bit subkey formation
    subkey = C[:24] + D[:24]

    print(f"K{round_no:2d} =", subkey)
