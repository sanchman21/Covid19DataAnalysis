#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem Statement 1:
#1. Identity the countries as HIGH RISK TRAVEL destination countries for Internship
#       or Project work for next two years.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import requests
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

style.use('fivethirtyeight')

url = "https://api.covid19api.com/total/dayone/country/"
url2 = "https://api.covid19api.com/countries"

print("\n HIGH RISK COUNTRIES (DGR > 2%) : \n")

try :
    print("Sl No.      " + "COUNTRY".ljust(40," ") + "DEATH GROWING RATE \n")    

    response2 = requests.request("GET", url2)
    data2 = response2.json()

    hrc = []
    hrc2 = []
    k=0
    for i in data2 :
        #break
        try :
            url = "https://api.covid19api.com/total/dayone/country/"
            url = url + i["Slug"]

            response = requests.request("GET", url)
            data = response.json()

            max1=0.0
            for j in data :
                c=float(j["Confirmed"])
                d=float(j["Deaths"])
        
                if c==0 :
                    dgr=0            
                else :
                    dgr=(d/c)*100

                if max1<dgr and c>=100 :
                    max1=dgr                                       
                
            if max1>=2 :
                k=k+1
                hrc.append(i["Country"])
                hrc2.append(max1)
                print((str(k) + ". ").rjust(6," ") + "      " + i["Country"].ljust(40," ") + str(max1))

        except :
            print(("------------The country " + i["Country"] + " had some data problem ").ljust(80,"-") + " Check your connection and try again.")
except :
    print("Data problem : Check your connection and try again")

print("")
#print(hrc)

n=10
if k<10 :
    n=k

for i in range(0,n) :
    max1=0
    for j in range(i,k) :
        if max1<hrc2[j] :
            max1=hrc2[j]
            p=j
    t2=hrc2[i]
    hrc2[i]=hrc2[p]
    hrc2[p]=t2
    t1=hrc[i]
    hrc[i]=hrc[p]
    hrc[p]=t2

print("\n TOP 10 HIGH RISK COUNTRIES : \n")
print("Sl No.      " + "COUNTRY".ljust(40," ") + "DEATH GROWING RATE \n") 

for i in range(0,n) :
    print((str(i+1) + ". ").rjust(6," ") + "      " + hrc[i].ljust(40," ") + str(hrc2[i]))

print("\n")

while True :
    a = input("Enter a Country to know it's DEATH GROWING RATE (Enter 0 to exit) : ")
    print("")
    if a == '0' :
        break
    else :
        try :
            a = a.lower()            
            url = "https://api.covid19api.com/total/dayone/country/"

            if (a == 'usa') or (a == 'us') or (a == 'united states of america') or (a == 'the united states of america') :
                a = "united states"
            elif (a == 'uk') or (a == 'england') or (a == 'great britain'):
                a = "united kingdom"
            elif a == 'uae':
                a = 'united arab emirates'

            url = url + a.replace(" ","-")

            response = requests.request("GET", url)
            data = response.json()

            i=0
            x=[0]
            x2=[]
            y=[0]
            y2=[]         
            for j in data :
                i=i+1
                c=float(j["Confirmed"])
                d=float(j["Deaths"])
        
                if c==0 :
                    dgr=0            
                else :
                    dgr=(d/c)*100

                x.append(i)
                x2.append("  Day : "+str(i)+"\n"+j["Date"][8:10]+"-"+j["Date"][5:7]+"-"+j["Date"][0:4]+"\n")
                y.append(dgr)
                y2.append(dgr)            

            plt.plot(x2,y2,c='r',linewidth=1.5)
            plt.subplots_adjust(left=0.12, bottom=0.14, right=0.92, top=0.9)
            plt.xticks(np.arange(min(x), max(x)+1, 12.0))            
            plt.xlabel('Date (From the first coronavirus case)',fontsize=15,weight='bold') 
            plt.ylabel('Death Growing Rate\n',fontsize=15,weight='bold')            
            plt.title("DEATH GROWING RATE of " + a.title() ,fontsize=18,weight='bold') 
            plt.show()

            resp=int(input("    Do you want to see details for the above graph? (Press 1 for Yes (or) Press 0 for No): "))
            print("")
            if resp == 1:
                i=0                           
                for j in data :
                    i=i+1
                    c=float(j["Confirmed"])
                    d=float(j["Deaths"])
        
                    if c==0 :
                        dgr=0            
                    else :
                        dgr=(d/c)*100
                
                    if i==1 :
                        print("      DAY     DATE          CONFIRMED      DEATHS       DEATH GROWING RATE (in %)")

                    print("    " + (str(i) + ".    ").rjust(10," ") + str(j["Date"][0:10]) + "    " + str(int(c)).rjust(10," ") + "    " + str(int(d)).rjust(8," ") + "      " ,end="")
                    print(f'{dgr:9.4f}')
                print("")  
        except :                
            print("    The country '" + a + "' had some data problem \n--- Check your connection and try again (or) Check the country name again.---\n")

print("\nEXIT Successful. \nThank You. \n")

