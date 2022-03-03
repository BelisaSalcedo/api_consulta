import requests

endpoint='htt2F7DA908-0B7C-49CF-9F1E-53B5D6C224C6ps://rest.coinapi.io/v1/exchangerate/{}/{}?apikey='

moneda_from=input('moneda de origen: ')
moneda_to=input('Moneda a conseguir: ')

r=requests.get(endpoint.format(moneda_from,moneda_to))
print(round(r.json()['rate'],2))