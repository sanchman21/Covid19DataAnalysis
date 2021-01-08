import requests
import pandas as pd
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.covid19api.com/"

url = url + 'summary'  # This is the url from where the data is being extracted.
response = requests.request("GET", url)  # Get request is sent to the api for getting the data.
data = response.json()  # data is then stored in json format.
df = pd.DataFrame(columns=['Country', 'Total Confirmed', 'Total Deaths', 'Total Recovered', 'New Confirmed',
                           'New Deaths', 'New Recovered'])
countries = []
confirmed = []
deaths = []
recovered = []
newconfirmed = []
newdeaths = []
newrecovered = []
countries.append('Global')
confirmed.append(data['Global']['TotalConfirmed'])
deaths.append(data['Global']['TotalDeaths'])
recovered.append(data['Global']['TotalRecovered'])
newconfirmed.append(data['Global']['NewConfirmed'])
newdeaths.append(data['Global']['NewDeaths'])
newrecovered.append(data['Global']['NewRecovered'])
for nation in data['Countries']:
    countries.append(nation['Country'])
    confirmed.append(nation['TotalConfirmed'])
    deaths.append(nation['TotalDeaths'])
    recovered.append(nation['TotalRecovered'])
    newconfirmed.append(nation['NewConfirmed'])
    newdeaths.append(nation['NewDeaths'])
    newrecovered.append(nation['NewRecovered'])
df['Country'] = countries
df['Total Confirmed'] = confirmed
df['Total Deaths'] = deaths
df['Total Recovered'] = recovered
df['New Confirmed'] = newconfirmed
df['New Deaths'] = newdeaths
df['New Recovered'] = newrecovered
df.groupby(df['Country'])
df.to_excel(r'F:\COLLEGE\DATA STRUCTURES\VIRTUAL HACKATHON\CountriesPresentData\PresentData.xlsx', index=False)


