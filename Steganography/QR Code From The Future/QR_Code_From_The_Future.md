# QR Code From The Future
## Description
> The following file was found in a device from a crashed UFO.      
> Can you solve that mystery?             
> Author : marufmurtuza      
Một file `QR_Code_From_The_Future.gif` được cung cấp
## Solution
Đầu tiên, sử dụng [web này](https://ezgif.com/) để cắt từng frame trong file gif      
![image](https://user-images.githubusercontent.com/62021009/150628840-d7356173-5ad7-41f3-8317-72c7e8e2df44.png)         
Ta được 48 frame hình ảnh, mỗi hình ảnh là một mã QR, khi scan thì ta sẽ được 1 kí tự.     
Ở đây, mình sẽ tiến hành capture 48 frame thành 2 hình (1 hình 40 frame và hình còn lại chứa 8 frame) và sử dụng `zbarimg` để tiến hành scan QR         
![image](https://user-images.githubusercontent.com/62021009/150629032-6445b65e-d6d9-4caf-91f2-0a4b78838269.png)        
Nối 2 chuỗi ta được `pbqr_tbg_ribyirq_sebz_fgngvp_gb_qlanzvp}GPXSE{_D`        
Có vẻ như chuỗi này đã được encode ROT13, thử decode xem sao         
![image](https://user-images.githubusercontent.com/62021009/150629152-789aaa2d-a6f3-43a6-a5b0-7a9315d38a92.png)
Sắp xếp lại một chút cho đúng flag thì ta được flag     
> Flag: KCTF{QR_code_got_evolved_from_static_to_dynamic}
## References
https://github.com/Stirring16/DownUnderCTF-2021/tree/main/Forensics/How%20to%20pronounce%20GIF      
https://www.youtube.com/watch?v=SrBYVkTVZyw
