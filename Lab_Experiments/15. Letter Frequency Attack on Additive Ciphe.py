from collections import Counter

english_frequency = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5,
    'i': 7.0, 'n': 6.7, 's': 6.3, 'h': 6.1,
    'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8,
    'u': 2.8, 'm': 2.4, 'w': 2.4, 'f': 2.2,
    'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5,
    'v': 1.0, 'k': 0.8, 'j': 0.15, 'x': 0.15,
    'q': 0.10, 'z': 0.07
}


def decrypt(ciphertext, shift):
    result = ""

    for ch in ciphertext:
        if ch.isalpha():
            value = (ord(ch.lower()) - ord('a') - shift) % 26
            result += chr(value + ord('a'))
        else:
            result += ch

    return result


def score(text):
    letters = [ch for ch in text.lower() if ch.isalpha()]
    count = Counter(letters)
    total = len(letters)

    if total == 0:
        return 0

    result = 0

    for ch, freq in english_frequency.items():
        actual = count[ch] / total * 100
        result += abs(actual - freq)

    return -result


ciphertext = input("Enter ciphertext: ")
top = int(input("Enter number of possible plaintexts: "))

results = []

for shift in range(26):
    plaintext = decrypt(ciphertext, shift)
    value = score(plaintext)
    results.append((value, shift, plaintext))

results.sort(reverse=True)

print("\nPossible plaintexts:")

for i in range(min(top, 26)):
    value, shift, plaintext = results[i]
    print(f"{i + 1}. Shift = {shift:2d} : {plaintext}")
