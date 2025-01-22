from mascota.perro import Perro
from electrodomesticos.televisor_inteligente import TelevisorInteligente  
from vehiculos.camioneta import Camioneta
from retos.clase_derivada import ClaseDerivada

mi_perro = Perro()
print(mi_perro.comer())
print(mi_perro.jugar())
print(mi_perro.ladrar())

mi_televisor = TelevisorInteligente()
print(mi_televisor.encender())         
print(mi_televisor.conectar_wifi())  
print(mi_televisor.streaming()) 

mi_camioneta = Camioneta()
print(mi_camioneta.arrancar())        
print(mi_camioneta.activar_4x4())    
print(mi_camioneta.cargar_carga())

objeto = ClaseDerivada()
print(objeto.metodo())