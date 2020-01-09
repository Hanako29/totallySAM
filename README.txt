~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                      totallySAM.py 1.0.0                                                  |
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
    - number of mapped/unmapped pairs, number of mapped/mapped reads, number of partially_mapped/mapped reads and the number 
      of partially_mapped/unmapped reads
    
  You can use it with an option to get, for partially mapped reads, the number of substitutions.
  The script has been coded under Python3.
  
  
If you have a mission for totallySAM.py : How to run totallySAM.py ?

  (1) Download totallySAM.py program on the GitHub
  (2) open your terminal
  (3) Go to the folder where you saved it
  (4) use the command line :
    
    Standard version
    < Python3 ./totallySAM.py samfile.sam >
    
    With variant calling option
    < Python3 ./totallySAM.py samfile.sam -v >
    
    The program need SAM format to run.
    
Issues : 
  - The program doesn't compute flag score so it doesn't take into account uncommon flag (it only use common flag that you 
    can find on https://www.samformat.info/sam-format-flag)
  
Commits :
  - 23-nov-2019 : the program only return pairs and reads information
  - 17-dec-2019 : the program check some file information to specify if the file is corrupted
  - 8-jan-2019 : the program can now (optionnaly) count and return variant number per reads
  
Licence :
  None
