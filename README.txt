~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                         totallySAM.py                                                     |
|                                                       SAM file analysis                                                   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auteur :
  Anaïs Prud'homme
  M1 SNS - BCD
  HMIN113M 
  
Date :
  creation : 

Programme de statistiques d'alignement d'un fichier SAM 

Ce programme permet d'obtenir des statistiques basiques d'alignements de séquences de 100 paires de bases.

La première fonction "extraction" consiste à ouvrir le fichier SAM (fichier tabulé) et d'en extraire les données. Pour cela, la fonction divise le fichier par colonne (une colonne étant séparée d'une autre par une tabulation) et récupère les données nécessaires aux statistiques : le nom de la séquence, le FLAG, le cigar et le TAG MD:Z (ce dernier étant récupéré à partir d'une recherche d'expression réguière car il n'est pas présent pour toutes les séquences). Ensuite, à partir de la fonction remplissage, il va créer un dictionnaire qui aura pour clé le flag et pour valeur, un autre dictionnaire qui aura pour clé le nom de la séquence et pour valeur le cigar et le TAG MD:Z.

Le seconde grande fonction "desc" va comptabiliser : 
- les séquences non mappés,
- les séquences partiellement mappés,
- les paires de séquences où une séquence est mappée, la seconde non mappée
- les paires de séquences où une séquence est mappée, la seconde partiellement mappée
