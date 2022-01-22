'''
v5 = "08'5[Z'Y:H3?X2K3V)?D2G3?H,N6?G$R(G]"
v4 = input()
for i = 0; v4[i]; i++
    if ( v4[i] <= 64 || v4[i] > 90 )
    {
        Nếu 
      if ( v4[i] <= 96 || v4[i] > 122 )
        v4[i] = v4[i];
      else (97->122 = a-->z)
        v4[i] = -37 - v4[i];
    }
    else (65 --> 90 = A-->Z)
    {
      v4[i] = -101 - v4[i];
    }

for ( j = 0; v4[j]; ++j )
    v4[j] -= 32;
'''

v5 = "08'5[Z'Y:H3?X2K3V)?D2G3?H,N6?G$R(G]"
for x in v5:
    tmp = ord(x)+32
    if 97 <= tmp <=122:
        print(chr(256-37-tmp),end='')
    elif 65 <= tmp <=90:
        print(chr(256-101-tmp),end='')
    else:
        print(chr(tmp),end='')