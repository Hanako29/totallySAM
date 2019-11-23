#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys
#re pour la fonction de recherche (re.search)



#***********************************************************************************************
##Lecture du fichier et extraction

def main(inputSam) :
    print("Lancement de l'extraction")
    #print(extraction(inputSam))
    extraction(inputSam)
    print("Fin extraction")
    desc(extraction(inputSam))
    

def extraction(inputSam) :
    with open("mapping.sam", "r") as fSam :
        
        next(fSam) #Saute la 1ere ligne
        next(fSam) #Saute la 2eme ligne

        dicoExt = {} #dico d'extraction
        #flag = []
        #nomReads = []
        #cigar = []
        #tagMDZ = []
        
        for reads in fSam :
            col = reads.split("\t")
            #flag.append(col[1])
            #nomReads.append(col[0])
            #cigar.append(col[5])
            flag = int(col[1])  #int permet de les convertir en entiers
            nomReads = col[0]
            cigar = col[5]
            
            resTagMDZ = re.search("(MD\:Z\:.*?\t)", reads)
            if resTagMDZ :
                resTagMDZ = resTagMDZ.group(0)[:-1] #[:-1] enlève \t
                #tagMDZ.append(resTagMDZ)
                tagMDZ = resTagMDZ
            remplissage(dicoExt,flag,nomReads,cigar, tagMDZ)

 
        
        return dicoExt
        

        #print(flag)
        #print(nomReads)
        #print(cigar)
        #print(tagMDZ)
        #print(len(flag))
        #print(len(nomReads))
        #print(len(cigar))
        #print(len(tagMDZ))
        #Même longueur de la liste partout sauf tagMDZ (mais c'est une info optionnelle)

        
    
def remplissage(dicoExt, flag, nomReads, cigar, tagMDZ) :

    if flag in dicoExt :
        dicoExt[flag][nomReads] = [cigar, tagMDZ]
    else :
        dicoExt[flag] = {nomReads : [cigar, tagMDZ]}



def desc(extraction) : #pas besoin de mettre l'input quand prend une entrée une fonction
    #Par contre, mettre l'input dans le main

    dicoExt = extraction #nécessaire pour utiliser mon dico
    #print(dicoExt)

    #listes de possibilité
    mapped = [67, 73, 83, 89, 97, 99, 115, 121, 131, 137, 145, 147, 153, 163, 179, 185]
    unmapped = [63, 69, 77, 101, 117, 133, 141, 165, 181]


    #compteurs
    m = 0 #mapped pour comparer boucle 1 et 2
    rm = 0 #mapped
    u = 0 #unmapped boucle 1
    ru = 0 #unmapped
    cp = 0 #partially mapped
    pmu = 0 #one mapped, one unmapped
    pmp = 0 #one mapped, one partially
    

    #boucle 1 : description rapide (juste reads mappés et non mappés)
    for flag in dicoExt :
        for nomReads in dicoExt[flag]:
            #print(flag)
            if flag in mapped :
            #    print("je suis dans mapped")
                m += 1
            elif flag in unmapped : #elif = else if
            #    print("là non")
                u += 1
    print("total reads boucle ",m+u)

    #for flag in dicoExt :
    #    for nomReads in dicoExt[flag]:
    #        print(dicoExt[flag][nomReads][0])   

    
    #for flag in dicoExt :
    #    for nomReads in dicoExt[flag]:
    #        print(dicoExt[flag][nomReads][1])

 
    
    #boucle 2 : réelle
    for flag in dicoExt :
        for nomReads in dicoExt[flag]:
            if flag in mapped :
                if (dicoExt[flag][nomReads][1] != 'MD:Z:100' or dicoExt[flag][nomReads][0] != '100M'):
                    #print("je suis dans cp")
                    rp += 1
                else :
                    #print("je suis dans cm")
                    rm += 1
            if flag in unmapped :
                ru +=1
            if flag in


    print("reads perfectly mapped ",rm)
    print("reads partially mapped ", rp)
    print("total mapped (cm +cp) ", rm+rp)
    print("total mapped (boucle 1) ",m)
    print("reads unmapped (boucle n) ",ru)
    print("reads unmapped (boucle 1) ",u)



        
        
if len(sys.argv) == 2 :
    main(sys.argv[1])
else :
    print("Le nom du fichier à analyser doit être spécifié en premier argument (après l'appel du programme)")
