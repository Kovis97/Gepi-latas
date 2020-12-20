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

print("Vannak-e uj kepek? I/H")
valasz = input()
if valasz == "I" or valasz == "i":
    uj = 1
else:
    uj = 0

f = open('Eredmeny_mert.txt', 'w')
text = ("Kep neve \t Dobas ertek\tkocka szama\n")
if uj:
    b = open('Eredmeny_valos.txt', 'w')
    b.write(text)
f.write(text)   


dirname = './kepek'     # eleresi utvonal
dirlist = os.scandir(dirname)   # fajlok, es mappak listazasa mappából
for e in dirlist:   # vegig iteralunk a neveken
    kep = dirname + '/'+ e.name # teljes eleres
    kepe = cv2.haveImageReader(kep) #le ellenorizuk, hogy megfelel-e cv2-nek, nehogy egy mappa nevet kapjunk
    if (not kepe):
        print('\tEz nem kep')
    else:
        ## -------
        megjelenjen = 0 # Ezt kell átírni, ha ellenőrizni szeretnénk a program képi kimenetét változatlan adatbázis esetén.
        ## -------
        if uj:
            megjelenjen = 1 ## Ezt semmi kép nem írható át!!
        eredmeny = vizsgal(kep,megjelenjen)   # az elso parameter a kepet adja at, a masodik a képek megjeleniteset engedelyezi
        print(kep)     # eredmeny: kor, kocka, waitKey(0) erteke
        f.write(str(eredmeny[0]) + '\t' + str(eredmeny[1]) + '\t' + str(eredmeny[2]) + '\n')
        if uj:
            print('Adja meg a korok szamat: ')
            korok = int(input())
            print('Adja meg a kockak szamat: ')
            kockak = int(input())
            b.write(str(eredmeny[0]) + '\t' + str(korok) + '\t' + str(kockak) + '\n')
        
        
        if eredmeny[3] == 113: # q -re kilepunk a kepek feldolgozasabol
            break
        cv2.destroyAllWindows()
