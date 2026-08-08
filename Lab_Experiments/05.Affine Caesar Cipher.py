from math import gcd

text = input("Enter Plain Text: ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid value of a")
else:
    cipher = ""

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            cipher = cipher + chr(c + 65)
        else:
            cipher = cipher + ch

    print("Cipher Text =", cipher)


'''
Enter Plain Text: power bank
Enter value of a: 3
Enter value of b: 7
Cipher Text = AXVTG KHUL
'''