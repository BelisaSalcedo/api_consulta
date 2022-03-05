from criptos.models import CriptoValorModel
from criptos.view import CriptoValorView
from criptos.errors import APIError

vista =CriptoValorView()
vista.pedir()

cvm=CriptoValorModel(vista.origen,vista.destino)
try:
    cvm.obtener_tasa()
    print (cvm.tasa)
except APIError:
    print ('NO se puede calcular la tasa')