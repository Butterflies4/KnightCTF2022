# Let's Walk Together
## Description
> Do you know anything about this image?     
> Flag Format: KCTF{S0m3_Tex7_H3re}     
> Author: TareqAhmed       

File [interesting_waves.png](https://github.com/Butterflies4/KnightCTF2022/edit/main/Digital%20Forensics/Let's%20Walk%20Together/interesting_waves.png)
## Solution
Sử dụng binwalk để kiểm tra có file nào bị nén không       
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Let's Walk Together]
└─$ binwalk interesting_waves.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1024 x 768, 8-bit/color RGBA, non-interlaced
99            0x63            Zlib compressed data, best compression
69968         0x11150         Zip archive data, at least v1.0 to extract, name: Flag/
70031         0x1118F         Zip archive data, encrypted at least v1.0 to extract, compressed size: 37, uncompressed size: 25, name: Flag/flag.txt
70313         0x112A9         End of Zip archive, footer length: 22

```
Ta thấy có file zip chứa `flag.txt`, tiến hành giải nén các file này ra         
```   
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Let's Walk Together]
└─$ binwalk -e interesting_waves.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1024 x 768, 8-bit/color RGBA, non-interlaced
99            0x63            Zlib compressed data, best compression
69968         0x11150         Zip archive data, at least v1.0 to extract, name: Flag/
70031         0x1118F         Zip archive data, encrypted at least v1.0 to extract, compressed size: 37, uncompressed size: 25, name: Flag/flag.txt
70313         0x112A9         End of Zip archive, footer length: 22

                                                                                                                                                 
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Let's Walk Together]
└─$ ls
interesting_waves.png  _interesting_waves.png.extracted
```
Kiểm tra cây thư mục `_interesting_waves.ong.extracted`     
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Let's Walk Together]
└─$ tree _interesting_waves.png.extracted 
_interesting_waves.png.extracted
├── 11150.zip
├── 63
├── 63.zlib
└── Flag
    └── flag.txt

1 directory, 4 files
```
Ta thấy có file flag.txt, tuy nhiên file này là file rỗng        
Tiếp theo, ta tiến hành giải nén file `11150.zip`, tuy nhiên file này yêu cầu mật khẩu    
```
┌──(kali㉿kali)-[~/…/KnightCTF/Digital_Forensics/Let's Walk Together/_interesting_waves.jpg.extracted]
└─$ unzip 11150.zip        
Archive:  11150.zip
[11150.zip] Flag/flag.txt password: 
password incorrect--reenter: 
   skipping: Flag/flag.txt           incorrect password
```
Ta sẽ tiến hành crack zip file với fcrackzip
```
┌──(kali㉿kali)-[~/…/KnightCTF/Digital_Forensics/Let's Walk Together/_interesting_waves.png.extracted]
└─$ fcrackzip -u -D -p /home/kali/Downloads/rockyou.txt 11150.zip                                                                            1 ⨯


PASSWORD FOUND!!!!: pw == letmein!
```
Cool, ta có được password là `letmein!`      
Tiến hành unzip file `11150.zip` với password vừa tìm được      
```
┌──(kali㉿kali)-[~/…/KnightCTF/Digital_Forensics/Let's Walk Together/_interesting_waves.png.extracted]
└─$ unzip 11150.zip
Archive:  11150.zip
[11150.zip] Flag/flag.txt password: 
replace Flag/flag.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
 extracting: Flag/flag.txt
 ```
 Giải nén thành công và ta có flag nằm trong thư mục `/Flag/flag.txt`      
 > Flag: KCTF{BiNw4lk_is_h3lpfUl}       

## Reference
[How to crack zip password on Kali Linux](https://linuxconfig.org/how-to-crack-zip-password-on-kali-linux)
