import requests
from criptos import API_KEY,URL_TASA_ESPECIFICA

class CriptoValorModel:
    def __init__(self,origen:str, destino:str):
        self.origen=origen
        self.destino=destino
        
        self.tasa=0.00

    
    def obtener_tasa(self):
        self.respuesta=requests.get(URL_TASA_ESPECIFICA.format (self.origen,self.destino,API_KEY))
        self.tasa=round (self.respuesta.json()['rate'],2)
        