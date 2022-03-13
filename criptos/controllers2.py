from criptos.models2 import CriptoValorModel
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
        conectado=False
        nueva_ApiKey=API_KEY
        while conectado==False:
            try:
                
                self.modelo.obtener_tasa(nueva_ApiKey)
                self.vista.mostrar(self.modelo.tasa)
                conectado=True
            except APIErrorKey:
                print('La clave es incorrecta')
                nueva_ApiKey=input('Debes introducir una clave correcta')
               
                
                
            
           
               
     
         
            
        
       
        