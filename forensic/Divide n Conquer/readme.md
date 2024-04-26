# Challenge Name: Divide n Conquer
Author: **purb03ragnarok**

## Description:
Bruh!! binwalk not binwalking? Try harder.  
Flag Format: kernelkombat{Y0urM3ss4g3}

File attached: [bruh.gif](bruh.gif)

## Solution:
1. As the challenge description suggests, use the binwalk command on the given gif file.
   > binwalk -e /path/to/bruh.gif
   
   ![Alt text](images/ss1.png?raw=true)  
   Clearly you can see there are 2 GIF files but no extracted folder created.

2. Try to see the hexadecimal dump of this file
   > xxd /path/to/bruh.gif

   ![Alt text](images/ss2.png?raw=true)  
   The hexadecimal dump of 2 GIF files are added one after the other.

3. I wrote this [script.py](script.py) to obtain the 2 GIF files from [bruh.gif](bruh.gif)  
   You can obtain the size of first GIF from here:
   ![Alt text](images/ss3.png?raw=true)

4. This is the [second GIF](images/hexahue.gif) which you will get using [script.py](script.py).  
   You may use this [link](https://ezgif.com/split) to extract all frames from this GIF.  
   This is **HEXAHUE** cipher which can be decrypted [here](https://www.dcode.fr/hexahue-cipher).  
   ![Alt text](images/ss4.png?raw=true)


FLAG: kernelkombat{EWWBROTHERWHATSTHAT69034}
