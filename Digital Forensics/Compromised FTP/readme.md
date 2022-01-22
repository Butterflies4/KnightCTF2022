# Compromised FTP
## Description
> We detected some malicious activity on our FTP server. Someone has performed bruteforce attack to gain access to our FTP server. Find out the Compromised FTP account username & the attacker IP from the following.           
> Flag Format: KCTF{username_127.0.0.1}          
> Author : TareqAhamed

File [ftp.log]
## Solution
Ở đây có chứa rất nhiều phiên đăng nhập từ ip 192.168.19.7, ta tiến hành lọc hết tất cả các log, và tìm log đăng nhập thành công    
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Digital_Forensics/Compromised FTP]
└─$ cat ftp.log| grep OK               
Mon Jan  3 15:24:13 2022 [pid 5399] [ftpuser] OK LOGIN: Client "::ffff:192.168.1.7"
```
> Flag: KCTF{ftpuser_192.168.1.7}
