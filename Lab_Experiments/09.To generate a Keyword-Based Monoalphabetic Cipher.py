matrix = [
    ['M','F','H','I','K'],
    ['U','N','O','P','Q'],
    ['Z','V','W','X','Y'],
    ['E','L','A','R','G'],
    ['D','S','T','B','C']
]

ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS"
pairs = ciphertext.split()

print("Cipher pairs:", pairs)
# Apply Playfair rules manually: same row, same column, rectangle swap


'''
output:
Cipher pairs: ['KXJEY', 'UREBE', 'ZWEHE', 'WRYTU', 'HEYFS']
'''