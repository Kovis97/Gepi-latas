dirname = './kepek'     # eleresi utvonal
'''
Dobókocka számláló alkalmazás: Bármilyen fényviszony és háttér előtt
képes legyen megszámlálni maximum 4 db dobókocka összértékét illetve
a dobókockák darabszámát is jelezze ki.
'''
'''
    A feladat megoldásánál abból indultam ki, hogy minden dobókocka
    fehér
'''
from vizsgalat import vizsgal
import numpy as np
import cv2
import os

def megjelenit(kep):
    kepe = cv2.haveImageReader(kep) #le ellenorizuk, hogy egy kep utvolat kaptuk-e meg
    if (not kepe):
        print(str(kep) + ':\tEz nem kep!')
    else:
        eredmeny = vizsgal(kep,1)   # az elso parameter a kepet adja at, a masodik a képek megjeleniteset engedelyezi
        print(kep)     # eredmeny: kor, kocka, waitKey(0) erteke
        cv2.destroyAllWindows()
        if eredmeny[3] == 113: # q -re kilepunk a kepek feldolgozasabol
            return -1



print("Kérem adja meg a kep elérési útvonalát,\nkülönben ./kepek mappa tartalma jelenik meg,\nez esetben a 'q' lenyomásával kiléphet:")
utvonal = input()

if utvonal:
    megjelenit(utvonal)
else:
    dirlist = os.scandir(dirname)   # fajlok, es mappak listazasa mappából
    for e in dirlist:   # vegig iteralunk a neveken
        utvonal = dirname + '/'+ e.name # teljes eleres
        if megjelenit(utvonal):
            break

cv2.destroyAllWindows()
    
