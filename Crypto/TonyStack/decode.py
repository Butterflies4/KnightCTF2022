# cipher = "IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"
cipher = "6G:653"
lst = ['T3NR1NG$', 'T3nR1ng$', 'TenRings', 'T3nR!ngs', 'T3nR!ng$', '73NR1GN$', '73nRing$', 'T3nR!nG$']
secarr = []
keyarr = []
x = 0

def keyfunc(key,keyarr,x):
    for character in key:
        keyarr.append(ord(character))

    for i in keyarr:
        x += i

for key in lst:
    keyarr = []
    for character in key:
        keyarr.append(ord(character))
    x = 0
    for i in keyarr:
        x += i

    ciparr = []
    for character in cipher:
        ciparr.append(ord(character))

    if x - 1 % 2 == 0:
        ciparr[-1] = ciparr[-1] - 3
    else:
        ciparr[-1] = ciparr[-1] - 2

    for i in range(len(ciparr)):
        if 91 <= ciparr[i] <= 116:
            ciparr[i] = ciparr[i]+6
        else:
            if 54 <= ciparr[i] <= 79:
                ciparr[i] = ciparr[i]+11

    for val in ciparr:
        print(chr(val),end='')
    # break
    print()

# Flag: KCTF{AREA51_TonyTheBadBoyGotScaredOfTheFatBoy}

    