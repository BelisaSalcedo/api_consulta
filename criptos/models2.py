import requests
from criptos import  API_KEY, URL_TASA_ESPECIFICA
from criptos.errors import APIError, APIErrorKey

class CriptoValorModel:
    def __init__(self, origen = "", destino = ""):
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0
 


    def obtener_tasa(self,APIKEY):
        
        self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(
            self.origen,
            self.destino,
            APIKEY
            
        ))
        if self.respuesta.status_code ==401:
            
            raise APIErrorKey
            
            
            
            
        if self.respuesta.status_code != 200:
            print('Error generico')
            raise APIError(self.respuesta.json()["error"])
            

        self.tasa = round(self.respuesta.json()["rate"], 2)