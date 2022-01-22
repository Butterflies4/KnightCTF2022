# FileD
## Description
> Can you see everything?              
> Flag Format: KCTF{S0m3_text_h3r3}              
> Author: 1xR1fat

File [filed.kra](https://github.com/Butterflies4/KnightCTF2022/edit/main/Steganography/FileD/filed.kra)
## Solution
Sau khi tìm hiểu thì ta thấy muốn mở được file cần phải cài phần mềm là [krita](https://fileinfo.com/extension/kra)        
Download về và mở hình ảnh lên      
![image](https://user-images.githubusercontent.com/62021009/150646751-d95bd9af-fae5-4d46-9b75-c83f221c1a9b.png)       
Ta nhận thấy có rất nhiều layer, mỗi layer là một hình ảnh khác nhau được chồng lên. Lần lượt remove các layer, đến layer `ctf.png` ta có flag       
![image](https://user-images.githubusercontent.com/62021009/150646858-b2939f96-a2e0-4bb5-807d-c8f2518c8400.png)
> Flag KCTF{W00_n1ce_you_got_me}
