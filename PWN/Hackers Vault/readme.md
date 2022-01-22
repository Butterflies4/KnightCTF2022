# Hackers Vault
## Mô tả
> Knight Squad members are using a hacker vault to store a secret. Can you find our their secret ?            
> nc 198.211.115.81:9999            
> Flag Format : KCTF{Fl4g_H3R3}            
> Author : NomanProdhan       

File binary: [hackers_vault](https://github.com/Butterflies4/KnightCTF2022/edit/main/PWN/Hackers%20Vault/hackers_vault)

## Phân tích
Kiểm tra file và checksec
![image](https://user-images.githubusercontent.com/62021009/150630602-6e4af6a2-9708-4892-97ad-15b632d5b4e9.png)

Sử dụng IDA Pro để xem mã giả của chương trình       
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4[2]; // [rsp+0h] [rbp-10h] BYREF
  int v5; // [rsp+8h] [rbp-8h]
  int v6; // [rsp+Ch] [rbp-4h]

  setvbuf(_bss_start, 0LL, 2, 0LL);
  puts("Welcome to Hackers Vault...");
  printf("Please enter your pass code : ");
  v6 = 0;
  v5 = 0;
  __isoc99_scanf("%d", v4);
  while ( v4[0] )
  {
    v4[1] = v4[0] % 10;
    v5 += v4[0] % 10;
    ++v6;
    v4[0] /= 10;
  }
  if ( v5 == 0x30 )
  {
    puts("\n");
    puts("Welcome to your vault...");
    puts("Your Secret : ");
    system("cat /home/hacker/flag.txt");
  }
  else
  {
    puts("Wrong pass code");
  }
  return 0;
}
```
Nói sơ về chương trình một chút
- v4 là mảng số nguyên gồm 2 phần tử, chương trình yêu cầu ta nhập v4[0]
- v5 sẽ là tổng chữ số của v4[0]

## Solution
Chương trình sẽ kiểm tra v5 và 0x30 (48 trong hệ 10). Như vậy, ta chỉ cần nhập một số có tổng chữ số bằng 48 là xong
![image](https://user-images.githubusercontent.com/62021009/150630734-48bc845a-7f30-4569-80ed-8287e9e04416.png)      
> Flag: KCTF{b1NaRy_3xOpL0iTaT1On_r0cK5}
