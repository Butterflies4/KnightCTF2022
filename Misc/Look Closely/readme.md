# Look Closely
## Description
> Look closely & try to find the flag from the following.           
> Flag Format : KCTF{SOM3THING H3R3}           
> Author : Asif Ahmed              

File [look closely.wav](https://github.com/Butterflies4/KnightCTF2022/edit/main/Misc/Look%20Closely/look%20closely.wav)
## Solution
Sử dụng `Audacity` để mở file âm thanh, chọn chế độ hiển thị là Spectrogram          
![image](https://user-images.githubusercontent.com/62021009/150679972-abef84ea-2dd5-4d9a-92e7-5ba5e8672c69.png)       
Ta được một link drive      
![image](https://user-images.githubusercontent.com/62021009/150679999-e0e97920-8e03-45a8-b245-bb853445f746.png)
> https://drive.google.com/file/d/1_6c_waS9ijouTpqI_tUO6VCRf7fE6gCY/view     

Truy cập vào drink, ta thấy có video, xem kĩ video, tại giây thứ 10
![1_1](https://user-images.githubusercontent.com/62021009/150680210-066d9fce-c506-49f5-9672-a68ba81b7238.png)
Ta được chuỗi binary `01001011 01000011 01010100 01000110 01111011 01001000 00110011`          
Và tại giây thứ 52, ta được chuỗi binary `01001100 01001100 01001111 01011111 01001010 00110011 01001100 01001100 01001111 01111101`       
![2-2](https://user-images.githubusercontent.com/62021009/150680850-c62a9eff-fbd3-4ac8-89bf-0831c61a28f1.png)
Nối 2 chuỗi, ta được `01001011 01000011 01010100 01000110 01111011 01001000 00110011 01001100 01001100 01001111 01011111 01001010 00110011 01001100 01001100 01001111 01111101`     
Chuyển binary thành chuỗi ta có flag        
![image](https://user-images.githubusercontent.com/62021009/150680901-efc68876-f362-4201-8b27-558fb3517d38.png)           
> Flag: KCTF{H3LLO_J3LLO}
