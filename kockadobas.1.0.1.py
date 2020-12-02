'''
Dobókocka számláló alkalmazás: Bármilyen fényviszony és háttér előtt
képes legyen megszámlálni maximum 4 db dobókocka összértékét illetve
a dobókockák darabszámát is jelezze ki.
'''
'''
    A feladat megoldásánál abból indultam ki, hogy minden dobókocka
    világos színű
'''

import numpy as np
import cv2

for i in range(12):
    if i+1<10:
         I = cv2.imread('0' + str(i+1) + '.jpg')
    else:
         I = cv2.imread(str(i+1) + '.jpg')

    # kép átméretezése a képerynőn való megjeleníthetőség kedvéért
    I= cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    x = 100/ I.shape[0]
    y = x

    I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)
    

    # Struktúráló elem
    k = np.ones((3, 3))

    # Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
    I = cv2.medianBlur(I, 7)
    I = cv2.morphologyEx(I, cv2.MORPH_CLOSE, k)

    mini = 240
    maxi = 255
    I = cv2.Canny(I, mini, maxi)
    
    x = 400 / I.shape[0]
    y = x

    I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)

    rows = I.shape[0]
    circles = cv2.HoughCircles(I, cv2.HOUGH_GRADIENT, 1, rows / 30,
                            param1=255, param2=20,
                            minRadius=1, maxRadius=60)

    korok =0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            print(center, i[2])
            # circle center
            cv2.circle(I, center, 1, (150), 1)
            # circle outline
            radius = i[2]
            cv2.circle(I, center, radius, (150), 1)
            korok= korok+1
    '''       
    print(I.shape)
    print("A dobas erteke:", korok)
    '''

    #Eredmeny kiiratasa
    text = 'Ossz.: ' + str(korok)             
    cv2.putText(I,text,(10,30),0,1,(200), 4, cv2.LINE_AA)
    

    cv2.imshow("detected circles", I)
    #cv2.imshow("I_median", I_median)
    #cv2.imshow("derivalt", I_derivalt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
