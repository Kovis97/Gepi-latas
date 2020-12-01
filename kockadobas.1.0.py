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

I = cv2.imread("06.jpg")

# kép átméretezése a képerynőn való megjeleníthetőség kedvéért
print(I.shape)

x = 100/ I.shape[0]
y = x

I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)

I_szurke = cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)


# Struktúráló elem
k = np.ones((6, 6))

# Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
I_median = cv2.morphologyEx(I_szurke, cv2.MORPH_CLOSE, k)
I_median = cv2.medianBlur(I_szurke, 7)

mini = 240
maxi = 255
I_derivalt = cv2.Canny(I_median, mini, maxi)

rows = I_median.shape[0]
circles = cv2.HoughCircles(I_derivalt, cv2.HOUGH_GRADIENT, 1, rows / 10,
                           param1=255, param2=5,
                           minRadius=1, maxRadius=6)

korok =0
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        print(center, i[2])
        # circle center
        cv2.circle(I_median, center, 1, (255, 0, 0), 1)
        # circle outline
        radius = i[2]
        cv2.circle(I_median, center, radius, (0, 255, 0), 1)
        korok= korok+1
        
print(I.shape)
print("A dobas erteke:", korok)

x = 400 / I.shape[0]
y = x

I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)

I_median = cv2.resize(I_median, None, None, x, y, cv2.INTER_LINEAR)

#Eredmeny kiiratasa
text = 'Ossz.: ' + str(korok)             
cv2.putText(I_median,text,(10,30),0,1,(0,255,0), 4, cv2.LINE_AA)

cv2.imshow("detected circles", I)
cv2.imshow("I_median", I_median)
cv2.imshow("derivalt", I_derivalt)
cv2.waitKey(0)
cv2.destroyAllWindows()
