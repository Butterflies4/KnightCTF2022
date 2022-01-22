# What's Your Name
## Mô tả
> Let us know your good name.             
> nc 198.211.115.81 10001           
> Flag Format : KCTF{S0m3_T3xT_H3r3}               
> Author : NomanProdhan

File binary `whats_your_name`
## Phân tích
Kiểm tra file và checksec
![image](https://user-images.githubusercontent.com/62021009/150630898-a1e55629-c759-48a6-b30f-9937daec832b.png)
Sử dụng IDA Pro để xem mã giả của chương trình    
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[60]; // [rsp+0h] [rbp-40h] BYREF
  int v5; // [rsp+3Ch] [rbp-4h]

  v5 = 100;
  printf("What's your name ? ");
  fflush(_bss_start);
  gets(v4, argv);
  printf("Welcome %s \n", v4);
  fflush(_bss_start);
  if ( v5 != 100 )
    system("cat /home/hacker/flag.txt");
  return 0;
}
```
Chương trình sẽ lấy input từ người dùng, lưu vào biến v4 và sau đó in ra `Welcome + v4`      
Biến v5 ban đầu được gán bằng 100, sau đó chương trình có kiểm tra nếu biến v5 đã bị thay đổi thì sẽ lấy flag cho ta :D
## Solution
Chúng ta sẽ sử dụng buffer overflow để ghi đè dẫn đến thay đổi giá trị của biến v5          
Ở đây, ta thấy biến v4 nằm ở vị trí `rbp-0x40`, biến v5 nằm ở `rbp-0x4`, như vậy ta chỉ cần có padding đủ lớn (cụ thể là lớn hơn hoặc bằng 60) thì sẽ thay đổi được biến v5
![image](https://user-images.githubusercontent.com/62021009/150631091-492c09ad-7bbb-466b-ae11-464b9be132e9.png)     
> Flag: KCTF{bAbY_bUfF3r_0v3Rf1Ow}
