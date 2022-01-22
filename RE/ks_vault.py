'''
v7= "*9J<qiEUoEkU]EjUc;U]EEZU`EEXU^7fFoU^7Y*_D]s"
v8 = input()
for ( i = 0; v8[i]; ++i )
  {
    v8[i + 512] = v8[i] - 10;
    if ( v8[i + 512] == 65 )
      v8[i + 512] = 42;
  }
  v6 = 0;
  v4 = 0;
  while ( v7[v6] )
  {
    if ( v7[v6] != v8[v6 + 512] )
    {
      v4 = 0;
      break;
    }
    v4 = 1;
    ++v6;
  }
'''
v7= "*9J<qiEUoEkU]EjUc;U]EEZU`EEXU^7fFoU^7Y*_D]s" 
for x in v7:
    i = ord(x)
    if i == 42: i=65
    print(chr(i+10),end='')