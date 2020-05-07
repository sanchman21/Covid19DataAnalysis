import requests
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.covid19api.com/"

country = input("Enter the country for which you want the data (Enter Global for global data)\n")

try:
    # Code for Global Data.
    if country.lower() == 'global':
        url = url + 'summary'  # This is the url from where the data is being extracted.
        response = requests.request("GET", url)  # Get request is sent to the api for getting the data.
        data = response.json()  # data is then stored in json format.
        ans = ''  # Declaring a string ans for storing the final answer in it.
        for i in data['Global']:
            if (i != 'NewConfirmed') & (i != 'NewDeaths') & (i != 'NewRecovered'):
                ans = ans + "\n" + i + ": " + str(data['Global'][i])  # Data extracted from the json data and stored in ans.
        print(ans)

    elif (country.lower() == 'usa') or (country.lower() == 'us') or (
            country.lower() == 'united states of america') or (
            country.lower() == 'the united states of america'):
        url = "https://corona.lmao.ninja/v2/countries/USA"  # api url for extracting data for US.

        payload = {}
        headers = {
            'Cookie': '__cfduid=d200d71060eb7fc135ca56ddd5f37e7041586929559'
        }

        response = requests.request("GET", url, headers=headers, data=payload)  # data being extracted from api using GET method.
        data = response.json()  # response stored in data as json.
        answer = "Total Cases: " + str(data['cases']) + "\n" + "Deaths: " + str(data['deaths']) + "\n" + "Recovered: " + str(data['recovered'])
        print(answer)  # printing the final answer extracted from json format in the string answer.
    else:
        if (country.lower() == 'uk') or (country.lower() == 'england') or (country.lower() == 'great britain'):
            country = 'United Kingdom'
        if country.lower() == 'uae':
            country = 'United Arab Emirates'
        country = country.replace(' ', '-').lower()
        url = url + 'summary'  # url for extracted info for other countries.
        response = requests.request("GET", url)  # data being extracted from api using GET method.
        data = response.json()  # response stored in data as json.
        final = ''
        for i in data['Countries']:
            if i['Country'].lower() == country:
                for j in i:
                    if (j != 'CountryCode') & (j != 'Slug') & (j != 'Date')\
                            & (j != 'NewConfirmed') & (j != 'NewDeaths') & (j != 'NewRecovered'):
                        final = final + '\n' + j + ': ' + str(i[j])
                print(final)  # printing the final answer extracted from json format in the string final.
except:
    print("The data hasn't been updated yet.")


