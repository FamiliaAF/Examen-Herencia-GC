from electrodomesticos.electrodomestico import Electrodomestico
from electrodomesticos.conectividad import Conectividad

class TelevisorInteligente(Electrodomestico, Conectividad):
  def streaming(self):
    return "Iniciando transmisión en línea"
