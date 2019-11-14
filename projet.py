#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys

#***********************************************************************************************
##Lecture du fichier et extraction

def main(inputSam) :
    print(extraction(inputSam))
   

def extraction(inputSam) :
    with open("mapping.sam", "r") as fSam :
        print("Lancement de l'extraction")

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
            flag = col[1]
            nomReads = col[0]
            cigar = col[5]
            
            resTagMDZ = re.search("(MD\:Z\:.*?\t)", reads)
            if resTagMDZ :
                resTagMDZ = resTagMDZ.group(0)[:-1] #[:-1] enlève \t
                #tagMDZ.append(resTagMDZ)
                tagMDZ = resTagMDZ
            remplissage(dicoExt,flag,nomReads,cigar, tagMDZ)

        print("Fin extraction")
        
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

        
if len(sys.argv) == 2 :
    main(sys.argv[1])
else :
    print("Le nom du fichier à analyser doit être spécifié en premier argument (après l'appel du programme)")
