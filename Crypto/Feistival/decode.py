cipher = open("cipher.txt", "r").read()
# ciparr = [ord(x) for x in cipher]
m, n = 21, 22
def f(word, key):
    out = ""
    for i in range(len(word)):
        out += chr(ord(word[i]) ^ key)
    return out

L, R = cipher[0:len(cipher)//2], cipher[len(cipher)//2:]
L = "".join(chr(ord(f(R, n)[i]) ^ ord(L[i])) for i in range(len(L)))
tmp = R
R = L
L = tmp
L = "".join(chr(ord(f(R, m)[i]) ^ ord(L[i])) for i in range(len(L)))

print(L+R)