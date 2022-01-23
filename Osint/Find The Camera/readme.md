# Find The Camera
## Description
> Can you find the manufacturer and the model number of the camera that took the picture of this bus?            
> Note: The whole flag is in Upper Case letters and replace any special character or space with underscores.            
> Flag Format: KCTF{MANUFACTURER_MODEL_SINGLELETTERNUMBER}                    
> Author : marufmurtuza

File [Bus.png](https://github.com/Butterflies4/KnightCTF2022/edit/main/Osint/Find%20The%20Camera/Bus.png)
## Solution
![image](https://user-images.githubusercontent.com/62021009/150681802-d60be843-aa28-4e32-9f72-d56ba2d05b49.png)         
Ta để ý trên hình có dòng chữ &copy;JenCh012 và số trên xe bus là 206. Google search với từ khoá `JenCh012 206`, ta tìm được trang web https://fotobus.msk.ru/vehicle/204172/?lang=en             
![image](https://user-images.githubusercontent.com/62021009/150681949-aa5e4180-bb89-4ab7-abd2-e65ec2a77510.png)
Ta tìm được ảnh gốc ở đây https://fotobus.msk.ru/photo/267442/?vid=204172, và các thông số kĩ thuật ở đây       
![image](https://user-images.githubusercontent.com/62021009/150681999-3efd3d18-3f87-4a61-8663-e1be307a6c31.png)
Ta có được model của máy ảnh là `DSC-S980`, tuy nhiên vẫn không biết nhà sản xuất. Google search với từ khoá `DSC-S980` ta tra được nhà sản xuất là SONY
> Flag: KCTF{SONY_DSC_S980}
