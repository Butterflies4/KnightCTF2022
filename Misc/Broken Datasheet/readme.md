# Broken Datasheet
## Description
> One of my friend sent me an important datasheet to me. But the sheet seems broken. Can you please help me to recover or read the datasheet.      
> Flag Format: KCTF{S0m3_TexT_H3re}        
> Author: marufmurtuza

File
## Solution
Sau khi tìm hiểu, thì các file powerpoint, excel thực chất là những file zip.     
Tiến hành unzip file excel         
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ file Broken\ Datasheet.xlsx 
Broken Datasheet.xlsx: Zip archive data, at least v2.0 to extract
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ unzip Broken\ Datasheet.xlsx 
Archive:  Broken Datasheet.xlsx
replace Broken Datasheet.xlsx? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: Broken Datasheet.xlsx   
  inflating: [Content_Types].xml     
  inflating: _rels/.rels             
  inflating: docProps/app.xml        
  inflating: docProps/core.xml       
  inflating: xl/_rels/workbook.xml.rels  
  inflating: xl/styles.xml           
  inflating: xl/theme/theme1.xml     
  inflating: xl/workbook.xml         
  inflating: xl/worksheets/sheet1.xml
```
Sử dụng `tree` để xem cây thư mục
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ tree ../Broken\ Datasheet 
../Broken Datasheet
├── Broken Datasheet.xlsx
├── [Content_Types].xml
├── docProps
│   ├── app.xml
│   └── core.xml
├── _rels
└── xl
    ├── _rels
    │   └── workbook.xml.rels
    ├── styles.xml
    ├── theme
    │   └── theme1.xml
    ├── workbook.xml
    └── worksheets
        └── sheet1.xml

6 directories, 9 files
```
Xem từng file và không thấy có gì, ta tiếp tục unzip một lần nữa file excel xem có còn file nào khác nữa không     
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ unzip Broken\ Datasheet.xlsx 
Archive:  Broken Datasheet.xlsx
replace [Content_Types].xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: [Content_Types].xml     
replace _rels/.rels? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: _rels/.rels             
replace xl/workbook.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/workbook.xml         
replace xl/_rels/workbook.xml.rels? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/_rels/workbook.xml.rels  
replace xl/worksheets/sheet1.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/worksheets/sheet1.xml  
replace xl/theme/theme1.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/theme/theme1.xml     
replace xl/styles.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/styles.xml           
replace xl/sharedStrings.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: xl/sharedStrings.xml    
replace docProps/core.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: docProps/core.xml       
replace docProps/app.xml? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: docProps/app.xml 
```
Ta thấy có thêm 1 file nữa là `sharedStrings.xml`, kiểm tra file này
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ file xl/sharedStrings.xml 
xl/sharedStrings.xml: XML 1.0 document, ASCII text, with very long lines
```
Đây là file text, đọc nội dung file thì ta nhận được flag :3      
```
┌──(kali㉿kali)-[~/Documents/KnightCTF/Mics/Broken Datasheet]
└─$ cat xl/sharedStrings.xml 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="4" uniqueCount="4"><si><t xml:space="preserve">                                                                                                           .     </t></si><si><t xml:space="preserve">    </t></si><si><t>KCTF{XLSX_Fil3$_4R3_Actually_0n3_Kind_0f_Zip_Fil3}</t></si><si><t xml:space="preserve">   </t></si></sst>
```
> Flag: KCTF{XLSX_Fil3$_4R3_Actually_0n3_Kind_0f_Zip_Fil3}
