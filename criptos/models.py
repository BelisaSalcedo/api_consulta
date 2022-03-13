import requests
from criptos import  API_KEY, URL_TASA_ESPECIFICA
from criptos.errors import APIError, APIErrorKey

class CriptoValorModel:
    def __init__(self, origen = "", destino = ""):
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0

    def obtener_tasa(self):
        self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(
            self.origen,
            self.destino,
            API_KEY
            
        ))
        if self.respuesta.status_code ==401:
            print('Esta Key {} no es correcta. Debes introducir una clave correcta'.format (API_KEY))
            nuevaAPIKEY=input('introduce de nuevo la clave: ')
            self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen,self.destino,nuevaAPIKEY ))
            while self.respuesta.status_code ==401: 
                print('Esta Key {} no es correcta. Debes introducir una clave correcta'.format (nuevaAPIKEY))
                nuevaAPIKEY=input('introduce de nuevo la clave: ')
                self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen,self.destino,nuevaAPIKEY )) 
                
            #raise APIErrorKey
            
            
            
        elif self.respuesta.status_code != 200:
            print('Error generico')
            raise APIError(self.respuesta.json()["error"])
            

        self.tasa = round(self.respuesta.json()["rate"], 2)