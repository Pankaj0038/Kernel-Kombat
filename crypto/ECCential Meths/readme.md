# Challenge Name: ECCential Meths
Author: purb03ragnarok

## Description:

Do you know Ellipse? Obviously yes(hope so).. What about Elliptic Curve Cryptography? Let's talk about this. Elliptic curves have a strange feature called "POINT ADDITION". This operator takes two points on some curve and produces a third point on the curve. Wooh! let me clear for you once. Take an elliptical curve and mark 2 points A, B along the curve. Draw a straight line that passes through both points and continue it untill it intersects the curve 3rd time. Say the 3rd point be C(x,y). Take the reflection of C along y axis naming it as C'(x,-y). The result of the point addition is A + B = R'.
Wait a second, what if some one gives you to add 2 same points? Try your common sense bro..  
I am giving you a Weierstrass equation E: y^2 = x^3 - 228x + 848 and prime p = 9739
Let A be a point (94, 900). I want you to find point B(x,y) such that B = 1337A.  
    
Flag Format: kernelkombat{x_y}
    
This might help you --> https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication

## Solution:
1. You are provided with a Weierstrass equation which is in the form y^2 = x^3 + ax + b where a=-228 and b=848. The prime p = 9739 denotes the field or region of operation. You have to find B = 1337A means B = A + A + A + ... + A (1337 times) that is addition of same point 1337 times. Addition of same point signifies that if you take a point A on curve E and draw a tangent along A on it then the resultant of addition of same points is the reflection of the point where the tangent intersects the curve for the 2nd time.

2. From the given wikipedia link, the formula for point doubling and algorithm for point multiplication is clearly mentioned.
   
   ![Alt text](assets/ss1.png?raw=true)
   ![Alt text](assets/ss2.png?raw=true)

   I have used recursive algorithm for point multiplication. There are many more algorithms available there, you can use any of them.

3. This is my [script](assets/script.py) which will give you the required point B = (7166,3042)

FLAG: kernelkombat{7166_3042}
