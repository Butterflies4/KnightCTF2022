# Follow The White Rabbit
## Description
> Will you choose to follow the white rabbit like NEO? THINK wisely or LOOK your path deeply before you take step.                
> Author: marufmurtuza

File `whiterabbit.jpg`
## Solution
Sử dụng [stegsolve](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve)       
Download file `stegsolve.jar` và chạy lệnh
```java
java -jar stegsolve.jar
```
![image](https://user-images.githubusercontent.com/62021009/150629866-96231c70-c876-4b53-a744-0670b897e2da.png)        
Sau khi chạy lệnh trên, thì giao diện hình như trên, tiến hành open file `whiterabbit.jpg`      
Tại red plane 4, ta thấy có xuất hiện đoạn mã morse      
![image](https://user-images.githubusercontent.com/62021009/150629947-4b8bba2a-e9df-442c-b306-0e5ef7b9a9ef.png)        
Mã morse `.-.. ----- --- -.- -... ....- -.-- ----- ..- .-.. ...-- ....- .--.`     
Decode mã morse, ta được flag
![image](https://user-images.githubusercontent.com/62021009/150630180-85a7a166-977c-4671-a5b1-d40b54ff257e.png)
> Flag KCTF{L0OKB4Y0UL34P}
