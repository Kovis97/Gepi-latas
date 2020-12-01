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

I = cv2.imread("03.jpg")

# kép átméretezése a képerynőn való megjeleníthetőség kedvéért
print(I.shape)

x = 400 / I.shape[0]
y = x

I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)

I_szurke = cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)

I_median = cv2.medianBlur(I_szurke, 5)


# Struktúráló elem
k = np.ones((3, 3))

# Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
I_z = cv2.morphologyEx(I_szurke, cv2.MORPH_CLOSE, k)
I_mz = cv2.morphologyEx(I_median, cv2.MORPH_CLOSE, k)

mini = 250
maxi = 255
#I_derivalt = cv2.Canny(I_z, mini, maxi)
I_derivalt1 = cv2.Canny(I_median, mini, maxi)
#I_derivalt1 = cv2.blur(I_derivalt1, (2, 2))
#I_derivalt2 = cv2.Canny(I_mz, mini, maxi)
#I_derivalt2 = cv2.blur(I_derivalt2, (2, 2))

#I[I_derivalt1 > 0] = np.array((255,0,0))




rows = I_derivalt1.shape[0]
circles = cv2.HoughCircles(I_median, cv2.HOUGH_GRADIENT, 1, rows / 16,
                           param1=255, param2=10,
                           minRadius=1, maxRadius=6)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        print(center, i[2])
        # circle center
        cv2.circle(I_derivalt1, center, 1, (200), 1)
        # circle outline
        radius = i[2]
        cv2.circle(I_derivalt1, center, radius, (150), 1)

cv2.imshow("detected circles", I_derivalt1)






'''
# Sarok detektálás a Harris módszerrel.
# Bővebben: https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345
E = cv2.cornerHarris(I_szurke.astype(np.float32), 5, 5, 0.1)

I_k = np.zeros(I.shape)
# Ahol E értéke nagyobb, mint a maximumának a 0,01-szerese, ott az I értéke legyen (0, 0, 255). 
I_k[E > E.max() * 0.01] = np.array((255,0,0))
cv2.imshow("E",I_k)
'''

#cv2.imshow("I_szurke", I_szurke)
#cv2.imshow("I_median", I_median)
#cv2.imshow("I", I)
#cv2.imshow("I_z", I_z)
#cv2.imshow("I_derivalt I_z", I_derivalt)
#cv2.imshow("I_derivalt1 I_median", I_derivalt1)
#cv2.imshow("I_derivalt2 I_mz", I_derivalt2)

cv2.waitKey(0)
cv2.destroyAllWindows()