'''
Encode
    for i = 0; i<countChar(s); i++
        printf(%d, 1337 + s[i])

    1412 1404 1421 1407 1460 1452 1386 1414 1449 1445 1388 1432 1388 1415 1436 1385 1405 1388 1451 1432 1386 1388 1388 1392 1462
'''
def conver2char(i):
    return chr(int(i)-1337)
lst = list(map(conver2char,input().split()))
print(''.join(lst))