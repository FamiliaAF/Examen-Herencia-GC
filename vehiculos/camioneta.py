from vehiculos.vehiculo import Vehiculo
from vehiculos.todo_terreno import TodoTerreno

class Camioneta(Vehiculo, TodoTerreno):
  def cargar_carga(self):
    return "Cargando la carga"