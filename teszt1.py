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

eredmenyek = []
kepdb = 0

f = open('Eredmeny_mert.txt', 'w')
f.write('Kep neve \t Dobas ertek\tkocka szama\n')   

dirname = './kepek'     # eleresi utvonal
dirlist = os.scandir(dirname)   # fajlok, es mappak listazasa mappából
for e in dirlist:   # vegig iteralunk a neveken
    kep = dirname + '/'+ e.name # teljes eleres
    kepe = cv2.haveImageReader(kep) #le ellenorizuk, hogy megfelel-e cv2-nek, nehogy egy mappa nevet kapjunk
    if (not kepe):
        print('\tEz nem kep')
    else:
        eredmeny = vizsgal(kep,0)   # az elso parameter a kepet adja at, a masodik a képek megjeleniteset engedelyezi
        print(kep)     # eredmeny: kor, kocka, waitKey(0) erteke
        kepdb += 1
        f.write(str(eredmeny[0]) + '\t' + str(eredmeny[1]) + '\t' + str(eredmeny[2]) + '\n')
        if eredmeny[3] == 113: # q -re kilepunk a kepek feldolgozasabol
            break
        cv2.destroyAllWindows()

f.close()