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
    mapped = [67, 73, 83, 89, 99, 115, 121, 131, 137, 147, 153, 163, 179, 185, 97, 145]
    unmapped = [63, 69, 77, 101, 117, 133, 141, 165, 181]

    #compteurs
    m = 0 #mapped pour comparer boucle 1 et 2
    cm = 0 #mapped
    cu = 0 #unmapped
    cp = 0 #partially mapped
    cmu = 0 #one mapped, one unmapped
    cmp = 0 #one mapped, one partially
    

    #boucle 1 : description rapide (juste reads mappés et non mappés)
    for flag in dicoExt :
        for nomReads in dicoExt[flag]:
            #print(flag)
            if flag in mapped :
            #    print("je suis dans mapped")
                m += 1
            elif flag in unmapped : #elif = else if
            #    print("là non")
                cu += 1
    print("mapped ", m)
    print("unmapped ", cu)
    print(m+cu)

    #for flag in dicoExt :
    #    for nomReads in dicoExt[flag]:
    #        print(dicoExt[flag][nomReads][1])
    
    #boucle 2 : réelle
    for flag in dicoExt :
        for nomReads in dicoExt[flag]:
            if flag in mapped :
                #print(dicoExt[flag][nomReads][1])
                if dicoExt[flag][nomReads][1] != 'MD:Z:100':
                    #print("je suis dans cp")
                    cp += 1
                else :
                    #print("je suis dans cm")
                    cm += 1
            #if flag in unmapped :
            #    if 

    print("perfectly mapped ",cm)
    print("partially mapped ", cp)
    print("total mapped (cm +cp) ", cm+cp)
    print("total mapped (boucle 1) ",m)



        
        
if len(sys.argv) == 2 :
    main(sys.argv[1])
else :
    print("Le nom du fichier à analyser doit être spécifié en premier argument (après l'appel du programme)")
