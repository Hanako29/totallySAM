#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys

#***********************************************************************************************
##Lecture du fichier et extraction

def main(inputSam) :
    dicoExt = {}
    extraction(inputSam)

def extraction(inputSam) :
    with open("mapping.sam", "r") as fSam :
        print("Lancement de l'extraction")
        
        for reads in fSam :
            refFlag = re.search("(^.*?\t\d{1,4}|^.*?\t\*)", reads)
            
            if refFlag : #car match pas les 2 premières lignes
                resRefFlag = refFlag.group(0)
                #print(resRefFlag)
                col = resRefFlag.split("\t")
                flag = col[1]
                #print(flag)
                

                #nomReads
                nomReads = col[0]
                #print(nomReads)

                #cigar
                resCig = re.search("(([0-9]+[MIDNSHPX=]+)+\t)", reads)
                if resCig:
                    cigar = resCig.group(0)
                    #print(cigar)

                #tag
                resTag=re.search("(MD\:Z\:([0-9]+[ATGC])+|MD\:Z\:([0-9])+)")
                if resTag :
                    tag = resTag.group(0)
                    print(tag)
                
                
                #if flag in dicoExt :
                #    dicoExt[flag] = append([nomReads])
                #else :
                #    dicoExt[flag] = 
                    
        print("nombre d'occurence flags", len(nomReads))
        print("nombre d'occurence nomReads", )    
        print("nombre d'occurence cigar",)
            
            #Remplissage du dico avec
            
            #cigar = re.search("(([0-9]+[MIDNSHPX=])+)")]
            #if flag in dicoExt :
            #    dicoExt[flag] = desc.append([])
            #else :
            #dicoExt[flag] = [[re.search("(([0-9]+[MIDNSHPX=])+)")]]

        #print(dicoExt)





        
if len(sys.argv) == 2 :
    main(sys.argv[1])
else :
    print("Le nom du fichier à analyser doit être spécifié en premier argument (après l'appel du programme)")
