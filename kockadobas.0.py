'''
Dobókocka számláló alkalmazás: Bármilyen fényviszony és háttér előtt
képes legyen megszámlálni maximum 4 db dobókocka összértékét illetve
a dobókockák darabszámát is jelezze ki.
'''
'''
    A feladat megoldásánál abból indultam ki, hogy minden dobókocka
    fehér
'''

import numpy as np
import cv2

I = cv2.imread("07.jpg")


# kép átméretezése a képerynőn való megjeleníthetőség kedvéért
print(I.shape)

x = 300 / I.shape[0]
y = x

I = cv2.resize(I, None, None, x, y, cv2.INTER_NEAREST)

I_szurke = cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)

I_median = cv2.medianBlur(I, 21)
I = cv2.medianBlur(I_szurke, 31)

cv2.imshow("I", I)
cv2.imshow("I_szurke", I_szurke)
cv2.imshow("I_median", I_median)

cv2.waitKey(0)
cv2.destroyAllWindows()