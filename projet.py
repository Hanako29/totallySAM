#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Importation des modules
import re, sys, os
#re : fonction de recherche (re.search)
#sys : utilisation de la liste des paramètres
#os : exceptions

#***********************************************************************************************

#Main
def main(inputSam) :

    print(inputSam)
    
    print("Extraction : start") #Print for the beginning of the extraction step
    #print(extraction(inputSam)) #Uncomment for dictionnary printing
    extraction(inputSam) #Extract reads name, FLAG, CIGAR and TAG MD:Z from SAM file and import it in a dictionnary (Key = Flag) of dictionnary (Key = read names)
    print("Extraction : end") #Print for the end of the extraction
    
    print("Reads Analysis : Start") # Print for the begining of the reads analysis
    desc(extraction(inputSam)) #Count the number of unmapped reads, mapped reads, partially mapped reads and paires of mapped/unmapped reads and paires of mapped/partially mapped reads 
    print("Reads Analysis : End")
    

#Read file and reads extraction from SAM file
def extraction(inputSam) :
    
    with open(inputSam, "r") as fSam : #Open SAM file (reading)

        #We don't take the two first lines in SAM file for reads extraction
        next(fSam) #next function skip a line
        next(fSam)

        dicoExt = {} #create a dictionnary for extraction that will contains reads data
        
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

            #Appel de la fonction remplissage pour remplir le dictionnaire de dictionnaires
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
    pairedMapped1 = [99, 83, 67, 115, 81, 97, 65, 113, 147, 163, 131, 179, 161, 145, 129, 177] #1st read puis 2nd read
    pairedMapped2 = [147, 163, 131, 179, 161, 145, 129, 177] #2nd read
    #pairedMapUnmap = [73, 89, 121, 153, 185, 137] #just the mapped read
    pairedMapUnmap = [133, 165, 181, 101, 117, 69] #just the unmapped read
    pairedUnmapped = [77]
                    
    #compteurs
    m = 0 #mapped pour comparer boucle 1 et 2
    rm = 0 #mapped
    u = 0 #unmapped boucle 1
    ru = 0 #unmapped
    rp = 0 #partially mapped
    pm = 0 #pair perfectly mapped
    pmu = 0 #one mapped, one unmapped
    pmp = 0 #one mapped, one partially
    pmm = 0 #paire mapped mapped
    puu = 0 #paires unmapped unmapped
    ppu = 0 #paires partial unmapped
    

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

    nameMappedPerfect = []
    nameMappedPartially = []
    nameUnmapped = []
    
    for flag in dicoExt :
        for nomReads in dicoExt[flag]:
            if flag in mapped :
                if (dicoExt[flag][nomReads][1] == 'MD:Z:100' or dicoExt[flag][nomReads][0] == '100M'):
                    #print("je suis dans rm")
                    rm += 1
                    nameMappedPerfect.append(nomReads) #récupère les noms des reads parfaitement mappés
                else :
                    #print("je suis dans rp")
                    rp += 1
                    nameMappedPartially.append(nomReads)
                    if flag in pairedMapped1 and nomReads in nameMappedPerfect :
                        pmp += 1

            if flag in unmapped :
                ru +=1 #compte reads non mappés
                nameUnmapped.append(nomReads)
            if flag in pairedMapUnmap : #and nomReads in nameMappedPerfect:
                ppu += 1 #paires partiellement mappés/non mappés
                #print(nomReads)
            if flag in pairedMapUnmap and nomReads in nameMappedPerfect:
                pmu += 1
            if flag in pairedUnmapped :
                puu +=1

    #print(nameMappedPartially)
                
    print("reads perfectly mapped ",rm)
    print("reads partially mapped ", rp)
    print("total mapped (cm +cp) ", rm+rp)
    print("total mapped (boucle 1) ",m)
    print("reads unmapped (boucle n) ",ru)
    print("reads unmapped (boucle 1) ",u)
    print("paired partially mapped/unmapped ", ppu)
    print("paired mapped/unmapped ", pmu)
    print("paired mapped/partially mapped ",pmp)# pmu + pmp
    print("paired unmapped/unmapped ", puu) 
        
if len(sys.argv) == 2 : #Marche

    if os.stat(sys.argv[1]).st_size > 0 : #Marche

        if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith('.sam') : #Marche

            print("C'est un fichier Sam non vide")

            with open(sys.argv[1], "r") as file :
                ligne = file.readline()
                print(ligne)
                res = re.search("[^@].*", ligne) #vérifie que 1ère ligne a arobase
            
                if res :
                    print("Fichier non corrompu")
                    main(sys.argv[1])

                    #Ajouter condition ou j'ai pas ligne des reads

                else :
                    print("Fichier corrompu (aucune ligne sans arobase)")
                    sys.exit()
            
        else :

            print("Attention ce n'est pas un fichier, ou pas un fichier au format SAM")

        

    else :
            print("Le fichier est vide")
    
    #try :
        
    #    with open(sys.argv[1], "r") as file:
    #        ligne = file.readlines()
            #print(ligne)
    #        for i in ligne :
    #            if re.search("^[^@].*", i):
                    
           

    #except IOError :# as err :
        #print("OS error : {}".format(err))
    #    print("Le fichier est vide")
    #    sys.exit()

    #else :
    #    print("Processing")
        
else :
        print("Le nom du fichier à analyser doit être spécifié en premier argument (après l'appel du programme) et doit être un fichier sam")
