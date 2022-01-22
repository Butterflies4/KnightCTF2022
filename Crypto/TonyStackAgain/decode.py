import base64
cipher = "JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M="

# cipher = "YENpU2VrPGlgQ0MlalNgQw=="
l_c = ''.join(chr(c) for c in range (97,123)) 
u_c = ''.join(chr(c) for c in range (65,91)) 
l_e = l_c[13:] + l_c[:13]
u_e = u_c[13:] + u_c[:13]
so = ""
cipher = base64.b64decode(cipher).decode("ascii")
# print(cipher)
def get_key(dic, val):
    for key, value in dic.items():
        if val == value:
            return key
 
    return "key doesn't exist"

d2  = { "~" : "A",
        "`" : "B",
        "@" : "C",
        "#" : "D",
        "$" : "E",
        "%" : "F",
        "^" : "G",
        "&" : "H",
        "*" : "I",
        "(" : "J",
        ")" : "K",
        "-" : "L",
        "_" : "M",
        "=" : "N",
        "+" : "O",
        "{" : "P",
        "[" : "Q",
        "]" : "R",
        ":" : "S",
        ";" : "T",
        "\'" : "U",
        "\"" : "V",
        "," : "W",
        "<" : "X",
        "." : "Y",
        ">" : "Z",
        "?" : "a",
        "/" : "b",
        "5" : "c",
        "1" : "d",
        "4" : "e",
        "2" : "f",
        "3" : "g",
        "9" : "h",
        "0" : "i",
        "8" : "j",
        "6" : "k",
        "7" : "l",
        "K" : "m",
        "Q" : "n",
        "F" : "o",
        "V" : "p",
        "X" : "q",
        "D" : "r",
        "S" : "s",
        "A" : "t",
        "J" : "u",
        "N" : "v",
        "M" : "w",
        "P" : "x",
        "I" : "y",
        "T" : "z",
        "A" : "~",
        "B" : "`",
        "C" : "*",
        "D" : "#",
        "E" : "$",
        "F" : "%",
        "G" : "^",
        "H" : "&",
        "I" : "@",
        "J" : "(",
        "K" : ")",
        "L" : "-",
        "M" : "_",
        "N" : "=",
        "O" : "+",
        "P" : "{",
        "Q" : "[",
        "R" : "]",
        "S" : ":",
        "T" : ";",
        "U" : "\'",
        "V" : "\"",
        "W" : ",",
        "X" : "<",
        "Y" : ".",
        "Z" : ">",
        "a" : "?",
        "b" : "/",
        "c" : "5",
        "d" : "7",
        "e" : "3",
        "f" : "2",
        "g" : "4",
        "h" : "9",
        "i" : "0",
        "j" : "8",
        "k" : "6",
        "l" : "1",
        }
d1  = { "A" : "~",
        "B" : "`",
        "C" : "@",
        "D" : "#",
        "E" : "$",
        "F" : "%",
        "G" : "^",
        "H" : "&",
        "I" : "*",
        "J" : "(",
        "K" : ")",
        "L" : "-",
        "M" : "_",
        "N" : "=",
        "O" : "+",
        "P" : "{",
        "Q" : "[",
        "R" : "]",
        "S" : ":",
        "T" : ";",
        "U" : "\'",
        "V" : "\"",
        "W" : ",",
        "X" : "<",
        "Y" : ".",
        "Z" : ">",
        "a" : "?",
        "b" : "/",
        "c" : "5",
        "d" : "1",
        "e" : "3",
        "f" : "2",
        "g" : "4",
        "h" : "9",
        "i" : "0",
        "j" : "8",
        "k" : "6",
        "l" : "7",
        "m" : "K",
        "n" : "Q",
        "o" : "F",
        "p" : "V",
        "q" : "X",
        "r" : "D",
        "s" : "S",
        "t" : "A",
        "u" : "J",
        "v" : "N",
        "w" : "M",
        "x" : "P",
        "y" : "I",
        "z" : "T",
        "~" : "A",
        "`" : "B",
        "@" : "C",
        "#" : "D",
        "$" : "E",
        "%" : "F",
        "^" : "G",
        "&" : "H",
        "*" : "I",
        "(" : "J",
        ")" : "K",
        "-" : "L",
        "_" : "M",
        "=" : "N",
        "+" : "O",
        "{" : "P",
        "[" : "Q",
        "]" : "R",
        ":" : "S",
        ";" : "T",
        "\'" : "U",
        "\"" : "V",
        "," : "W",
        "<" : "X",
        "." : "Y",
        ">" : "Z",
        "?" : "a",
        "/" : "b",
        "5" : "c",
        "1" : "d",
        "3" : "e",
        "2" : "f",
        "4" : "g",
        "9" : "h",
        "0" : "i",
        "8" : "j",
        "6" : "k",
        "7" : "l",
        }
vas1 = ""
saa2t = ''
for i in cipher:
    saa2t = get_key(d2,i) + saa2t
arr2= [ord(c) for c in saa2t]
print(arr2)
for c in arr2:
    tmp = get_key(d1,chr(c - 1))
    if tmp in l_c:
        print(l_e[l_c.find(tmp)],end='')
    elif tmp in u_c:
        print(u_e[u_c.find(tmp)],end='')
    else:
        print(tmp,end='')
print()
for c in arr2:
    tmp = get_key(d1,chr(c - 2))
    if tmp in l_c:
        print(l_e[l_c.find(tmp)],end='')
    elif tmp in u_c:
        print(u_e[u_c.find(tmp)],end='')
    else:
        print(tmp,end='')
'''
nuHHzAH@HajG@p'Anju+lljA3lojAlljZH3jAq3nG$S$
MwUUhKU`Uk-F`tmKM-wi&&-K1&L-K&&-TU1-Kv1MFeRe

MwUUhKU@Uk-F@pmAn-will-K1lL-All-TH3-Av3nGeR$
'''
# JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=
# JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=
# JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=
  JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=