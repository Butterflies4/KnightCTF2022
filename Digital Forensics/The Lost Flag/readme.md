# The Lost Flag
## Description
> We recovered a image file from an incident. There might be something interesting in the file. Give it a try.        
> Flag Format: KCTF{pla1n_t3xt_here}       
> Author : TareqAhamed

File [Lost Flag.png](https://github.com/Butterflies4/KnightCTF2022/blob/main/Digital%20Forensics/The%20Lost%20Flag/Lost%20Flag%20.png)
## Solution
Sử dụng [stegsolve](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve)       
Download file `stegsolve.jar` và chạy lệnh
```java
java -jar stegsolve.jar
```
![image](https://user-images.githubusercontent.com/62021009/150629866-96231c70-c876-4b53-a744-0670b897e2da.png)        
Sau khi chạy lệnh trên, thì giao diện hình như trên, tiến hành open file `Lost Flag .jpg`      
Tại red plane 0, ta thấy flag :3     
![image](https://user-images.githubusercontent.com/62021009/150631890-2772196f-5648-455c-8891-2aaca4315307.png)     
> Flag: KCTF{Y0U_F0uNd_M3}
