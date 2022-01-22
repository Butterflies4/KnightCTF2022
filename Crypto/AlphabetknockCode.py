table = [
    ['a','b','c','d','e','f'],
    ['g','h','i','j','l','m'],
    ['n','o','p','q','r','s'],
    ['u','t','v','w','x','y'],
]
cipher = "... ......  . .....  . ...  ... .....  . .....  .... ..  . ...  ... .  .. ...  .. .  .. ..  .... .."
for x in cipher.split("  "):
    tmp = x.split()
    print(table[len(tmp[0])-1][len(tmp[1])-1],end='')

'''
secreucnighu
secreuknighu
SECRETKNIGHT --> flag
'''