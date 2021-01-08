import requests
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime

url = 'https://pomber.github.io/covid19/timeseries.json'

response = requests.request("GET", url)
data = response.json()
lst = []

for index in data['Afghanistan']:
    lst.append({'date': index['date']})
GlobalData = {'Global': lst}


x = range(0, len(data['Afghanistan']))
for i in x:
    confirmed = 0
    deaths = 0
    recovered = 0
    for country in data:
        confirmed = confirmed + data[country][i]['confirmed']
        deaths = deaths + data[country][i]['deaths']
        recovered = recovered + data[country][i]['recovered']
    GlobalData['Global'][i].update({'confirmed': confirmed})
    GlobalData['Global'][i].update({'deaths': deaths})
    GlobalData['Global'][i].update({'recovered': recovered})
data.update(GlobalData)
df = pd.DataFrame(columns=['Country', 'Date', 'Total Confirmed', 'Total Deaths', 'Total Recovered'])
country = []
date = []
Confirmed = []
Deaths = []
Recovered = []
for nation in data:
    for x in range(0, len(data[nation])):
        if data[nation][x]['confirmed'] != 0:
            country.append(nation)
            date.append(datetime.strptime(data[nation][x]['date'], '%Y-%m-%d').date())
            Confirmed.append(data[nation][x]['confirmed'])
            Deaths.append(data[nation][x]['deaths'])
            Recovered.append(data[nation][x]['recovered'])
df['Country'] = country
df['Date'] = date
df['Total Confirmed'] = Confirmed
df['Total Deaths'] = Deaths
df['Total Recovered'] = Recovered
df.to_excel(r'F:\COLLEGE\DATA STRUCTURES\VIRTUAL HACKATHON\CountriesTimeSeriesData\TimeSeriesData.xlsx', index=False)