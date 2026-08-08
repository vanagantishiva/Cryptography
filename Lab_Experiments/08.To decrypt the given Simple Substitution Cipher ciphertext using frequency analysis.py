plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "CIPHERABDFGJKLMNOQSTUVWXYZ"
message = "attack at dawn"

result = ""
for ch in message:
    if ch == " ":
        result += " "
    else:
        idx = plain.index(ch)
        result += cipher[idx]
print("Ciphertext:", result)
