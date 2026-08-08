cipher = input("Enter Cipher Text: ").upper()

a = 3
b = 15
a_inv = 9      # Modular inverse of 3 mod 26

plain = ""

for ch in cipher:
    if ch.isalpha():
        c = ord(ch) - 65
        p = (a_inv * (c - b)) % 26
        plain = plain + chr(p + 65)
    else:
        plain = plain + ch

print("Key values:")
print("a =", a)
print("b =", b)
print("Plain Text =", plain)


'''
output:
Enter Cipher Text: american turister
Key values:
a = 3
b = 15
Plain Text = VZFSPNVI KTSPBKFS
'''