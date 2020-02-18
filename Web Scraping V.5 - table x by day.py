import requests
import pandas as pd
import numpy as np
import re
import glob
import os
#from Parameter1 import webscraping as ws
from Parameter1 import webscraping1 as ws
##ปี 2559มี 29 วัน##
#A= 28
#B= 30
#C= 31
y = 2562 #ค.ศ.
y1 = y-543 #พ.ศ.
URLDatefrom2 = '%2F'+str(y)
URLDateto2 = '%2F'+str(y)
df=[]
for o in range(1,13):
    #เดือน31 วัน: 1,3,5,7,8,10,12
    if o == 1 or o == 3 or o == 5 or o == 7 or o == 8:
        for d in range(1,32):
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                URLDatefrom1 = 'DateFrom=0'+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo=0'+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
            else:
                URLDatefrom1 = 'DateFrom='+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo='+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
    elif o == 10 or o == 12:
        for d in range(1,32):
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                URLDatefrom1 = 'DateFrom=0'+str(d)+'%2F'+str(o)
                URLDateto1 = '&txtDateTo=0'+str(d)+'%2F'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
            else:
                URLDatefrom1 = 'DateFrom='+str(d)+'%2F'+str(o)
                URLDateto1 = '&txtDateTo='+str(d)+'%2F'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
    #เดือน30 วัน: 4,6,9,11
    elif o == 4 or o ==  6 or o ==  9:
        for d in range(1,31):
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                URLDatefrom1 = 'DateFrom=0'+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo=0'+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
            else:
                URLDatefrom1 = 'DateFrom='+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo='+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
    elif o == 11:
        for d in range(1,31):
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                URLDatefrom1 = 'DateFrom=0'+str(d)+'%2F'+str(o)
                URLDateto1 = '&txtDateTo=0'+str(d)+'%2F'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
            else:
                URLDatefrom1 = 'DateFrom='+str(d)+'%2F'+str(o)
                URLDateto1 = '&txtDateTo='+str(d)+'%2F'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
    #เดือน28,29 วัน: 2
    else:
        for d in range(1,29):
            if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 or d == 7 or d == 8 or d == 9:
                URLDatefrom1 = 'DateFrom=0'+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo=0'+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)
            else:
                URLDatefrom1 = 'DateFrom='+str(d)+'%2F0'+str(o)
                URLDateto1 = '&txtDateTo='+str(d)+'%2F0'+str(o)
                df=ws(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1)

    df3=[]
    df3 = pd.DataFrame(df)
    filename="ยานพาหนะที่เกิดอุบัติเหตุ"+str(y1)
    file_path = "D:/"+filename+".csv"
    df3.to_csv(file_path)