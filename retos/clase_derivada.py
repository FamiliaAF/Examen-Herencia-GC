from retos.clase_a import ClaseA
from retos.clase_b import ClaseB

class ClaseDerivada(ClaseA, ClaseB):
  def metodo(self):
    return f"{super().metodo()} y luego el método de ClaseB"
