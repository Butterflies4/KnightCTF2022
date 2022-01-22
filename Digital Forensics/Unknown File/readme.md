# Unknown File
## Description
> My friend sent me a file & told me there is a flag in it. He dare me to find the flag. But I have no idea what the file is about. Can you help me get the flag?        
> Flag Format: KCTF{pla1n_t3xt_here}      
> Author : TareqAhamed

File [unknown file](https://github.com/Butterflies4/KnightCTF2022/blob/main/Digital%20Forensics/Unknown%20File/unknown%20file)
## Solution
Tham khảo [trang này](https://www.garykessler.net/library/file_sigs.html) để kiểm tra file signature, thì ta thấy 8 bytes đầu của file bị sai. Ta sửa lại thành định dạng png `89 50 4E 47`    
Sử dụng `hexedit` để sửa 8 bytes đầu tiên, sau đó sửa đuôi thành png
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Unknown File]
└─$ hexedit unknown\ file
```
Mở file png và ta có flag     
> KCTF{Imag3_H3ad3r_M4nipul4t10N}
