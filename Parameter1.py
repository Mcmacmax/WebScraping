import requests
import pandas as pd
import numpy as np
import re
import glob
import os
from bs4 import BeautifulSoup
URL1 = 'http://appgis.mot.go.th/trams/default.aspx?txtFestival=0&txtFestivalName=&txt'
URL2 = '&modeWeb=0&modePdf=0&publicYear=0&txtReportDate=06%2F02%2F2563&txtReportTime=09%3A15&txt'
URL3 = '&txtTimeStop=LONG&txtCar=0&txtDept=&isEvent=2'
ProvinceDict = {
10:	"Bangkok",
11:	"Samut Prakarn",
12:	"Nonthaburi",
13:	"Pathum Thani",
14:	"Phra Nakhon Si Ayutthaya",
15:	"Ang Thong",
16:	"Lop Buri",
17:	"Sing Buri",
18:	"Chai Nat",
19:	"Saraburi",
20:	"Chon Buri",
21:	"Rayong",
22:	"Chanthaburi",
23:	"Trat",
24:	"Chachoengsao",
25:	"Prachin Buri",
26:	"Nakhon Nayok",
27:	"Sa kaeo",
30:	"Nakhon Ratchasima",
31:	"Buri Ram",
32:	"Surin",
33:	"Si Sa Ket",
34:	"Ubon Ratchathani",
35:	"Yasothon",
36:	"Chaiyaphum",
37:	"Amnat Charoen",
38:	"Bueng Kan",
39:	"Nong Bua Lam Phu",
40:	"Khon Kaen",
41:	"Udon Thani",
42:	"Loei",
43:	"Nong Khai",
44:	"Maha Sarakham",
45:	"Roi Et",
46:	"Kalasin",
47:	"Sakon Nakhon",
48:	"Nakhon Phanom",
49:	"Mukdahan",
50:	"Chiang Mai",
51:	"Lamphun",
52:	"Lampang",
53:	"Uttaradit",
54:	"Phrae",
55:	"Nan",
56:	"Phayao",
57:	"Chiang Rai",
58:	"Mae Hong Son",
60:	"Nakhon Sawan",
61:	"Uthai Thani",
62:	"Kamphaeng Phet",
63:	"Tak",
64:	"Sukhothai",
65:	"Phitsanulok",
66:	"Phichit",
67:	"Phetchabun",
70:	"Ratchaburi",
71:	"Kanchanaburi",
72:	"Suphan Buri",
73:	"Nakhon Pathom",
74:	"Samut Sakhon",
75:	"Samut Songkhram",
76:	"Phetchaburi",
77:	"Prachuap Khiri Khan",
80:	"Nakhon Si Thammarat",
81:	"Krabi",
82:	"Phang-nga",
83:	"Phuket",
84:	"Surat Thani",
85:	"Ranong",
86:	"Chumphon",
90:	"Songkhla",
91:	"Satun",
92:	"Trang",
93:	"Phatthalung",
94:	"Pattani",
95:	"Yala",
96:	"Narathiwat",
}
df=[]

def webscraping(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1):
    for i in ProvinceDict: 
        print("Province : ",ProvinceDict[i],"Date :",d,"Month :",o,"Year :",y1)
        URLPROV = 'Prov='+str(i)
        url = URL1+URLDatefrom1+URLDatefrom2+URLDateto1+URLDateto2+URL2+URLPROV+URL3
        #print(url)
        data = requests.get(url)
        soup = BeautifulSoup(data.text,'html.parser')
        x = soup.find_all("table",{"class":"MISTable BlackBorderTable"}) # <- ค้นหาตาราง
        Col1 = x[2].get_text()
        new = Col1.replace('\n\n\n', ';')
        row_list = new.split(';')
        for r in row_list:
            df.append(r.split('\n'))
        length = len(df)
        q=0
        while q < length:
            df[q].insert(27,ProvinceDict[i])
            df[q].insert(28,str(d)+"/"+str(o)+"/"+str(y1))
            q +=1
    return(df)

def webscraping1(URLDatefrom2,URLDateto2,URLDatefrom1,URLDateto1,d,o,y1):
    print("Date :",d,"Month :",o,"Year :",y1)
    URLPROV = 'Prov=0'
    url = URL1+URLDatefrom1+URLDatefrom2+URLDateto1+URLDateto2+URL2+URLPROV+URL3
    #print(url)
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("table",{"class":"MISTable BlackBorderTable"}) # <- ค้นหาตาราง
    Col1 = x[4].get_text()
    new = Col1.replace('\n\n\n', ';')
    row_list = new.split(';')
    for r in row_list:
        df.append(r.split('\n'))
    length = len(df)
    q=0
    while q < length:
        #df[q].insert(27,ProvinceDict[i])
        df[q].insert(28,str(d)+"/"+str(o)+"/"+str(y1))
        q +=1
    return(df)
