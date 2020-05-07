#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Problem Statement 3:
#3.1 Find out the Average number of days it took for a confirmed case to turn
#to a death state in any country. Which country took the maximum number of days?
#3.2 Find out the Average number of days it took a confirmed case to turn to a
#recovery state in any country . Which country took the maximum number of days?


import requests
import matplotlib.pyplot as plt

url = 'https://pomber.github.io/covid19/timeseries.json'
response = requests.request("GET", url)
data = response.json()
ans = input("Enter the name of the country to know how long it took for that country to become a death state.\n")
if (ans.lower() == 'usa') or (ans.lower() == 'us') or (ans.lower() == 'states') or (ans.lower() == 'united states of america') or (ans.lower() == 'the united states of america'):
    ans = 'US'
if (ans.lower() == 'uk') or (ans.lower() == 'england'):
    ans = 'United Kingdom'
if (ans.lower() == 'china'):
    print("Death State Data is not available for China as worldwide data has been recorded from 22nd January, 2020.")
    exit()
for countries in data:
    if countries.lower() == ans.lower():
        x = range(0, len(data[countries]))
        for j in x:
            if data[countries][j]['confirmed'] >= 1:
                break
        for i in x:
            if 0 < data[countries][i]['deaths'] == 1:
                days = i-j+1
                print("The number of days taken for " + ans + " to become a death state is " + str(days) + ".")
                break
                
Ans = input("Enter the name of the country to know how long it took for that country to become a recovery state.\n")               
for countries in data:
    if countries.lower() == Ans.lower():
        x = range(0, len(data[countries]))
        for j in x:
            if data[countries][j]['confirmed'] >= 1:
                break
        for i in x:
            if 0 < data[countries][i]['recovered']:
                days = i-j+1
                print("The number of days taken for " + Ans + " to become a recovery state is " + str(days) + ".")
                break


# In[ ]:




