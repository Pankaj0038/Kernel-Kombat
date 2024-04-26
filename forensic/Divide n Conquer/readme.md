# Challenge Name: Divide n Conquer

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
   
