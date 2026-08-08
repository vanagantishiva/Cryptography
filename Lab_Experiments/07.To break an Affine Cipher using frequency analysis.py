ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

freq = {}
for ch in ciphertext:
    if ch not in freq:
        freq[ch] = 0
    freq[ch] += 1

print("Character frequencies:")
for k,v in freq.items():
    print(k, ":", v)

# Example substitution mapping
decoded = ""
for ch in ciphertext:
    if ch == '‡': decoded += 'e'
    elif ch == '4': decoded += 't'
    elif ch == '8': decoded += 'h'
    else: decoded += ch
print("\nPartial decoded text:\n", decoded)


'''
output:
Character frequencies:
5 : 12
3 : 4
‡ : 15
† : 8
0 : 6
) : 16
6 : 11
* : 14
; : 27
4 : 19
8 : 34
2 : 5
. : 1
¶ : 2
] : 1
: : 4

 : 3
( : 9
9 : 5
? : 3
— : 1
1 : 7

Partial decoded text:
 53ee†305))6*;th26)te.)te);h06*;th†h¶60))h5;;]h*;:e*h†h3
(hh)5*†;t6(;hh*96*?;h)*e(;th5);5*†2:*e(;t956*2(5*—t)h¶h*
;t0692h5);)6†h)tee;1(e9;th0h1;h:he1;th†h5;t)th5†52hh06*h1
(e9;th;(hh;t(e?3t;th)te;161;:1hh;e?;
'''
