from mascota.animal import Animal
from mascota.jugueton import Jugueton

class Perro(Animal, Jugueton):
  def ladrar(self):
    return "Guau Guau!"
