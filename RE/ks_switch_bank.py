'''
v6="ZRIU]HdANdJAGDIAxIAvDDsAyDDq_"

while ( v5[v10] )
{
    if ( v5[v10] <= 64 || v5[v10] > 77 )
    {
        if ( v5[v10] <= 96 || v5[v10] > 109 )
        {
            if ( v5[v10] <= 77 || v5[v10] > 90 )
            {
                if ( v5[v10] <= 109 || v5[v10] > 122 )
                v4[v10] = v5[v10] - 32;
                else (110-->122 == n-->z)
                v4[v10] = v5[v10] - 13;
            }
            else (78 -->90 = n -->z)
            {
                v4[v10] = v5[v10] - 13;
            }
        }
        else (97 --> 109 = a-->m)
        {
            v4[v10] = v5[v10] + 13;
        }
    }
    else # 65-->77 (A-->M)
    {
        v4[v10] = v5[v10] + 13;
    }
    ++v10;
}
'''
v6="ZRIU]HdANdJAGDIAxIAvDDsAyDDq_"

for x in v6:
    i = ord(x) - 2
    if 97 <= i <= 109:
        print(chr(i+13),end='')
    elif 110 <= i <= 122:
        print(chr(i-13),end='')
    elif 65 <= i <= 77:
        print(chr(i+13),end='')
    elif 78 <= i <= 90:
        print(chr(i-13),end='')
    else:
        print(chr(i+32),end='')