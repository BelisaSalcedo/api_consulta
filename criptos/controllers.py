from criptos.models import CriptoValorModel
from criptos.view import CriptoValorView
from criptos.errors import APIError,APIErrorKey
import requests
from criptos import API_KEY, URL_TASA_ESPECIFICA

class CriptoValorController:
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel()
        

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
       
        self.modelo.obtener_tasa()
     
         
            
        self.vista.mostrar(self.modelo.tasa)
       
        