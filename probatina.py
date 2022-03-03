import requests
respuesta =requests.get('https://rest.coinapi.io/v1/exchangerate/BTC?apikey=2F7DA908-0B7C-49CF-9F1E-53B5D6C224C6')
print (respuesta.status_code)
#print(respuesta.json())
data =respuesta.json()
print(data['rates'][3])