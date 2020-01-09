~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                         totallySAM.py                                                     |
|                                                     SAM file analysis tool                                                |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author :
  Anaïs Prud'homme (prudhomme.anais.12@outlook.fr)
  M1 SNS - BCD
  HMIN113M 
  WOOHP coorporation
  
Date :
  creation date : 12-nov-2019
  first version : 09-jan-2020
  
Requierements :
  To accomplish its mission, totallySAM requires Python3.
  You can install Python3 by running :
    < sudo apt-get install python3 >
    
Description :
  totallySAM.py is a bioinformatic tool for SAM file analysis. 
  The standard programm will return :
    - Short file description
    - number of perfectly mapped reads, number of partially mapped reads and number of unmapped reads
    - number of mapped/unmapped pairs, number of mapped/mapped reads, number of partially_mapped/mapped reads and the number of partially_mapped/unmapped reads
    
  You can use it with an option to get, for partially mapped reads, the number of substitutions.
  The script has been coded under Python3
  
  
If you have a mission for totallySAM.py : How to run totallySAM.py ?
  To run totallySAM, you need to use the command line :
    
    Standard version
    < Python3 ./totallySAM.py samfile.sam >
    
    With variant calling option
    < Python3 ./totallySAM.py samfile.sam -v >
 

Programme de statistiques d'alignement d'un fichier SAM 

Ce programme permet d'obtenir des statistiques basiques d'alignements de séquences de 100 paires de bases.

La première fonction "extraction" consiste à ouvrir le fichier SAM (fichier tabulé) et d'en extraire les données. Pour cela, la fonction divise le fichier par colonne (une colonne étant séparée d'une autre par une tabulation) et récupère les données nécessaires aux statistiques : le nom de la séquence, le FLAG, le cigar et le TAG MD:Z (ce dernier étant récupéré à partir d'une recherche d'expression réguière car il n'est pas présent pour toutes les séquences). Ensuite, à partir de la fonction remplissage, il va créer un dictionnaire qui aura pour clé le flag et pour valeur, un autre dictionnaire qui aura pour clé le nom de la séquence et pour valeur le cigar et le TAG MD:Z.

Le seconde grande fonction "desc" va comptabiliser : 
- les séquences non mappés,
- les séquences partiellement mappés,
- les paires de séquences où une séquence est mappée, la seconde non mappée
- les paires de séquences où une séquence est mappée, la seconde partiellement mappée
