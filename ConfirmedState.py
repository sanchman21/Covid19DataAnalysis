import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import requests

url = 'https://pomber.github.io/covid19/timeseries.json'
response = requests.request("GET", url)
data = response.json()

ans = input("Enter the name of the country to know how long it took for that country to become a recovery state.\n")
if (ans.lower() == 'usa') or (ans.lower() == 'us') or (ans.lower() == 'states') or (ans.lower() == 'united states of america') or (ans.lower() == 'the united states of america'):
    ans = 'US'
if (ans.lower() == 'uk') or (ans.lower() == 'england'):
    ans = 'United Kingdom'

weeklydata = {}
for countries in data:
    if countries.lower() == ans.lower():
        for day in range(0, len(data[countries])):
            death = data[countries][day]['confirmed']
            date = data[countries][day]['date']
            weeklydata.update({date: death})

correctdata = {}
for key, value in weeklydata.items():
    if value != 0:
        correctdata.update({key: value})
corona_df = pd.DataFrame({'ds': list(correctdata.keys()), 'y': list(correctdata.values())})
print(corona_df)

pro = Prophet(daily_seasonality=True)
pro.fit(corona_df)

future1 = pro.make_future_dataframe(periods=14)
prediction1 = pro.predict(future1)
pro.plot(prediction1)
plt.xlabel('Date')
plt.ylabel('Confirmed')
plt.legend(['Confirmed Predictions'])
print(type(prediction1))
plt.show()

