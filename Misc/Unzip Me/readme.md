# Unzip Me
## Description
> Can you unzip the file ?         
> Flag Format: KCTF{S0m3_T3xt_H3re}          
> Author: NomanProdhan

File 
## Solution
Như đề bài yêu cầu, ta cần giải nén file này ra.
Kiểm tra file thì thấy được nén theo gzip      
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Unzip me]
└─$ file unzipme.tar.gz             
unzipme.tar.gz: gzip compressed data, last modified: Tue Jan 11 21:49:36 2022, from Unix, original size modulo 2^32 2048
```
Giải nén file gzip bằng lệnh `gzip -d unzipme.tar.gz`     
File sau khi được giải nén là `unzipme.tar` và được nén theo tar     
Tiếp tục giải nén `tar -xf unzipme.tar`     
Ta được file `unzipme`, kiểm tra kiểu file thì thấy đây là file data.      
![image](https://user-images.githubusercontent.com/62021009/150647491-30a5cac1-7013-49d3-b083-caa26f3fa7c4.png)        
Lấy nội dung của file     
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Unzip me]
└─$ cat unzipme    
KP�T,|�Glfgat.txCKFTs{_OOy_uWsPa3P_DHt_e1f3L
}KP?�T,|�G��lfgat.txKP6D
```
Ta nhận thấy có đoạn flag, tuy nhiên các bytes của flag đã bị đảo, lần lượt 2 byte sẽ bị đảo vị trí cho nhau. Sử dụng [CyberChef](https://gchq.github.io/CyberChef), chọn `Swap endianess`, `Data Format` là Raw và `Word length` là 2       
![image](https://user-images.githubusercontent.com/62021009/150647770-33136f24-07ef-401d-861e-f7ba65cd2960.png)
> Flag KCTF{sO_yOu_sWaPP3D_tHe_f1L3}
