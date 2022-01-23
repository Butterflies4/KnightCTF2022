# Find the Flag
## Description
> Find the flag from the following file.       
> Flag Format: KCTF{plain_t3xt_here}                
> Author : TareqAhamed

File [file](https://github.com/Butterflies4/KnightCTF2022/edit/main/Networking/Find%20the%20Flag/file)
## Solution
Sử dụng lệnh `strings file` để xem các chuỗi đọc được trong file
![image](https://user-images.githubusercontent.com/62021009/150683327-e01bd491-7644-4473-861b-210258952dc8.png)
> S0NURntGVFBfUDRDSzNUX0M0cFR1cjNfVXNJbmdfV2lyZVNINFJLfQo=

Base64 decode chuỗi trên ta được flag
> Flag: KCTF{FTP_P4CK3T_C4pTur3_UsIng_WireSH4RK}
