import numpy as np
import cv2
def vizsgal(kep, megjelenit):
    I = cv2.imread(kep)
    

    # kép átméretezése a vizsgálathoz, hogy a dobokocka pottyei kozel azonosak legyenek
    # Ezzel szeretném kiküszöbölni, hogy azonos távolságból, de más felbontással
    # készült képeken is mukodjon
    #print(I.shape)

    x = 2000 / I.shape[0]
    y = x

    I = cv2.resize(I, None, None, x, y, cv2.INTER_CUBIC)
    I_k = I.copy()

    I_kszurke = cv2.cvtColor(I_k.astype(np.uint8), cv2.COLOR_BGR2GRAY)

    I_kmedian = cv2.medianBlur(I_kszurke, 11)
    # Struktúráló elem
    k = np.ones((3, 3))

    # Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
    I_kmedian = cv2.morphologyEx(I_kmedian, cv2.MORPH_CLOSE, k)

    #mini = 250
    #maxi = 255
    #I_derivalt = cv2.Canny(I_median, mini, maxi)

    rows = I_kmedian.shape[0]
    circles = cv2.HoughCircles(I_kmedian, cv2.HOUGH_GRADIENT, 1, rows / 100,
                            param1=240, param2=23,
                            minRadius=1, maxRadius=50)
    korok =0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            #print(center, i[2])
            # circle center
            cv2.circle(I_k, center, 1, (255, 0, 0), 8)
            # circle outline
            radius = i[2]
            cv2.circle(I_k, center, radius, (0, 255, 0), 8)
            korok= korok+1
            
    x = 500 / I_k.shape[0]
    y = x

    I_k = cv2.resize(I_k, None, None, x, y, cv2.INTER_CUBIC)
    I_kmedian = cv2.resize(I_kmedian, None, None, x, y, cv2.INTER_CUBIC)

    ### Dobokockak szamlalasa ####

    x = 500 / I.shape[0]
    y = x
    I = cv2.resize(I, None, None, x, y, cv2.INTER_LINEAR)

    I_szurke = cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    I_median = cv2.medianBlur(I_szurke, 41)

    # Struktúráló elem
    k = np.ones((20, 20))
    
    mini = 0
    maxi = 40
    I_median = cv2.Canny(I_median, mini, maxi)
    # Morfológiai zárás. Az apró hibákat eltünteti az objektum felületén.
    I_median = cv2.morphologyEx(I_median, cv2.MORPH_CLOSE, k)
    #cv2.imshow("I_median", I_median)


    rows = I_median.shape[0]
    circles = cv2.HoughCircles(I_median, cv2.HOUGH_GRADIENT, 1, rows / 20,
                            param1=200, param2=15,
                            minRadius=10, maxRadius=60)
    kocka = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            #print(center, i[2])
            # circle center
            cv2.circle(I_k, center, 1, (255, 0, 0), 1)
            # circle outline
            radius = i[2]
            cv2.circle(I_k, center, radius+15, (255, 0, 0), 3)
            kocka= kocka + 1
    
    vege = 0
    if (megjelenit):

        ##------------###


        #Eredmeny kiiratasa
        text = 'Ossz.: ' + str(korok) + ' Kocka(k): ' + str(kocka)            
        cv2.putText(I_k,text,(10,30),0,1,(0,255,0), 4, cv2.LINE_AA)

        #cv2.imshow("I_szurke", I_szurke)

        #cv2.imshow("I_kmedian", I_kmedian)
        #cv2.imshow("I_median", I_median)
        #cv2.imshow("Kockak", I)
        cv2.imshow("detected circles " + kep, I_k)
        vege = cv2.waitKey(0)
        cv2.destroyAllWindows()
    return [kep,korok,kocka,vege]