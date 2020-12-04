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

for i in range(12):
    if i+1<10:
         I = cv2.imread('0' + str(i+1) + '.jpg')
    else:
         I = cv2.imread(str(i+1) + '.jpg') 

    I_k = I

    # kép átméretezése a vizsgálathoz, hogy a dobokocka pottyei kozel azonosak legyenek
    # Ezzel csak azt lehet kiküszöbölni, hogy azonos távolságból, de más felbontással
    # készült képeken is mukodjon
    print(I.shape)

    x = 2000 / I_k.shape[0]
    y = x

    I_k = cv2.resize(I_k, None, None, x, y, cv2.INTER_CUBIC)

    I_szurke = cv2.cvtColor(I_k.astype(np.uint8), cv2.COLOR_BGR2GRAY)

    I_median = cv2.medianBlur(I_szurke, 7)
    # Struktúráló elem
    k = np.ones((3, 3))

    # Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
    I_median = cv2.morphologyEx(I_median, cv2.MORPH_CLOSE, k)

    mini = 250
    maxi = 255
    #I_derivalt = cv2.Canny(I_median, mini, maxi)

    rows = I_median.shape[0]
    circles = cv2.HoughCircles(I_median, cv2.HOUGH_GRADIENT, 1, rows / 100,
                            param1=245, param2=24 ,
                            minRadius=1, maxRadius=50)
    korok =0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            print(center, i[2])
            # circle center
            cv2.circle(I_k, center, 1, (255, 0, 0), 8)
            # circle outline
            radius = i[2]
            cv2.circle(I_k, center, radius, (0, 255, 0), 8)
            korok= korok+1
            

    ### Dobokockak szamlalasa ####

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

    kocka = 0
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
            kocka= kocka + 1


    ##------------###

    x = 500 / I_k.shape[0]
    y = x

    I_k = cv2.resize(I_k, None, None, x, y, cv2.INTER_CUBIC)
    x = 500 / I_median.shape[0]
    y = x

    I_median = cv2.resize(I_median, None, None, x, y, cv2.INTER_LINEAR)

    #Eredmeny kiiratasa
    text = 'Ossz.: ' + str(korok) + ' Kocka(k): ' + str(kocka)            
    cv2.putText(I_k,text,(10,30),0,1,(0,255,0), 4, cv2.LINE_AA)

    cv2.imshow("detected circles", I_k)
    cv2.imshow("I_median", I_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.destroyAllWindows()