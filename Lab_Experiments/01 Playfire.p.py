key = input("Enter Key: ").upper().replace("J", "I")
text = input("Enter Plaintext: ").upper().replace("J", "I")
matrix = []
for ch in key:
    if ch.isalpha() and ch not in matrix:
        matrix.append(ch)
for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in matrix:
        matrix.append(ch)
print("\nPlayfair Matrix:")
for i in range(0, 25, 5):
    print(matrix[i:i+5])
plain = ""
i = 0
while i < len(text):
    if text[i].isalpha():
        plain += text[i]
    i += 1
prepared = ""
i = 0
while i < len(plain):
    a = plain[i]
    if i + 1 < len(plain):
        b = plain[i + 1]
        if a == b:
            prepared += a + "X"
            i += 1
        else:
            prepared += a + b
            i += 2
    else:
        prepared += a + "X"
        i += 1
print("\nPrepared Text:", prepared)
cipher = ""
for k in range(0, len(prepared), 2):
    a = prepared[k]
    b = prepared[k + 1]
    for i in range(5):
        for j in range(5):
            if matrix[i * 5 + j] == a:
                r1, c1 = i, j
            if matrix[i * 5 + j] == b:
                r2, c2 = i, j
    if r1 == r2:
        cipher += matrix[r1 * 5 + (c1 + 1) % 5]
        cipher += matrix[r2 * 5 + (c2 + 1) % 5]
    elif c1 == c2:
        cipher += matrix[((r1 + 1) % 5) * 5 + c1]
        cipher += matrix[((r2 + 1) % 5) * 5 + c2]
    else:
        cipher += matrix[r1 * 5 + c2]
        cipher += matrix[r2 * 5 + c1]
print("Cipher Text:", cipher)
